# -*- coding: utf-8 -*-

"""Get rss feed for youtube channel"""

from bs4 import BeautifulSoup

from hal.internet.web import Webpage

YOUTUBE_USER_BASE_URL = "https://www.youtube.com/user/"
YOUTUBE_FEED_BASE_URL = "https://www.youtube.com/feeds/videos.xml?channel_id="


class YoutubeChannel:
    """Youtube channel"""

    def __init__(self, channel_name):
        self.channel_name = channel_name

    def get_channel_page(self):
        """Fetches source page

        :returns: source page of youtube channel
        """
        channel_url = YOUTUBE_USER_BASE_URL + self.channel_name  # url
        source_page = Webpage(
            channel_url).get_html_source()  # get source page of channel
        return source_page

    def get_channel_id(self):
        """Fetches id

        :returns: id of youtube channel
        """
        soup = BeautifulSoup(
            self.get_channel_page(), "lxml"
        )  # parser for source page
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

    def get_feed_url(self):
        """Fetches RSS url

        :returns: rss url feed of youtube channel
        """
        channel_id = self.get_channel_id()  # get id
        return YoutubeChannel.get_feed_url_from_id(channel_id)

    @staticmethod
    def get_feed_url_from_id(channel_id):
        """Fetches feed url

        :param channel_id: id of channel
        :returns: feed url
        """
        return YOUTUBE_FEED_BASE_URL + channel_id

    @staticmethod
    def get_feed_url_from_video(video_url):
        """Gets channel id and then creates feed url

        :param video_url: Url of video
        :returns: feed url
        """
        web_page = Webpage(video_url)
        web_page.get_html_source()
        channel_id = \
            web_page.soup.find_all("div", {"class": "yt-user-info"})[0].a[
                "href"]
        channel_id = str(channel_id).strip().replace("/channel/",
                                                     "")  # get channel id
        return YoutubeChannel.get_feed_url_from_id(channel_id)
