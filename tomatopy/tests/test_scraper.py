import unittest

from tomatopy.scraper import scrape_movie_info

class TestScraper(unittest.TestCase):
    
    def test_scrape_movie_info(self):
        # test the main scraper
        main_info, reviews = scrape_movie_info('x2: X-men united')

        # verify keys exist
        keys_main_info = main_info.keys()
        self.assertTrue('synopsis' in keys_main_info)
        self.assertTrue('rating' in keys_main_info)
        self.assertTrue('genre' in keys_main_info)
        self.assertTrue('director' in keys_main_info)
        self.assertTrue('writer' in keys_main_info)
        self.assertTrue('theater_date' in keys_main_info)
        self.assertTrue('dvd_date' in keys_main_info)
        self.assertTrue('currency' in keys_main_info)
        self.assertTrue('box_office' in keys_main_info)
        self.assertTrue('runtime' in keys_main_info)
        self.assertTrue('studio' in keys_main_info)

        # verify content of main_info dict
        self.assertEqual(main_info['synopsis'][:30],'When a failed assassination at')
        self.assertEqual(main_info['rating'],'PG-13')
        self.assertEqual(main_info['genre'],'Action and Adventure|Science Fiction and Fantasy')
        self.assertEqual(main_info['director'],'Bryan Singer')
        self.assertEqual(main_info['writer'],'Daniel Harris|Dan Harris|Michael Dougherty|Bryan Singer|David Hayter')
        self.assertEqual(main_info['theater_date'],'May 2, 2003')
        self.assertEqual(main_info['dvd_date'],'Nov 25, 2003')
        self.assertEqual(main_info['currency'],'$')
        self.assertEqual(main_info['box_office'],'214,813,155')
        self.assertEqual(main_info['runtime'],'134 minutes')
        self.assertEqual(main_info['studio'],'20th Century Fox')

        # verify keys exist
        keys_reviews = reviews.keys()
        self.assertTrue('reviews' in keys_reviews)
        self.assertTrue('rating' in keys_reviews)
        self.assertTrue('fresh' in keys_reviews)
        self.assertTrue('critic' in keys_reviews)
        self.assertTrue('top_critic' in keys_reviews)
        self.assertTrue('date' in keys_reviews)
    
        # cannot verify content as this will likely
        # change as new items are added
        # instead verify that something was captured
        self.assertTrue(len(reviews['reviews']) > 0)
        self.assertTrue(len(reviews['rating']) > 0)
        self.assertTrue(len(reviews['fresh']) > 0)
        self.assertTrue(len(reviews['critic']) > 0)
        self.assertTrue(len(reviews['top_critic']) > 0)
        self.assertTrue(len(reviews['date']) > 0)