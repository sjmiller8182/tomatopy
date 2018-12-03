"""const.py

This file contains constants and classes only.

This file requires no packages.

This file contains to functions.

"""

RT_BASE_URL = 'https://www.rottentomatoes.com/'
DEFAULT_CRAWL_RATE = 1

class LibGlobalsContainer():
    def __init__(self):
        """Init container; setup behavior variables

        Parameters
        ----------
        self : self

        Returns
        -------
        None
        """
        self.custom_crawl_rate = 0
        
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