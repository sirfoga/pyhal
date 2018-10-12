<div align="center">
<h1>HAL | Handy Algorithmic Library</h1>
<em>Your swiss knife to perform fast and easy pythonic stuff</em></br></br>
</div>

<div align="center">
<a href="https://travis-ci.org/sirfoga/pyhal"><img alt="Build Status" src="https://travis-ci.org/sirfoga/pyhal.svg?branch=master"></a> <a href="https://codecov.io/github/rsirfoga/pyhal"><img alt="codecov.io" src="https://codecov.io/github/sirfoga/pyhal/coverage.svg?branch=master"></a> <a href="https://landscape.io/github/sirfoga/hal/master"><img alt="Code Health" src="https://landscape.io/github/sirfoga/pyhal/master/landscape.svg?style=flat"></a> 
</div>


<details>
  <summary>Table of Contents</summary>

* [The problem](#the-problem)
* [Examples](#examples)
* [Install](#install)
* [Usage and documentation](#usage-and-documentation)
* [Questions and issues](#questions-and-issues)
* [License](#license)

</details>


## The problem
Say you want to
- [edit the tags of all the songs in a folder](#using-pyhal)
- [plot 2D/3D or even 4D points](#using-pyhal-1)
- [fetch the RSS feed of a YouTube channel](#using-pyhal-2)

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
from hal.files.models.system import ls_recurse
from hal.files.models.audio import MP3Song

my_folder = "path to folder containing songs"

for file in ls_recurse(my_folder):
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

Plot2d().plot(np.sin, 1, 100, 100)
```

### Get YouTube RSS feed of channel
    
#### Classic way

No easy way that I know of

#### Using `pyhal`
```python
from hal.internet.services.youtube import YoutubeChannel

video_url = "my awesome video of an awesome channel"
channel_feed = YoutubeChannel.get_feed_url_from_video(video_url)

# or if you know the name
channel_name = "my awesome channel"
channel_feed = YoutubeChannel(channel_name).get_feed_url()
```


## Install
<a href="https://pypi.org/project/PyHal/"><img alt="PyPI version" src="https://badge.fury.io/py/PyHal.svg"></a> <a href="https://requires.io/github/sirfoga/pyhal/requirements/?branch=master"><img alt="Requirements Status" src="https://requires.io/github/sirfoga/pyhal/requirements.svg?branch=master"></a> <a href="https://snyk.io/test/github/sirfoga/pyhal?targetFile=requirements.txt"><img src="https://snyk.io/test/github/sirfoga/pyhal/badge.svg?targetFile=requirements.txt" alt="Known Vulnerabilities" data-canonical-src="https://snyk.io/test/github/sirfoga/pyhal?targetFile=requirements.txt" style="max-width:100%;"></a>

Different ways, all equals

### via `pipenv`
- ```$ pipenv install .```
- ```$ make install```

### via `pip`
- ```$ pip3 install PyHal``` via [pip](https://pypi.org/project/PyHal/)
- ```$ make pip-install```

### fast install
- ```make fast-init```
*just copies source files to distitribution files ... run it only if you're sure about dependencies*


## Usage and documentation
<a href="https://pyhal.readthedocs.io/en/latest/"><img src="https://readthedocs.org/projects/pyhal/badge/?version=latest"></a>

Browse the online documentation
- on my [personal page]([readthedocs](https://sirfoga.github.io/pyhal/))
- on [readthedocs.org](https://pyhal.readthedocs.io/en/latest/)
or make your own by `make docs`


## Contributing and feedback
<a href="https://github.com/sirfoga/pyhal/issues"><img alt="Contributions welcome" src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://opensource.org/licenses/MIT"><img alt="Open Source Love" src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103"></a>

0. [open an issue](https://github.com/sirfoga/pyhal/issues/new)
0. [fork](https://github.com/sirfoga/pyhal/fork) this repository
0. create your feature branch (`git checkout -b my-new-feature`)
0. commit your changes (`git commit -am 'Added my new feature'`)
0. publish the branch (`git push origin my-new-feature`)
0. [open a PR](https://github.com/sirfoga/pyhal/compare)

Suggestions and improvements are [welcome](https://github.com/sirfoga/pyhal/issues)!


## Authors
<a href="https://codeclimate.com/github/sirfoga/pyhal"><img alt="Code Climate" src="https://lima.codeclimate.com/github/sirfoga/pyhal/badges/gpa.svg"></a>
<a href="https://bettercodehub.com/"><img alt="BCH compliance" src="https://bettercodehub.com/edge/badge/sirfoga/pyhal?branch=master"></a>
<a href="https://travis-ci.org/sirfoga/pyhal"><img alt="pylint score" src="https://mperlet.github.io/pybadge/badges/9.65.svg"></a>

| [![sirfoga](https://avatars0.githubusercontent.com/u/14162628?s=128&v=4)](https://github.com/sirfoga "Follow @sirfoga on Github") |
|---|
| [Stefano Fogarollo](https://sirfoga.github.io) |


## Thanks to
- [Kenneth Reitz](https://github.com/kennethreitz)


## License
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
