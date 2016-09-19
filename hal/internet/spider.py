# !/usr/bin/python
# coding: utf_8

# Copyright 2016 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


""" create and run simple web crawler """

import queue
import calendar
import os
import socket
import string
import sys
import threading
import time

from hal.computer import shell
from hal.internet.web import Webpage


class SpiderThread(threading.Thread):
    """ thread that helps Spider to crawl the web """

    def __init__(self, boss, queue, pool, recall, timeout, max_pages, domains, name):
        """
        :param queue: queue where to fetch urls
        :param pool: hash-table where to store results
        :param recall: max number of attempts to get web_page answer
        :param timeout: time (ms) to wait for web_page answer
        :param name: how would you call a spider-thread??
        :return: new SpiderThread
        """

        threading.Thread.__init__(self)
        self._stop = threading.Event()
        self.boss = boss  # data
        self.can_get_lock = False
        self.queue = queue
        self.pool = pool

        self.name = name  # log
        self.log = "INIT"
        self.verbose_log = self.name + ' has been created'
        self.stats = ''

        self.web_page = ''  # pages
        self.url = ''
        self.links = []
        self.avg_time_crawling = 0

        self.recall = recall  # settings
        self.timeout = timeout
        self.max_pages = max_pages
        self.domains = domains

    def am_i_done(self):
        """
        :return: true iff queue is empty or enough pages fetch
        """

        for attempt in range(10):
            if not len(self.pool) >= self.max_pages:  # or not self.queue.empty()
                return False
            time.sleep(0.1)
        return True

    @property
    def is_working(self):
        """
        :return: is working?
        """

        return self.is_crawling or self.is_updating

    @property
    def is_crawling(self):
        """
        :return: is crawling?
        """

        return self.log == "CRAWLING"

    @property
    def is_updating(self):
        """
        :return: is updating?
        """

        return self.log == "UPDATING"

    @property
    def is_page_known(self):
        """
        :return: is current url already visited?
        """

        return self.url in self.pool

    @property
    def is_url_approved(self):
        """
        :return: url approval by looking up robots.txt file and already visited pages
        """

        can_crawl_domain = True  # can crawl domain?
        if len(self.domains) > 0:
            pass  # look in domains

        return not self.is_page_known and can_crawl_domain
        # ... and utils.can_be_crawled(self.url, '*')

    def run(self):
        """
        :return: crawl just fetched url from queue
        """

        can_exit = False
        while not can_exit:
            self.log = "CRAWLING"  # get page and update log
            self.web_page = Webpage(self.queue.get())
            self.url = self.web_page.url
            self.verbose_log += '\n' + self.name + ' starting crawling ' + self.url            
            self.boss.next_crawl = self.url  # update boss page stats
            
            if self.is_url_approved:  # wait for approval and avoid spider traps
                self.boss.current_crawling = self.url  # update boss page stats

                try:  # get links
                    socket.setdefaulttimeout(self.timeout)   # setting timeout
                    self.links = self.web_page.links
                    self.verbose_log += '\n' + self.name + ' extracted ' + str(len(self.links)) + ' links from ' + self.url
                    self.log = "CRAWLED"
                    self.update()  # update queue, pool and local repo
                except:
                    self.log = "DISCARDED"
                finally:
                    self.log = "IDLE"
                    self.queue.task_done()
                    can_exit = self.am_i_done()
            else:
                self.log = "DISCARDED"

        self.boss.stop_thread(self)

    def update_lock(self):
        """
        :return: True iff can get ros available
        """

        self.can_get_lock = self.boss.can_get_lock

    def block_lock(self):
        """
        :return: block any other thread from getting res available
        """

        self.boss.can_get_lock = False
        self.update_lock()

    def release_lock(self):
        """
        :return: block any other thread from getting res available
        """

        self.boss.can_get_lock = True
        self.update_lock()

    def update(self):
        """
        :return: update local repo, queue and already visited sites
        """

        self.boss.last_crawled = self.url  # page stats
        self.log = "UPDATING"  # log and repo
        self.verbose_log += '\n' + self.name + ' getting control over pool and updating..'  # lock for global variable g_URLs
        
        while not self.can_get_lock:  # wait for lock
            self.update_lock()
            self.log = "WAITING"

        
        self.block_lock()  # eventually it will get resources available, then block resources and update
        self.update_queue()
        self.update_pool()
        self.update_repo()        
        self.release_lock()  # release lock -> all other threads can work on it
        self.verbose_log += '\n' + self.name + ' updated queue and local repo; now releasing control over pool..'

    def update_queue(self):
        """
        :return: update main queue of websites to be visited
        """

        for link in self.links:  # update queue with newly found links
            self.queue.put(str(link))

        self.boss.pages_in_queue = self.queue.qsize()  # update boss page stats
        self.boss.pages_crawled += 1

    def update_pool(self):
        """
        :return: update main pool of already visited websites
        """

        self.verbose_log += '\n' + self.name + ' updating pool..'
        self.pool[self.url] = string.join(self.links, ',')

    def update_repo(self):
        """
        :return: update local repo
        """

        self.verbose_log += '\n' + self.name + ' updating local repo..'


class Spider(object):
    """ crawls the web """
    
    UPDATE_INTERVAL = 0  # interval at which sample threads for status and log

    def __init__(self, config, starter, recall, timeout, max_pages, max_threads, domains, output, name):
        """
        :param starter: web-page where to start crawler
        :param recall: max number of attempts to get web_page answer
        :param timeout: time (ms) to wait for web_page answer
        :param max_pages: max number of web-pages to crawl
        :param max_threads: max number of threads to share job with
        :param domains: array of domain to restrict crawler
        :param output: folder where to store results
        :param config: file where results from previous crawl are stored
        :param name: name of spider
        :return: new crawler
        """

        self.can_get_lock = True  # data
        self.queue = queue.Queue()
        self.pool = dict()
        self.threads = []
        self.name = name  # log
        self.can_update = True
        self.log = "INIT"
        self.verbose_log = 'spider has been created'
        self.stats = ''
        self.config = config  # I/O
        self.output = output
        self.next_crawl = starter  # pages
        self.current_crawling = ''
        self.last_crawled = ''
        self.pages_crawled = 0
        self.pages_in_queue = 0
        self.avg_time_crawling = 0
        self.start_time = 0
        self.running_time = 0
        self.ETA = 0
        self.recall = recall  # settings
        self.timeout = timeout
        self.max_pages = max_pages
        self.max_threads = max_threads
        self.domains = domains

    def get_log(self):
        """
        :return: simple (not extensive) log
        """

        return self.log

    @property
    def get_verbose_log(self):
        """
        :return: extensive log (like verbose mode)
        """

        return self.verbose_log

    @staticmethod
    def start_thread(new_thread):
        """
        :param new_thread: thread to be started
        :return: starts given thread
        """

        new_thread.setDaemon(True)
        new_thread.start()

    def stop_thread(self, old_thread):
        """
        :param old_thread: thread to be stopped
        :return: stop given thread
        """
        
        old_thread.log = "DONE"  # stop thread
        old_thread._stop.set()
        thread_index = self.threads.index(old_thread)  # remove it form list of threads
        del self.threads[thread_index]
        if len(self.threads) < 1:  # check if last, then exit
            self.exit()

    def create_thread(self):
        """
        :return: create new thread
        """

        new_thread = SpiderThread(self,
            self.queue,
            self.pool,
            self.recall,
            self.timeout,
            self.max_pages,
            self.domains,
            'Thread-' + str(len(self.threads))
        )

        self.verbose_log += '\n' + self.name + ' creating ' + new_thread.name
        self.threads.append(new_thread)

    def run(self):
        """
        :return: run crawler! run!
        """

        self.start_time = calendar.timegm(time.gmtime())
        self.log = "WORKING"  # update log, queue, pool and create threads
        self.stats += '\nJob has started at ' + time.strftime('%c')
        self.queue.put(self.next_crawl)
        for new_thread in range(0, self.max_threads):  # create threads
            self.create_thread()

        for new_thread in self.threads:  # start threads
            self.start_thread(new_thread)
        
        while self.can_update:  # update
            self.update()
            time.sleep(Spider.UPDATE_INTERVAL)

        self.queue.join()

    def update(self):
        """
        :return: update current logs
        """

        # log, extensive log, stats
        self.running_time = calendar.timegm(time.gmtime()) - self.start_time
        if self.pages_crawled == 0:
            self.avg_time_crawling = 0
        else:
            self.avg_time_crawling = self.running_time / float(self.pages_crawled)

        self.ETA = float(self.max_pages) * float(self.avg_time_crawling)
        self.show_verbose()  # verbose log

    def show_verbose(self):
        """
        :return: show detailed info about threads
        """

        os.system('setterm -cursor off')  # hide cursor in terminal
        shell_width = shell.size()[1]  # get shell size
        column0_width = int(shell_width * float(0.4))  # page stats
        column1_width = int(shell_width * float(0.6))
        print('-------PAGES-------'.center(column0_width, '-'))
        print('crawled pages:'.ljust(column0_width) + '{:.{}}'.format(str(self.pages_crawled), column1_width))
        print('queued'.ljust(column0_width) + '{:.{}}'.format(str(self.pages_in_queue), column1_width))
        print('last'.ljust(column0_width) + shell.get_formatted(self.last_crawled, column1_width))
        print('current'.ljust(column0_width) + shell.get_formatted(self.current_crawling, column1_width))
        print('next crawl'.ljust(column0_width) + shell.get_formatted(self.next_crawl, column1_width))
        print('running since (s)'.ljust(column0_width) + '{:.{}}'.format(str(self.running_time), column1_width))
        print('avg time/crawl(s)'.ljust(column0_width) + '{:.{}}'.format(str(self.avg_time_crawling), column1_width))
        print('eta (s)'.ljust(column0_width) + '{:.{}}'.format(str(self.ETA), column1_width))
        lines_printed = 9

        name = []
        status = []
        url = []
        for thread in self.threads:
            name.append(thread.name)
            status.append(thread.log)
            url.append(thread.url)

        column2_width = int(shell_width * float(0.15))
        column3_width = int(shell_width * float(0.15))
        column4_width = int(shell_width * float(0.55))
        print('-------THREADS-------'.center(column0_width, '-'))
        print('NAME'.ljust(column2_width) + 'STATUS'.ljust(column3_width) + 'URL'.ljust(column4_width))
        lines_printed += 2
        for index in range(min(len(name), len(status), len(url))):
            print(name[index].ljust(column2_width) + status[index].ljust(column3_width) + shell.get_formatted(url[index], column4_width))
            lines_printed += 1

        # cursor up -> next time overwrite
        for line_up in range(lines_printed):
            sys.stdout.write('\033[F')

    def exit(self):
        """
        :return: exit main method
        """

        os.system('cls' if os.name == 'nt' else 'clear')  # clear window and restore cursor
        os.system('setterm -cursor on')

        self.can_update = False  # job done -> exit
        self.log = "DONE"
        self.verbose_log += '\n' + self.name + ' has finished crawling!'
        self.stats += '\nJob has finished at ' + time.strftime('%c') + '.'
        os._exit(0)
