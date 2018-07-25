# !/usr/bin/python3
# coding: utf-8


""" Get rss feed for youtube channel. """

from bs4 import BeautifulSoup

from hal.internet.web import Webpage

YOUTUBE_USER_BASE_URL = "https://www.youtube.com/user/"
YOUTUBE_FEED_BASE_URL = "https://www.youtube.com/feeds/videos.xml?channel_id="


def get_channel_page_from_name(channel_name):
    """
    :param channel_name: string
        name of channel (e.g in  https://www.youtube.com/user/caseyneistat"
        you should take "caseyneistat")
    :return string
        source page of youtube channel.
    """

    channel_url = YOUTUBE_USER_BASE_URL + channel_name  # url of channel
    source_page = Webpage(
        channel_url).get_html_source()  # get source page of channel homepage
    return source_page


def get_channel_id_from_name(channel_name):
    """
    :param channel_name: string name of channel (e.g in
        "https://www.youtube.com/user/caseyneistat" you should take
        "caseyneistat")
    :return string
        id of youtube channel
    """

    soup = BeautifulSoup(get_channel_page_from_name(channel_name),
                         "lxml")  # parser for source page
    channel_id = soup.find_all(
        "span",
        {
            "class": "channel-header-subscription-button-container"
        }
    )  # get all good spans
    channel_id = channel_id[0].find_all("button")[
        0]  # get button in first span
    channel_id = channel_id["data-channel-external-id"]  # get id
    return channel_id


def get_channel_feed_url_from_id(channel_id):
    """
    :param channel_id: string
        id of channel (e.g in
        "https://www.youtube.com/channel/UC2zjki3bJIaXmgV_LBQ2jTg" you should
        take "UC2zjki3bJIaXmgV_LBQ2jTg")
    :return string
        rss url feed of youtube channel
    """

    return YOUTUBE_FEED_BASE_URL + channel_id


def get_channel_feed_url_from_name(channel_name):
    """
    :param channel_name: string
        name of channel (e.g in "https://www.youtube.com/user/caseyneistat"
        you should take "caseyneistat")
    :return string
        rss url feed of youtube channel
    """

    channel_id = get_channel_id_from_name(channel_name)  # get channel id
    return get_channel_feed_url_from_id(channel_id)


def get_channel_feed_url_from_video(video_url):
    """
    :param video_url: string
        Url of video (e.g in https://www.youtube.com/watch?v=KB_iTbDrkxE)
    :return string
        rss url feed of youtube channel.
    """

    web_page = Webpage(video_url)
    web_page.get_html_source()
    channel_id = web_page.soup.find_all("div", {"class": "yt-user-info"})[0].a[
        "href"]
    channel_id = str(channel_id).strip().replace("/channel/",
                                                 "")  # get channel id
    return get_channel_feed_url_from_id(channel_id)
