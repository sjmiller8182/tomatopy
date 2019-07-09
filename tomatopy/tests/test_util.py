import unittest

from tomatopy.util import _make_soup, _is_page_404, _format_name, _build_url, check_min_delay, get_crawl_rate, set_crawl_rate, get_verbose_setting
from tomatopy.gl import DEFAULT_CRAWL_RATE

class TestUtil(unittest.TestCase):
    
    def test_make_soup(self):
        # basic test to verify the request works
        soup = _make_soup("https://www.rottentomatoes.com/")
        self.assertTrue('Rotten Tomatoes' in str(soup.find('title')))

    def test_is_page_404(self):
        # get a page that is likely 404 for testing
        soup = _make_soup('https://www.rottentomatoes.com/404')
        self.assertTrue(_is_page_404(soup))

    def test_format_name(self):
        # weird name to reformat
        self.assertEqual('x2_xmen_united',
                         _format_name('x2: X-men united'))

    def test_build_url(self):
        # build url from a weird name
        self.assertEqual('https://www.rottentomatoes.com/m/x2_xmen_united/',
                         _build_url('x2: X-men united'))
        # check a typical name
        self.assertEqual('https://www.rottentomatoes.com/m/the_dark_knight/',
                         _build_url('The Dark Knight'))

    # currently check that RT does not seem to have a default crawl rate
    def test_check_min_delay(self):
        self.assertEqual(0,
                         check_min_delay())

    def test_get_crawl_rate(self):
        # expect that default crawl rate is returned on initialization
        self.assertEqual(get_crawl_rate(), 
                         DEFAULT_CRAWL_RATE)

    def test_set_crawl_rate(self):
        # verify that custom crawl rate is returned when set and set back
        set_crawl_rate(10)
        self.assertEqual(get_crawl_rate(), 
                         10)
        set_crawl_rate(DEFAULT_CRAWL_RATE)
        self.assertEqual(get_crawl_rate(), 
                         DEFAULT_CRAWL_RATE)

    def test_get_verbose_setting(self):
        # test that verbose has correct initial setting
        self.assertFalse(get_verbose_setting())