"""__init__.py

Initializes module.

This file requires that `BeautifulSoup` be installed within the Python
environment you are running in.

This file contains not functions.

"""

#====================
# Primary User Access
#====================

from .scraper import scrape_movie_info
from .wikipedia import scrape_movie_names

#=========================
# Supplemental User Access
#=========================

from .reviews import get_critic_reviews
from .main_info import get_main_page_info
from .util import check_min_delay

#====================
# User Control Access
#====================

from .util import set_crawl_rate
from .util import get_crawl_rate
from .util import get_verbose_setting
from .util import set_verbose_mode
