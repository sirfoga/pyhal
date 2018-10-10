.. PyHal documentation master file, created by
   sphinx-quickstart on Mon Oct  8 20:57:10 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Hal: Your swiss knife to perform fast and easy pythonic stuff
=================================

Release v\ |version| (:ref:`Installation <install>`)

.. image:: https://img.shields.io/pypi/l/requests.svg
    :target: https://pypi.org/project/requests/

.. image:: https://img.shields.io/pypi/wheel/requests.svg
    :target: https://pypi.org/project/requests/

.. image:: https://img.shields.io/pypi/pyversions/requests.svg
    :target: https://pypi.org/project/requests/

.. image:: https://codecov.io/github/requests/requests/coverage.svg?branch=master
    :target: https://codecov.io/github/requests/requests
    :alt: codecov.io

.. image:: https://img.shields.io/badge/Say%20Thanks!-🦉-1EAEDB.svg
    :target: https://saythanks.io/to/kennethreitz


-------------------

**Behold, the power of Hal**::

    >>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    >>> r.status_code
    200
    >>> r.headers['content-type']
    'application/json; charset=utf8'
    >>> r.encoding
    'utf-8'
    >>> r.text
    u'{"type":"User"...'
    >>> r.json()
    {u'private_gists': 419, u'total_private_repos': 77, ...}

See `similar code, sans pyhal <https://gist.github.com/973705>`_.



Table of contents
--------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


The User Guide
--------------

This part of the documentation, which is mostly prose, begins with some
background information about Requests, then focuses on step-by-step
instructions for getting the most out of Requests.

.. toctree::
   :maxdepth: 2

   user/intro
   user/install
   user/quickstart
   user/advanced
   user/authentication


The Community Guide
-------------------

This part of the documentation, which is mostly prose, details the
Requests ecosystem and community.

.. toctree::
   :maxdepth: 2

   community/sponsors
   community/recommended
   community/faq
   community/out-there
   community/support
   community/vulnerabilities
   community/updates
   community/release-process

The API Documentation / Guide
-----------------------------

If you are looking for information on a specific function, class, or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api


The Contributor Guide
---------------------

If you want to contribute to the project, this part of the documentation is for
you.

.. toctree::
   :maxdepth: 3

   dev/contributing
   dev/philosophy
   dev/todo
   dev/authors

.. todo add thanks to section (mirror README.md)