"""const.py

This file contains constants and classes only.

This file requires no packages.

This file contains to functions.

"""

#==========
# constants
#==========

RT_BASE_URL = 'https://www.rottentomatoes.com/'
DEFAULT_CRAWL_RATE = 1

#========
# classes
#========

class LibGlobalsContainer():
    """
    A class used to contain internal settings

    ...

    Attributes
    ----------
    custom_crawl_rate : float
        Crawl rate used by _make_soup
    verbose : boolean
        Verbose scraping setting

    Methods
    -------
    set_crawl_rate(rate)
        Sets the crawl rate
    get_crawl_rate
        Gets the current crawl rate
    set_verbose_mode(verbose = False)
        Sets crawling to verbose mode
    get_verbose_setting
        Gets the current verbose setting
    
    """
    
    def __init__(self) -> None:
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
        self.verbose = False
        
    def set_crawl_rate(self, rate: float) -> None:
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
            
    def get_crawl_rate(self) -> float:
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
            
    def set_verbose_mode(self, verbose: bool = False) -> None:
        """Enable/Disable Verbose Mode

        Parameters
        ----------
        verbose : boolean
            Internal mode setting

        Returns
        -------
        None
        """

        self.verbose = verbose
            
    def get_verbose_setting(self) -> bool:
        """Get the current setting of verbose

        Parameters
        ----------
        None

        Returns
        -------
        boolean
            State of self.verbose
        """

        return self.verbose