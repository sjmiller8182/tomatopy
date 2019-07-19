"""scraper.py

This file contains the main scraping functions

This file requires no packages.

This file contains the following functions:

    *  scrape_movie_info - main movie scraper

"""
# base
from typing import List, Dict

# this package
from .util import _is_page_404, _build_url, _make_soup
from .main_info import get_main_page_info
from .reviews import get_critic_reviews
from .util import get_verbose_setting

def scrape_movie_info(movie_name: str) -> [Dict[str, List], Dict[str, List]]:
    """Get the main info and critic reviews for
    input movie.

    Parameters
    ----------
    movie_name : string
        movie name to scrape RT for

    Returns
    -------
    dict
        dict containing main information about
        the movie
    dict
        dict containing the review information
        
    """
    
    unable_to_scrape = True
    
    # determine if url can be used
    seps = ['_', '-']
    for _ in seps:
        movie_url = _build_url(movie_name)
        soup = _make_soup(movie_url)
        is_404 = _is_page_404(soup)
        if not is_404:
            unable_to_scrape = False
            break
    
    # scrape page if possible
    if not unable_to_scrape:
        # verbose option
        if get_verbose_setting():
            print('found ' + movie_name)
            
        main_info = get_main_page_info(movie_url)
        critic_reviews = get_critic_reviews(movie_url)
        
        return main_info, critic_reviews
    else:
        print('unable to scrape ' + movie_name)
        return None, None