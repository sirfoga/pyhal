# !/usr/bin/python3
# coding: utf-8

""" Async-fetch urls """

import asyncio

import aiohttp
from aiosocks.connector import ProxyConnector, ProxyClientRequest


async def fetch(url, on_response, on_exception):
    """
    :param url: str
        Url of page to fetch
    :param on_response: function
        Function to execute when successfully fetched page body
    :param on_exception: function
        Function to execute when any exception is raised
    :return: void
        Fetches url
    """

    try:
        conn = ProxyConnector(remote_resolve=True)
        async with aiohttp.ClientSession(
                connector=conn,
                request_class=ProxyClientRequest
        ) as session:
            async with session.get(url) as response:
                body = await response.text()
                on_response(url, body, response.status)
                return body
    except Exception as exception:
        on_exception(url, exception)
        return ""


async def bound_fetch(sem, url, on_response, on_exception):
    """
    :param sem: Semaphore
        Asynchronous driver
    :param url: str
        Url of page to fetch
    :param on_response: function
        Function to execute when successfully fetched page body
    :param on_exception: function
        Function to execute when any exception is raised
    :return: void
        Asynchronously fetches url
    """

    async with sem:
        await fetch(url, on_response, on_exception)


async def fetch_urls(list_of_urls, on_response, on_exception,
                     max_concurrent=100):
    """
    :param list_of_urls: [] of str
        List of urls to fetch
    :param on_response: function
        Function to execute when successfully fetched page body
    :param on_exception: function
        Function to execute when any exception is raised
    :param max_concurrent: int
        Max number of concurrent connections
    :return: void
        Fetches url
    """

    tasks = []
    sem = asyncio.Semaphore(max_concurrent)
    for url in list_of_urls:
        task = asyncio.ensure_future(
            bound_fetch(sem, url, on_response, on_exception)
        )
        tasks.append(task)

    responses = asyncio.gather(*tasks)
    await responses
