# -*- coding: utf-8 -*-

"""Get rss feed for youtube channel"""

from bs4 import BeautifulSoup

from hal.internet.web import Webpage

# last dot to avoid pay/adv wall
YOUTUBE_USER_BASE_URL = "https://www.youtube.com/user/"
YOUTUBE_CHANNEL_BASE_URL = "https://www.youtube.com/c/"
YOUTUBE_FEED_BASE_URL = "https://www.youtube.com/feeds/videos.xml?channel_id="


class YoutubeChannel:
    """Youtube channel"""

    def __init__(self, url):
        self.url = url

    def get_channel_page(self):
        """Fetches source page

        :return: source page of youtube channel
        """
        source_page = Webpage(self.url).get_html_source()  # get source page of channel
        return source_page

    def get_channel_id(self):
        """Fetches id

        :return: id of youtube channel
        """
        soup = BeautifulSoup(
            self.get_channel_page(), "lxml"
        )  # parser for source page
        return soup.find_all('link', {'rel': 'canonical'})[0]['href'].split('/')[-1]

    def get_feed_url(self):
        """Fetches RSS url

        :return: rss url feed of youtube channel
        """
        channel_id = self.get_channel_id()  # get id
        return YoutubeChannel.get_feed_url_from_id(channel_id)

    @staticmethod
    def get_feed_url_from_id(channel_id):
        """Fetches feed url

        :param channel_id: id of channel
        :return: feed url
        """
        return YOUTUBE_FEED_BASE_URL + channel_id

    @staticmethod
    def get_feed_url_from_video(video_url):
        """Gets channel id and then creates feed url

        :param video_url: Url of video
        :return: feed url
        """
        web_page = Webpage(video_url)
        channel_id = YoutubeChannel(video_url).get_channel_id()
        return YoutubeChannel.get_feed_url_from_id(channel_id)

    @staticmethod
    def get_feed_url_from_channel(channel_name):
        url = YOUTUBE_CHANNEL_BASE_URL + channel_name 
        channel_id = YoutubeChannel(url).get_channel_id()
        return YoutubeChannel.get_feed_url_from_id(channel_id)
