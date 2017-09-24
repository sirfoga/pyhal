# HAL: Handy Algorithmic Library

[![Build Status](https://travis-ci.org/sirfoga/pyhal.svg?branch=master)](https://travis-ci.org/sirfoga/pyhal) [![Build status](https://ci.appveyor.com/api/projects/status/isfmmdaqhkbgqaeu?svg=true)](https://ci.appveyor.com/project/sirfoga/pyhal) [![Coverage Status](https://coveralls.io/repos/github/sirfoga/pyhal/badge.svg?branch=master)](https://coveralls.io/github/sirfoga/pyhal?branch=master)

[![Code Health](https://landscape.io/github/sirfoga/pyhal/master/landscape.svg?style=flat)](https://landscape.io/github/sirfoga/hal/master) [![Code Climate](https://lima.codeclimate.com/github/sirfoga/pyhal/badges/gpa.svg)](https://codeclimate.com/github/sirfoga/pyhal) ![pylint Score](https://mperlet.de/pybadge/badges/8.83.svg)

[![PyPI version](https://badge.fury.io/py/PyHal.svg)](https://pypi.org/project/PyHal/) [![Requirements Status](https://requires.io/github/sirfoga/pyhal/requirements.svg?branch=master)](https://requires.io/github/sirfoga/pyhal/requirements/?branch=master) [![Documentation Status](https://readthedocs.org/projects/pyhal/badge/?version=latest)](http://pyhal.readthedocs.io/en/latest/?badge=latest)

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fsirfoga%2Fpyhal.svg?type=shield)](https://app.fossa.io/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fsirfoga%2Fpyhal?ref=badge_shield) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/licenses/Apache-2.0)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/sirfoga/pyhal/issues)


*A multipurpose library to perform great stuff in the most easy, fast and pythonic way.*

![screenshot](logo.png)

**Table of Contents**

- [The problem](#the-problem)
- [An example](#an-example)
- [The solution](#the-solution)
- [Install](#install)
- [Requirements](#requirements)
- [Python dependencies](#python-dependencies)
- [Examples](#examples)
- [Usage and documentation](#usage-and-documentation)
- [Questions and issues](#questions-and-issues)
- [LICENSE](#license)

## The problem
Say you want to edit the tags of all the songs in a folder. Say you wish to 
plot 2D/3D or even 4D points. Say you'd like to know the RSS feed of a 
YouTube channel.

If you want to do this stuff in a fast and easy way, this library is for ya.

## An example

- Edit songs tags
    #### Classic way
    ```python
    import os
    from mutagen.mp3 import MP3
    
    my_folder = "path to folder containing songs"
    
    for root, dirs, files in os.walk(my_folder):
        for file in files:
            audio = MP3(file)
            audio["artist"] = "An example"
            audio.save()
    ```
    #### Using `pyhal`
    ```python
    from hal.files.models import FileSystem, MP3Song
    
    my_folder = "path to folder containing songs"
    
    for file in FileSystem.ls_recurse(my_folder):
        MP3Song(file).set_artist("An example")
    ```
- Plot data
    #### Classic way
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    
    x = np.arange(1., 100.)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()
    ```
    #### Using `pyhal`
    ```python
    import numpy as np
    from hal.charts.plotter import Plot2d
    
    Plot2d.plot(np.sin, 1, 100, 100)
    ```
- Get YouTube RSS feed of channel
    #### Classic way
    
    No easy way that I know of

    #### Using `pyhal`
    ```python
    from hal.internet.youtube import get_channel_feed_url_from_video
    
    video_url = "my awesome video of an awesome channel"
    channel_feed = get_channel_feed_url_from_video(video_url)
    ```

<!-- ## The solution -->

## Install
- ``` $ pip3 install . --upgrade --force-reinstall ``` from the source
- ``` $ pip3 install pyhal``` via [pip](https://pypi.org/project/PyHal/)

## Requirements
- ```python 3.4``` or greater

### Python dependencies
Take a look [here](https://github.com/sirfoga/pyhal/blob/master/setup.py#L58) for the complete and updated list
- bs4
- colorama
- Crypto
- lxml
- matplotlib
- mutagen
- numpy
- psutil
- pycrypto
- pymongo
- requests
- scipy
- send2trash
- sklearn
- statsmodels

## Examples
You can take a look at [my other repository](https://github.com/sirfoga/pymisc/tree/master/misc): there are lots of implementations from various HAL modules.
Browse extra examples here:
- [`charts`](docs/examples/CHARTS.md) module
- [`tests`](docs/examples/TESTS.md) module


## Usage and documentation
- you can browse the [html](docs/doxygen/html/index.html) (or if you prefer the [epydoc docs](docs/epydoc/html/index.html))
- there is also the [pdf](docs/doxygen/pdf/api.pdf) version (for the epydoc pdfs go [here](docs/epydoc/pdf)
- download the repository and open the [sphinx](docs/sphinx/_build/html/index.html) documentation
- read online at the official [readthedocs](http://pyhal.readthedocs.io) web-page


## Questions and issues
The [github issue tracker](https://github.com/sirfoga/pyhal/issues) is **only** for bug reports and feature requests. Anything else, such as questions for help in using the library, should be mailed [here](mailto:sirfoga@protonmail.com).


## LICENSE
[Apache License](http://www.apache.org/licenses/LICENSE-2.0) Version 2.0, January 2004


