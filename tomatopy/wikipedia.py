import time
import datetime
import re
import requests
from bs4 import BeautifulSoup

DEFAULT_CRAWL_RATE = 1
movie_patt = re.compile(r'<i><a href=\"/wiki/[\w\(\)\%.\,\_\:\;\"]+\stitle=\"[\w\s\(\)\%.\,\_\:\;\'\"\-]+\"')

#========
# classes
#========

class GlobalsContainer():
    """
    A class used to contain internal settings

    ...

    Attributes
    ----------
    custom_crawl_rate : float
        Crawl rate used by _make_soup
    time_exe : boolean
        time code execution

    Methods
    -------
    set_crawl_rate(rate)
        Sets the crawl rate
    get_crawl_rate
        Gets the current crawl rate
    set_time_mode(verbose = False)
        Sets crawling to verbose mode
    get_time_setting
        Gets the current verbose setting
    
    """
    
    def __init__(self):
        """Init container; setup behavior variables
        Set custom_crawl_rate to 0 be default to use
        DEFAULT_CRAWL_RATE
        
        Parameters
        ----------
        self : self

        Returns
        -------
        None
        """
        self.custom_crawl_rate = 0.0
        self.time_exe = False
        
    def set_crawl_rate(self, rate):
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

        if rate <= 0:
            raise Exception('Argument `rate` must not be less than \
            or equal to 0. The input value was {}'.format(rate))
        else:
            self.custom_crawl_rate = rate
            
    def get_crawl_rate(self):
        """Get the rate used to crawl

        Parameters
        ----------
        None

        Returns
        -------
        float
            The current web crawling rate
        """

        if self.custom_crawl_rate != 0:
            return self.custom_crawl_rate
        else:
            return DEFAULT_CRAWL_RATE
            
    def set_time_mode(self, time_exe = False):
        """Enable/Disable code timing

        Parameters
        ----------
        time_exe : boolean
            Internal mode setting

        Returns
        -------
        None
        """

        self.time_exe = time_exe
            
    def get_time_setting(self):
        """Get the current setting of time_exe

        Parameters
        ----------
        None

        Returns
        -------
        boolean
            State of self.time_exe
        """

        return self.time_exe
     

GLContainer = GlobalsContainer()

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

    return GLContainer.get_crawl_rate()

def set_time_mode(time_exe = False):
    """Enable/Disable code timing

    Parameters
    ----------
    time_exe : boolean
        Internal mode setting

    Returns
    -------
    None
    """

    GLContainer.set_time_mode(time_exe)
        
def build_url(year):
    """Builds url for wikipedia 'year in film'

    Parameters
    ----------
    year : str
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
            
def make_soup(url):
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
    
    time.sleep(GLContainer.get_crawl_rate())
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup
    
def scrape_movie_names(year):
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
    
    if GLContainer.get_time_setting():
        t0 = time.time()
    
    url = build_url(year)
    print('Scraping from ' + url)
    soup = make_soup(url)
    
    if GLContainer.get_time_setting():
        t1 = time.time()
    
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
        
    if GLContainer.get_time_setting():
        t2 = time.time()
        print('request time: {:8.4f}'.format(t1-t0))
        print('execution time: {:5.4f}'.format(t2-t1))
    
    return matches