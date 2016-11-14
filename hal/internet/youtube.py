# !/usr/bin/python
# coding: utf_8

# Copyright 2016 stefano fogarollo
#
# licensed under the apache license, version 2.0 (the "license");
# you may not use this file except in compliance with the license.
# you may obtain a copy of the license at
#
# http://www.apache.org/licenses/license-2.0
#
# unless required by applicable law or agreed to in writing, software
# distributed under the license is distributed on an "as is" basis,
# without warranties or conditions of any kind, either express or implied.
# see the license for the specific language governing permissions and
# limitations under the license.


""" Get rss feed for youtube channel. """


from hal.internet.web import Webpage
from bs4 import BeautifulSoup


def get_channel_page(channel_name, youtube_channel_url="https://www.youtube.com/user/"):
    """
    @param channel_name: string
        name of channel.
    @param youtube_channel_url: string
        base url of youtube channels.
    @return string
        source page of youtube channel.
    """

    channel_url = youtube_channel_url + channel_name  # url of channel
    source_page = Webpage(channel_url).get_html_source()  # get source page of channel homepage
    return source_page


def get_channel_id(channel_name, channel_id_field="data-channel-external-id"):
    """
    @param channel_name: string
        channel_name name of channel.
    @param channel_id_field: string
        default field to get channel id.
    @return string
        id of youtube channel.
    """

    soup = BeautifulSoup(get_channel_page(channel_name), "lxml")  # parser for source page
    channel_id = soup.find_all("span", {"class": "channel-header-subscription-button-container"})  # get all good spans
    channel_id = channel_id[0].find_all("button")[0]  # get button in first span
    channel_id = channel_id[channel_id_field]  # get id
    return channel_id


def get_channel_feed_url(channel_name, base_feed_url="https://www.youtube.com/feeds/videos.xml?channel_id="):
    """
    @param channel_name: string
        channel_name name of channel.
    @param base_feed_url: string
        default base url for rss feed of youtube channels.
    @return string
        rss url feed of youtube channel.
    """

    channel_id = get_channel_id(channel_name)  # get channel id
    return base_feed_url + channel_id
