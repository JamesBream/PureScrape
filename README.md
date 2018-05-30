# PureScrape

### What is this?

PureScrape is a personal project designed for my own use in keeping track of how many people visit my local gym at any given time.

Written in Python, PureScrape is designed to scrape the PureGym.com member dashboard at a predefined interval in order to return the reported number of visitors at a member's home gym. This information is then collated allowing a better idea of when the gym is busy - mostly a project borne out of curiosity and a love of gathering data.

I'm documenting my progress in tutorial posts on my blog at https:jbream.me - though they might not be available as of yet.


### Roadmap

Currently, PureScrape is able to achieve a persistent login and scrapes data at intervals. This data is to be stored in an SQLite database.

Beyond this, it is my intention to give PureScrape some graphing capability so that it might make some sense of the dataset it acquires. The graphs will be made available via a web interface.


### How to Use This?

This project is built using **Python 3.5+** and almost certainly won't work on Python 2.

The project uses *PipEnv* to manage dependencies and to avoid you having to manage a virtualenv. Install PipEnv, clone this repo and then run `pipenv install` to create a virtualenv and install all dependencies.

`pipenv shell` will launch the virtualenv and you can then run PureScrape with `python purescrape.py`.
