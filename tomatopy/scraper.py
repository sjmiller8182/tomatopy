"""scraper.py

This file contains the main scraping functions

This file requires no packages.

This file contains the following functions:

    *  

"""

#===================
# imports / m-global
#===================

from .util import _is_page_404, _build_url
from .main_info import get_main_page_info
from .reviews import get_critic_reviews

def scrape_movie_info(movie_name):
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
    # check name (is page a 404?), multiple seperator schemes
    not_404 = is_page_404(movie_name)
    
    if not_404:
        # scrape main info page
        dict_main_info = get_main_info(page)
        # wait between scrapes?
        dict_critic_reviews = get_critic_reviews(page)
        
        # wait between scrapes
        # get_user_reviews
        