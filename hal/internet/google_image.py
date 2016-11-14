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


import time
import urllib.request
import os
from hal.wrappers.methods import handle_exceptions
from hal.internet.web import Webpage


BASE_URL = "https://www.google.com/search?q="  # base url to search google images
TOKEN_URL = "&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg"


def get_next_image(s):
    """
    :param s:
    :return:
    """

    start_line = s.find("rg_di")
    if start_line == -1:  # If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find("\"class=\"rg_meta\"")
        start_content = s.find("\"ou\"",start_line+1)
        end_content = s.find(",\"ow\"",start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def get_images(page, max_items=10):
    """
    Getting all links with the help of "_images_get_next_image"
    :param page: string
        Source page
    :param max_items: int
        Max items to download
    :return: []
        List of images in page
    """

    items = []
    while len(items) < max_items:
        item, end_content = get_next_image(page)
        if item == "no_links":
            break
        else:
            items.append(item)  # append all the links in the list named "Links"
            page = page[end_content:]
    return items


@handle_exceptions
def save_image(url, local_file):
    """
    :param url: string
        Url to fetch image from
    :param local_file: string
        Path to local file to store image
    :return: void
        Download and save image in local_file
    """

    d = urllib.request.URLopener()
    d.retrieve(url, local_file)


@handle_exceptions
def search_and_save(search_keywords):
    """
    :param search_keywords: string
        Search keyword
    :return: void
        Download images matching given search keywords
    """

    url = BASE_URL + search_keywords.replace(" ", "%20") + TOKEN_URL
    raw_html = (Webpage(url).get_html_source())
    images = get_images(raw_html, max_items=100)
    save_folder = os.path.join(
        os.getcwd(),
        str(search_keywords)
            .replace(os.path.pathsep, "")  # remove path separators
            .replace(" ", "-")  # remove blanks
            .lower(),  # lowercase folder
        str(int(time.time())),  # seconds since 1970
    )

    if len(images) > 0:  # if there are images to download
        os.makedirs(save_folder)
        for image in images:
            save_file = str(image.__hash__())
            save_image(image, os.path.join(save_folder, save_file))
