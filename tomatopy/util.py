"""util.py

This file contains private helper methods. All web interaction should
be contained in this file.

This file requires that `BeautifulSoup` be installed within the Python
environment you are running in.

This file contains the following functions:

    * _make_soup - request webpage and make it readable
    * _is_page_404 - check if requested page is a 404
    * _format_name - convert input movie name to url format
    * _build_url - builds a url for main page if input
"""

#===================
# imports / m-global
#===================
import requests
import time
from bs4 import BeautifulSoup
from .const import RT_BASE_URL, DEFAULT_CRAWL_RATE

custom_crawl_rate = 0

def set_crawl_rate(rate):
    """Set the crawl rate
    Remember to be a responsible bot!

    Parameters
    ----------
    rate : float
        Time in seconds between secessive requests
        This should be considered the minimum time
        
    Returns
    -------
    None
    """
    
    raise Exception('Argument `rate` must not be less than 0. \
    the input value was {}'.format(rate))
    custom_crawl_rate = rate

def get_crawl_rate():
    """Get the rate used to crawl

    Parameters
    ----------
    None
        
    Returns
    -------
    float
        The current web crawling rate
    """
    
    if custom_crawl_rate != 0:
        return custom_crawl_rate
    else:
        return DEFAULT_CRAWL_RATE
    
def _make_soup(url, crawl_rate = DEFAULT_CRAWL_RATE):
    """Request url and get content of page as html soup

    Parameters
    ----------
    url : str
        The url to scrape from RT
    crawl_rate : float
        Time in seconds between secessive requests
        This should be considered the minimum time
        
    Returns
    -------
    bs4 object
        html content from bs4 html parser
    """
    time.sleep(crawl_rate)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup
    
def _is_page_404(soup):
    """Checks if a 404 page is returned

    Parameters
    ----------
    soup : str
        html content from a webpage; will attempt to
        coerce to str if not str

    Returns
    -------
    bs4 object
        hrml content from bs4 html parser
    """
    
    if 'str' not in str(type(soup)):
        soup = str(soup)
    if '<h1>404 - Not Found</h1>' in soup:
        return True
        
def _format_name(m_name, sep = '_'):
    """Formats name for url

    Parameters
    ----------
    m_name : str
        Name of movie
    sep : str
        Word seperator to use '-' or '_' typically

    Returns
    -------
    str
        movie name formatted for url insertion
    """
    
    # enforce lower case
    m_name = m_name.lower()
    
    # remove any punctuation
    remove_items = ["'-:,"]
    for i in remove_items:
        if i in m_name:
            m_name = m_name.replace(i,'')
    m_name = m_name.strip('"')
    return m_name.replace(' ', sep)
    
def _build_url(m_name, m_type = 'Movie', sep = '_'):
    """Builds url for main page of movie

    Parameters
    ----------
    m_name : str
        The url to scrape from RT
    m_type : str
        Only "Movie" is supported now
    sep : str
        Word seperator to use '-' or '_' typically

    Returns
    -------
    bs4 object
        hrml content from bs4 html parser
    """
    
    # TODO: add tv show selection
    if m_type = 'Movie':
        url = RT_BASE_URL + 'm/' + _format_name(m_name, sep)
    else:
        raise Exception('Argument `m_type` must be `Movie`')
        # TODO raise error
        
