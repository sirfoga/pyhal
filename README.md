<div align="center">
<h1>HAL | Handy Algorithmic Library</h1>
<em>A multipurpose library homemade from scratch to perform great stuff in a pythonic way</em></br></br>
</div>

<div align="center">
<a href="https://travis-ci.org/sirfoga/pyhal"><img alt="Build Status" src="https://travis-ci.org/sirfoga/pyhal.svg?branch=master"></a> <a href="https://coveralls.io/github/sirfoga/pyhal?branch=master"><img alt="Coverage Status" src="https://coveralls.io/repos/github/sirfoga/pyhal/badge.svg?branch=master"></a>
</div>

<div align="center">
<a href="https://landscape.io/github/sirfoga/hal/master"><img alt="Code Health" src="https://landscape.io/github/sirfoga/pyhal/master/landscape.svg?style=flat"></a> <a href="https://bettercodehub.com/"><img alt="BCH compliance" src="https://bettercodehub.com/edge/badge/sirfoga/pyhal?branch=master"></a> <a href="https://codeclimate.com/github/sirfoga/pyhal"><img alt="Code Climate" src="https://lima.codeclimate.com/github/sirfoga/pyhal/badges/gpa.svg"></a> <img alt="pylint Score" src="https://mperlet.de/pybadge/badges/8.83.svg">
</div>

<div align="center">
<a href="https://pypi.org/project/PyHal/"><img alt="PyPI version" src="https://badge.fury.io/py/PyHal.svg"></a> <a href="https://requires.io/github/sirfoga/pyhal/requirements/?branch=master"><img alt="Requirements Status" src="https://requires.io/github/sirfoga/pyhal/requirements.svg?branch=master"></a>
</div>

<div align="center">
<a href="https://app.fossa.io/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fsirfoga%2Fpyhal?ref=badge_shield"><img alt="FOSSA Status" src="https://app.fossa.io/api/projects/git%2Bhttps%3A%2F%2Fgithub.com%2Fsirfoga%2Fpyhal.svg?type=shield"></a> <a href="http://unlicense.org/"><img src="https://img.shields.io/badge/license-Unlicense-blue.svg"></a> <a href="http://unlicense.org/"><img alt="Open Source Love" src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103"></a> <a href="https://github.com/sirfoga/pyhal/issues"><img alt="Contributions welcome" src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
</div>

</br>


## Table of Contents

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


## Examples

### Edit songs tags
    
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

### Plot data
    
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

### Get YouTube RSS feed of channel
    
#### Classic way

No easy way that I know of

#### Using `pyhal`
```python
from hal.internet.youtube import get_channel_feed_url_from_video

video_url = "my awesome video of an awesome channel"
channel_feed = get_channel_feed_url_from_video(video_url)
```


## The solution
One-line, fast and extensible python commands to deal with most of every-day
 situation.


## Install
- ``` $ pip3 install . --upgrade --force-reinstall ``` from the source
- ``` $ pip3 install pyhal``` via [pip](https://pypi.org/project/PyHal/)


## Examples
You can take a look at [my other repository](https://github.com/sirfoga/pymisc/tree/master/misc): there are lots of implementations from various HAL modules.
Browse extra examples here:
- [`charts`](docs/examples/CHARTS.md) module
- [`tests`](docs/examples/TESTS.md) module


## Usage and documentation
- you can browse the [html](docs/doxygen/html/index.html)


## Contributing
[Fork](https://github.com/sirfoga/pyhal/fork) | Patch | Push | [Pull request](https://github.com/sirfoga/pyhal/pulls)


## Feedback
Suggestions and improvements [welcome](https://github.com/sirfoga/pyhal/issues)!


## Authors
| [![sirfoga](https://avatars0.githubusercontent.com/u/14162628?s=128&v=4)](https://github.com/sirfoga "Follow @sirfoga on Github") |
|---|
| [Stefano Fogarollo](https://sirfoga.github.io) |


## License
[Unlicense](https://unlicense.org/)
