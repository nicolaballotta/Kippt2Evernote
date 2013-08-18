Kippt2Evernote
==============

A simple Python script to migrate Kippt bookmarks to Evernote.

Overview
========

I started using [Kippt](https://kippt.com/) about one year ago and I've to admit that it's very powerful and well designed. However in the last months I falled in love with Evernote, so I decided to migrate all my Kippt bookmarks into one Evernote notebook; I took the opportunity of doing this in Python, cause I'm learning it.

Setup and usage
===============
1. Install [BeautifulSoup 4](http://www.crummy.com/software/BeautifulSoup/) using pip:

    ```bash
    $ sudo pip install beautifulsoup4
    ```
2. Go [here](https://www.evernote.com/api/DeveloperToken.action) and get a developer token.
3. Edit ```kippt2evernote.py``` and set these values:

    ```python
    # Set Kippt html export file
    kippt_file = ""

    # Set the auth token for Evenrote
    auth_token = ""

    # Set the notebook where to import bookmarks
    import_notebook = ""
    ```
4. Run Kippt2Evernote.

    ```bash
    $ python kippt2evernote.py
    ```

Notes
=====

As I said, I've just started learning Python, so feel free to contribute, fork and open issues!




