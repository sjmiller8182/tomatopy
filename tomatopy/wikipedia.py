"""util.py

This file handles interations with wikipedia

This file requires that `BeautifulSoup` be installed within the Python
environment you are running in.

This file contains the following functions:

    * Builds url for wikipedia 'year in film'
    * scrape_movie_names - scrape movie names from wikipedia'
"""
# base
import time
import datetime
import re
from typing import List

# requirements
import requests
from bs4 import BeautifulSoup

# this package
from .util import _make_soup

DEFAULT_CRAWL_RATE = 1
movie_patt = re.compile(r'<i><a href=\"/wiki/[\w\(\)\%.\,\_\:\;\"]+\stitle=\"[\w\s\(\)\%.\,\_\:\;\'\"\-]+\"')
      
def _build_wiki_url(year: str) -> str:
    """Builds url for wikipedia 'year in film'

    Parameters
    ----------
    year : int
        year to scrape movie titles from

    Returns
    -------
    str
        formatted url
    """
    
    current_year = datetime.datetime.now().year
    base_url = 'https://en.wikipedia.org/wiki/'
    
    if year >= 1960 and year <= current_year:
        url = base_url + str(year) + '_in_film'
    else:
        raise Exception('Input year must be later than 1960 and not later than the current year (' + str(current_year) + ')')
    return url
    
def scrape_movie_names(year: int) -> List[str]:
    """scrape movie names from wikipedia'

    Parameters
    ----------
    year : int
        year to scrape movie titles from

    Returns
    -------
    list
        list of movie titles
    """
    
    url = _build_wiki_url(year)
    print('Scraping from ' + url)
    soup = _make_soup(url)

    s_html = str(soup)

    matches = list()
    matches += re.findall(movie_patt, s_html)
    for m in range(len(matches)):
        matches[m] = matches[m].split('title=')[1].replace('"','')
        matches[m] = re.sub(r'\s\((\d+\s)?([\w\s]+)?film\)','',matches[m])
        matches[m] = re.sub(r'Category\:\d+','',matches[m])
    matches.remove('')

    if len(matches) == 0:
        print('-> Scraping failed.')
    else:
        print('-> Scraping done.')
        
    return matches