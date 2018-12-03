# TomatoPy - Rotten Tomatoes Scraper
====================================

[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://pypi.org/project/requests/)

Easy web scraping for [rotten tomatoes](https://www.rottentomatoes.com/) movie reviews and info.

![](https://c1.staticflickr.com/4/3614/3695696788_219f255121_b.jpg?raw=true)

[Enjoy the recipe](https://www.geniuskitchen.com/recipe/easy-tomato-cheese-pie-with-crumb-crust-27486)

### Basic Usage

```python
import tomatopy as rtp
# get main information and critic reivews 
main_info, reviews = rtp.scrape_movie_info('X2: X-Men United')
```
