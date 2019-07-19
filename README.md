# TomatoPy - Rotten Tomatoes Scraper

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.org/project/requests/)

Easy web scraping for [Rotten Tomatoes](https://www.rottentomatoes.com/) movie reviews and info. 

![](https://c1.staticflickr.com/4/3614/3695696788_219f255121_b.jpg?raw=true)

[Enjoy the recipe](https://www.geniuskitchen.com/recipe/easy-tomato-cheese-pie-with-crumb-crust-27486)

**Why Rotten Tomatoes?**  
Rotten Tomatoes is the world's most trusted source for entertainment recommendations. They provide users with indications of fresh or rotten by aggreation of reviews from critics. [Learn more about Rotten Tomatoes](https://www.rottentomatoes.com/about/).

### Recent Versions

### Initial Release 0.0.0
- One line scraper
- Critic review scraper
- Main info scraper

### Planned Updates for 0.1.0

- Add code to get movie names from Wikipedia
- ~~Update secondary API functions to accept movie name instead of link~~
- Check robots.txt for crawl rate in case of future addition

### Planned Updates for 0.1.1
- Type hints

### Planned Updates for 0.2.0
- Scrape user reviews
- Scrape Tomatometer and audience score in main info.

### Basic Usage

```python
import tomatopy as rtp

# get main information and critic reivews for X2
main_info, reviews = rtp.scrape_movie_info('X2: X-Men United')

# just get main info
reivews = rtp.get_critic_reviews('https://www.rottentomatoes.com/m/x2_xmen_united')

# just get critic reviews
main_info = rtp.get_main_page_info('https://www.rottentomatoes.com/m/x2_xmen_united')

# change crawl rate to 1 second per request (default rate)
rtp.set_crawl_rate(1.0)

# get movie names from wikipedia [2008 in film] (https://en.wikipedia.org/wiki/2008_in_film)
names = rtp.scrape_movie_names(2008)
```
