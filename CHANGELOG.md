# Change Log
All notable changes to this project will be documented in this file.

### 4.7.4 - 2017-10-22

### Added
- email templates and utils

### Refactored
- move gmail module to email module

### 4.7.3 - 2017-10-22

### Added
- app cron lock, notifications utils, internet utils

### 4.7.2 - 2017-10-22

### Added
- datetime utils

### 4.7.1 - 2017-10-22

### Added
- google authenticator (gmail module)

### 4.7 - 2017-09-24

### Added
- examples of usage in readme

### Fixed
- static methods in Plot2d/Plot3d

### 4.6.4 - 2017-09-22

### Added
- mp3 set genre

### 4.6.3 - 2017-08-23

### Added
- language option in github api
- async utils
- download to file with headers and cookies options
- appveyor config

### Removed
- print_item_info() in time.profile

### 4.6.2

### Removed
- duplicate primes matrix in maths module
- duplicate code in maths prime checking
- duplicate code in ml time series
- low primality checking in maths.Integer

### Fixed
- matplotlib dependencies
- Plot4d.plot canvas updater
- maths is_probably_prime power int

### Added
- charts module examples
- tests module examples

### 4.6.1

### Added
- tests utils
- test suite on files
- sphinx docs script

### Fixed
- hal hidden ls
- code misspelling

### 4.6

### Added
- Pylint badge in README

### Fixed
- duplicate code in ml.utils.misc
- cleaned code (PEP8 compliant, score: 8.78/10)

### 4.5.1

### Added
- pretty printer for tables

### Fixed
- badges in README
- converted to sklearn.model_selection
- flake8-ed all modules
- pylint-ed all modules

### Refactored
- selenium -> selenium_bots to avoid misunderstandings in imports

### Removed
- epydoc text docs

### 4.5

### Added
- pymongo utils

### 4.4.9

### Added
- memory profiling and gc collector

### 4.4.8

### Added
- file utils save_dicts_to_csv, save_matrix_to_csv

### Changed
- time.utils eta time

### 4.4.7

### Added
- download_pdf_to_file

### 4.4.6

### Added
- get_time_eta

### 4.4.5

### Added
- add and remove_column_from_matrix
- get_average_length_of_word
- MONTHS_NAMES in time utils
- normalize option in create_multiple_bar_chart

### 4.4.4

### Added
- time utils

### Fixed
- extremely annoying bug on csv parser

### 4.4.3

### Added
- charts module
- charts.correlation
- charts.bar
- ml.utils normalize array

### 4.4.2

### Fixed
- ml csv parser discarding first column

### Refactored
- show correlation matrix

### 4.4.1

### Fixed
- ml.utils.matrix.get_subset_of_matrix transpose bug

### 4.4.0

### Added
- ml.utils.matrix
- ml.utils.misc

### 4.3.9

### Added
- github api models

### 4.3.8

### Added
- strings module
- strings.how_similar_are
- 4.3.8 docs

### Changed
- updated copyright to 2017

### 4.3.7

### Refactored
- internet.youtube feed fetcher

### Added
- youtube feed fetcher from id, video url

### 4.3.6

### Fixed
- ml.analysis.correlation minor bugs

### 4.3.5

### Added
- ml.analysis.correlation

### Fixed
- now ml.analysis.correlation analyzes only `csv` files
- ml.analysis.correlation: parsing data to float only after choosing headers
- CSVParser
- create_visual_correlation_matrix

### 4.3.4

### Fixed
- EightQueen performance tester

### 4.3.3

### Fixed
- now search engines can fetch pages using onion (tor) protocol

### 4.3.2

### Fixed
- hal.ml.utils: removed fixed title in correlation matrix

### Added
- method to get correlation matrix

### 4.3.1.4

### Fixed
- backward compatibility for Webpage.get_html_source()

### 4.3.1.3

### Fixed
- design but in webpage (would load webpage in class constructor)
- search engine updated to latest Webpage

### 4.3.1.2

### Added
- url validator with regex

### 4.3.1.1

### Fixed
- now Webpage does NOT use TOR as default internet connection 

### 4.3.1

### Added
- .pdf and .html docs generated with epydoc (I'm not enough brave to try sphinx)

### Changed
- Refactored changelog

### 4.3.0.1

### Changed
- Now path separator works also in windows
- Fixed more annoying bugs in files.models

### 4.3

### Removed
- Google search engine deprecated (too unreliable)

### Fixed
- Fixed annoying bugs in files.models

### 4.2

### Added
- Google image search engine.

### 4.1.1

### Changed
- YouTube RSS channel creator, moved engines.

### 4.1

### Changed
- Reformat code, removed lots of useless modules, improved performance.

### 3.3

### Added
- Search engine module (torrent at least ...)

### 3.0

### Changed
- Converted to Python 3.x (also imports and libraries)

### 2.0

### Changed
- Refactored python modules, ready to bring in machine learning one

### 1.0

### Added
- Installation tool, examples, and docs

### 0.2.1

### Fixed
- General bug fixes

### Added
- Folder.sync

### 0.2

### Changed
- Created new modules, classes and functions
- Got qt to work

### 0.1

### Fixed
- Fixed small bugs

### Added
- Previously created modules following PEP rules

### 0.0

### Added
- Quick release for new library project
- Language: Python 2.7
