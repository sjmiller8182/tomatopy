import unittest

from tomatopy.wikipedia import _build_wiki_url, scrape_movie_names

class TestWikiedia(unittest.TestCase):
    def test_build_wiki_url(self):
        self.assertEqual(_build_wiki_url(2008),
                         'https://en.wikipedia.org/wiki/2008_in_film')

    def test_scrape_movie_names(self):
        # get movies from 2008 for test
        movies = scrape_movie_names(2008)
        self.assertTrue('The Dark Knight' in movies)
        self.assertTrue('Mishima: A Life in Four Chapters' in movies)
        self.assertTrue("My Best Friend's Girl" in movies)
        self.assertTrue('All That Jazz' in movies)
        self.assertTrue('No Country for Old Men' in movies)

        # get movies from 1980 for test
        movies = scrape_movie_names(1980)
        self.assertTrue('All This, and Heaven Too' in movies)
        self.assertTrue('Honeysuckle Rose' in movies)
        self.assertTrue("The Kidnapping of the President" in movies)
        self.assertTrue('Charly' in movies)
        self.assertTrue('Legend of Tianyun Mountain' in movies)

        # get movies from 1960 for test
        movies = scrape_movie_names(1960)
        self.assertTrue('L\'Avventura' in movies)
        self.assertTrue('Ice Palace' in movies)
        self.assertTrue("Under Ten Flags" in movies)
        self.assertTrue('The Hole' in movies)
        self.assertTrue('Macumba Love' in movies)