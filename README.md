# TomatoPy - Rotten Tomatoes Scraper

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.org/project/requests/)

Easy web scraping for [rotten tomatoes](https://www.rottentomatoes.com/) movie reviews and info.

![](https://c1.staticflickr.com/4/3614/3695696788_219f255121_b.jpg?raw=true)

[Enjoy the recipe](https://www.geniuskitchen.com/recipe/easy-tomato-cheese-pie-with-crumb-crust-27486)

### Recent Versions

- Initial Release 0.0.0
  - One line scraper
  - Critic review scraper
  - Main info scraper

### Planned Updates for 0.1.0

- Scrape user reviews
- Update secondary API functions to accept movie name instead of link
- Scrape Tomatometer and Audience Score in main info.
- Check robots.txt for crawl rate in case of future addition

### Basic Usage

```python
import tomatopy as rtp

# get main information and critic reivews for X2
main_info, reviews = rtp.scrape_movie_info('X2: X-Men United')

# just get main info
reivews = get_critic_reviews(https://www.rottentomatoes.com/m/x2_xmen_united)

# just get critic reviews
main_info = get_main_page_info(https://www.rottentomatoes.com/m/x2_xmen_united)

# change crawl rate to 1 second per request (default rate)
rtp.set_crawl_rate(1.0)
```
