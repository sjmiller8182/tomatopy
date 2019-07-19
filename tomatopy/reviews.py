"""main_info.py

This file contains private functions for scraping the review pages

This file requires no packages.

This file contains the following functions:

    * _get_critic_reviews_from_page - scrapes info per critic page
    * _get_num_pages - finds number of pages to scrape
    * get_critic_reviews - scrapes info over all critic pages 

"""

#===================
# imports / m-global
#===================

# base
import re
import time
from typing import Dict, List

# this package
from .util import _make_soup
from .util import get_verbose_setting
from .util import _build_url

# regex patterns
# run once on import
page_pat = re.compile(r'Page 1 of \d+')
review_pat = re.compile(r'<div class=\"the_review\">[;a-zA-Z\s,-.\'\/\?\[\]\":\']*</div>')
rating_pat = re.compile(r'Original Score:\s([A-Z](\+|-)?|\d(.\d)?(\/\d)?)')
fresh_pat = re.compile(r'small\s(fresh|rotten)\"')
critic_pat = re.compile(r'\/\"\>([A-Z][a-zA-Z]+\s[A-Z][a-zA-Z\-]+)|([A-Z][a-zA-Z.]+\s[A-Z].?\s[A-Z][a-zA-Z]+)|([A-Z][a-zA-Z]+\s[A-Z]+\'[A-Z][a-zA-Z]+)')
publisher_pat = re.compile(r'\"subtle\">[a-zA-Z\s,.\(\)\'\-&;!\/\d+]+</em>')
date_pat = re.compile(r'[a-zA-Z]+\s\d+,\s\d+')

#=======================
# Critic Review Handling
#=======================

#==================
# interal functions
#==================

def _get_critic_reviews_from_page(soup) -> List:
    """Get the review, rating, critic, if critic is a 
    'top critic', publisher, date from a given page (bs4)

    Parameters
    ----------
    soup : bs4 object
        bs4 html tree from html_parser

    Returns
    -------
    list
        list of lists containing the following:
        reviews, rating, fresh, critic, top_critic,
        publisher, date
        
    """
    
    reviews = list()
    rating = list()
    fresh = list()
    critic = list()
    top_critic = list()
    publisher = list()
    date = list()
    
    soup = str(soup)
    review_soup = soup.split('="review_table')[1].split('row review_table_row')
    review_soup.pop(0)
    
    # extract info
    for review in review_soup:
        
        # extract review
        match = re.findall(review_pat, str(review))
        if len(match) > 0:
            m = match[0]
            for iden in ['<div class="the_review"> ','</div>']:
                m = m.replace(iden,'')
            reviews.append(m.strip('"'))
            
            # extract rating
            match = re.findall(rating_pat, str(review))
            if len(match) > 0:
                m = match[0][0]
                if '/1' in m:
                    sp_m = m.split('/')
                    if sp_m[-1] == '1':
                        sp_m[-1] = '10'
                    m = '/'.join(sp_m)
                rating.append(m)
            else:
                rating.append(None)
            
            # extract fresh indicator
            match = re.findall(fresh_pat, str(review))
            if len(match) > 0:
                fresh.append(match[0])
            else:
                fresh.append(None)
            
            # extract ciritic
            match = re.findall(critic_pat, str(review))
            if len(match) > 0:
                critic.append(''.join(match[0]))
            else:
                critic.append(None)
            
            # check if top critic
            if '> Top Critic<' in str(review):
                top_critic.append(1)
            else:
                top_critic.append(0)
            
            # extract publisher
            match = re.findall(publisher_pat, str(review))
            if len(match) > 0:
                m = match[0]
                m = m.replace('"subtle">', '')
                m = m.replace('</em>','')
                publisher.append(m)
            else:
                publisher.append(None)
            
            # extract date
            match = re.findall(date_pat, str(review))
            if len(match) > 0:
                date.append(match[0].strip('"'))
            else:
                date.append(None)
            
    return [reviews, rating, fresh, critic, top_critic, publisher, date]

def _get_num_pages(soup) -> List:
    """Find the number of pages to scrape reviews from

    Parameters
    ----------
    soup : bs4 object
        bs4 html tree from html_parser

    Returns
    -------
    str
        number of pages with reviews
        
    """
    
    # from soup decend to page level
    match = re.findall(page_pat,str(list(soup)))
    if len(match) > 0:
        match = match[0]
        match = match.split(' of ')[-1]
        return match
    else:
        return None

#===============
# user functions
#===============
    
def get_critic_reviews(page: str) -> Dict[str, List]:
    """Crawls the set of critic review pages for the given movie.
    Returns a dict withkeys: reviews, rating, fresh,
    critic, top_critic, publisher, date.

    Parameters
    ----------
    page : str
        main page url for movie

    Returns
    -------
    dict
        dict containing scraped review info with the following keys:
        'reviews', 'rating', 'fresh', 'critic', 'top_critic',
        'publisher', 'date'
        
    """

    # containers
    info = [[],[],[],[],[],[],[]]
        
    # make soup
    soup = _make_soup(page + "reviews")
    
    # how many soups?
    pages = _get_num_pages(soup)
    
    if pages is not None:
        # verbose option
        if get_verbose_setting():
            print('scraping critic reviews')
            print('scraping url: ' + page + "reviews " + str(pages) + " pages to scrape")
        
        # eat soup
        for page_num in range(1,int(pages)+1):
            soup = _make_soup(page + "reviews?page=" + str(page_num) + "&sort=")
            c_info = _get_critic_reviews_from_page(soup)
            
            # accumulate review info
            for i in range(len(c_info)):
                info[i] = info[i] + c_info[i]
        
        c_info = dict()
        keys = ['reviews', 'rating', 'fresh', 'critic', 'top_critic', 'publisher', 'date']
        for k in range(len(keys)):
            c_info[keys[k]] = info[k]
        
        # verbose option
        if get_verbose_setting():
            print('done scraping critic reviews')
    else:
        # if pages doesnt match return None; its easy to detect
        c_info = None
        
    return c_info
    
#=====================
# User Review Handling
#=====================

# TODO: Add scraping for user reviews

