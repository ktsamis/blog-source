#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# General site settings:
AUTHOR = 'Kostas Tsamis'
SITENAME = 'Notes-blog'
SITEURL = 'http://tsamis73.github.io'
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'
#DELETE_OUTPUT_DIRECTORY = True
DEFAULT_METADATA = {}
#OUTPUT_RETENTION = [output/.git]
SUMMARY_MAX_LENGTH = 50
CHECK_MODIFIED_METHOD = 'mtime'


# Path settings:
PATH = 'content'
OUTPUT_PATH = 'output/'
#PAGE_PATHS = ['content/pages']
# For the favicon.ico:

STATIC_PATHS = ['images', 'extras/favicon.ico']
EXTRA_PATH_METADATA = {
        'extras/favicon.ico': {'path': 'favicon.ico'}
        }





# URL settings:
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
#PAGE_URL = 'pages/{slug}/'
#PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'



# Template settings:
#TEMPLATE_PAGES = {'src/books.html': 'dest/books.html',
#                  'src/resume.html': 'dest/resume.html',
#                                    'src/contact.html': 'dest/contact.html'}


# Theme settings:
GITHUB_URL = "http://github.com/tsamis73"




# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
