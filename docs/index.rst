.. PyHal documentation master file, created by
   sphinx-quickstart on Mon Oct  8 20:57:10 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Hal: Your swiss knife to perform fast and easy pythonic stuff
=============================================================

Release v\ |version|


.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT

.. image:: https://badge.fury.io/py/PyHal.svg
   :target: https://pypi.org/project/PyHal/

.. image:: https://img.shields.io/badge/Python-3.6-blue.svg
   :target: https://www.python.org/download/releases/3

.. image:: https://codecov.io/github/sirfoga/pyhal/coverage.svg?branch=master
   :target: https://codecov.io/github/sirfoga/pyhal

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
   :target: https://saythanks.io/to/sirfoga

-------------------


Table of contents
-----------------

* `Introduction`_
* `Installation`_
* `Contribute`_
* `Authors`_
* `Thanks`_
* `License`_

API reference
-------------

* `Hal`_
* `Alphabetical list`_


Behold, the power of Hal
------------------------

Edit songs tags
~~~~~~~~~~~~~~~

Classic way
^^^^^^^^^^^

.. code:: python

    >>> import os
    >>> from mutagen.mp3 import MP3
    >>> my_folder = "path to folder containing songs"
    >>> for root, dirs, files in os.walk(my_folder):
    >>>     for file in files:
    >>>         audio = MP3(file)
    >>>         audio["artist"] = "An example"
    >>>         audio.save()

Using ``Hal``
^^^^^^^^^^^^^^^

.. code:: python

    >>> from hal.files.models.system import ls_recurse
    >>> from hal.files.models.audio import MP3Song
    >>> my_folder = "path to folder containing songs"
    >>> for file in ls_recurse(my_folder):
    >>>     MP3Song(file).set_artist("An example")

Plot data
~~~~~~~~~

.. _classic-way-1:

Classic way
^^^^^^^^^^^

.. code:: python

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> x = np.arange(1., 100.)
    >>> y = np.sin(x)
    >>> plt.plot(x, y)
    >>> plt.show()

.. _using-pyhal-1:

Using ``Hal``
^^^^^^^^^^^^^^^

.. code:: python

    >>> import numpy as np
    >>> from hal.charts.plotter import Plot2d
    >>> Plot2d().plot(np.sin, 1, 100, 100)

Get YouTube RSS feed of channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _classic-way-2:

Classic way
^^^^^^^^^^^

No easy way that I know of

.. _using-pyhal-2:

Using ``Hal``
^^^^^^^^^^^^^^^

.. code:: python

    >>> from hal.internet.services.youtube import YoutubeChannel
    >>> video_url = "my awesome video of an awesome channel"
    >>> channel_feed = YoutubeChannel.get_feed_url_from_video(video_url)
    >>> # or if you know the name
    >>> channel_name = "my awesome channel"
    >>> channel_feed = YoutubeChannel(channel_name).get_feed_url()

Generate module tests code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _classic-way-3:

Classic way
^^^^^^^^^^^

No easy way that I know of

.. _using-pyhal-3:

Using ``Hal``
^^^^^^^^^^^^^^^

.. code:: python

    >>> from hal.tests.gen import TestWriter
    >>> src = "path to module source folder"
    >>> out = "path to output folder"
    >>> w = TestWriter(src)
    >>> w.write_tests(out)


Install
-------

Different ways, all equals

via ``pipenv``
~~~~~~~~~~~~~~

-  ``$ pipenv install .``
-  ``$ make install``

via ``pip``
~~~~~~~~~~~

-  ``$ pip3 install PyHal``
-  ``$ make pip-install``

fast install
~~~~~~~~~~~~

-  ``make fast-init`` *just copies source files to distribution files
   … run it only if you’re sure about dependencies*

.. _pip: https://pypi.org/project/PyHal/


Contributing and feedback
-------------------------

0. `open an issue`_
1. `fork`_ this repository
2. create your feature branch (``git checkout -b my-new-feature``)
3. commit your changes (``git commit -am 'Added my new feature'``)
4. publish the branch (``git push origin my-new-feature``)
5. `open a PR`_

Suggestions and improvements are `welcome`_!

Authors
-------

+----------------------+
| |sirfoga|            |
+======================+
| `Stefano Fogarollo`_ |
+----------------------+

Thanks to
---------

-  `Kenneth Reitz`_

License
-------
.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://opensource.org/licenses/MIT

GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007

Copyright (c) Stefano Fogarollo

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the "Software"), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
    the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
    FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


.. _open an issue: https://github.com/sirfoga/pyhal/issues/new
.. _fork: https://github.com/sirfoga/pyhal/fork
.. _open a PR: https://github.com/sirfoga/pyhal/compare
.. _welcome: https://github.com/sirfoga/pyhal/issues
.. _Stefano Fogarollo: https://sirfoga.github.io
.. _Kenneth Reitz: https://github.com/kennethreitz

.. |sirfoga| image:: https://avatars0.githubusercontent.com/u/14162628?s=128&v=4
   :target: https://github.com/sirfoga

.. _Introduction: #behold-the-power-of-hal
.. _Installation: #install
.. _Contribute: #contributing-and-feedback
.. _Authors: #authors
.. _Thanks: #thanks-to
.. _License: #license
.. _Hal: source/hal.html
.. _Alphabetical list: genindex.html