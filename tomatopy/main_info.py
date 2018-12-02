# imports
import re
import time
from .util import _make_soup
from .const import DEFAULT_CRAWL_RATE

# regex patterns
# run once on import
movieSyn_pat = re.compile(r'movieSynopsis[a-zA-Z\"\s=\:]+>\s+[a-zA-Z\"\s=\:.,-\;\&\']+')
rating_pat = re.compile(r'Rating: </div>[\s]+[a-zA-Z\=\-\<\>\s\"]+\>[A-Z\-\d]+')
genres_pat = re.compile(r'Genre: </div>[\s]+[a-zA-Z\=\-\<\>\s\"\/\?\d\&\;\,]+</div>')
dir_pat = re.compile(r'Directed By: </div>[a-zA-Z\=\-\<\>\s\"\/\?\d\&\;\,\_]+</div>')
wrt_pat = re.compile(r'Written By: </div>[a-zA-Z\=\-\<\>\s\"\/\?\d\&\;\,\_]+</div>')
date_pat = re.compile(r'In Theaters: </div>[a-zA-Z\=\-\<\>\s\"\/\?\d\&\;\,\_\:]+</time>')
date2_pat = re.compile(r'\w+\s\d+\,\s\d+')
boxOff_pat = re.compile(r'Box Office: </div>[\sa-z\<\=\"\-\>]+.?[\d,]+')  
rt_pat = re.compile(r'Runtime: </div>[\sa-zA-Z\d\<\=\"\-\>]+minutes')
studio_pat = re.compile(r'Studio: </div>[\sa-zA-Z\d\<\=\"\-\>\:\/\.]+a>\s+</div>')   

def get_main_page_info(page, crawl_rate = DEFAULT_CRAWL_RATE):
    info = dict()   
    
    # make soup
    time.sleep(crawl_rate)
    soup = _make_soup(page)
    
    # prepare soup
    # ignore steping through tree due to instability
    info_html = str(soup)
    
    ### eat soup ###
    
    # get synopsis
    match = re.findall(movieSyn_pat, info_html)
    if len(match) > 0:
        match = match[0].split('>')[-1].replace('\n','').replace('                ','')
        info['synopsis'] = match
    else:
        info['synopsis'] = None
    
    # get rating
    match = re.findall(rating_pat, info_html)
    if len(match) > 0:
        match = match[0].split('>')[-1]
        info['rating'] = match
    else:
        info['rating'] = None
    
    # get genre
    match = re.findall(genres_pat, info_html)
    if len(match) > 0:
        match = match[0].replace('&amp;','and').split('>')
        genre = list()
        for g in match:
            if '</a' in g:
                genre.append(g.replace('</a','').rstrip().lstrip())
        info['genre'] = '|'.join(genre)
    else:
        info['genre'] = None
    
    # get director
    match = re.findall(dir_pat, info_html)
    if len(match) > 0:
        match = match[0].replace('&amp;','and').split('>')
        director = list()
        for d in match:
            if '</a' in d:
                director.append(d.replace('</a',''))
        info['director'] = '|'.join(director)
    else:
        info['director'] = None
    
    # get director
    match = re.findall(wrt_pat, info_html)
    if len(match) > 0:
        match = match[0].replace('&amp;','and').split('>')
        writer = list()
        for w in match:
            if '</a' in w:
                writer.append(w.replace('</a',''))
        info['writer'] = '|'.join(writer)
    else:
        info['writer'] = None
    
    # get dates
    match = re.findall(date_pat, info_html)
    if len(match) > 0:
        match = re.findall(date2_pat, match[0])
        if len(match) == 2:
            info['theater_date'] = match[0]
            info['dvd_date'] = match[1]
        else:
            #match failed
            info['theater_date'] = None
            info['dvd_date'] = None
    else:
        info['theater_date'] = None
        info['dvd_date'] = None
    
    # get box_office
    match = re.findall(boxOff_pat, info_html)
    if len(match) > 0:
        info['currency'] = match[0].split('>')[-1][0]
        info['box_office'] = match[0].split('>')[-1][1:]
    else:
        info['currency'] = None
        info['box_office'] = None
    
    # get runtime
    match = re.findall(rt_pat, info_html)
    if len(match) > 0:
        info['runtime'] = match[0].split('\n')[-1].lstrip()
    else:
        info['runtime'] = None
    
    # get studio
    match = re.findall(studio_pat, info_html)
    if len(match) > 0:
        match = match[0].split('">')
        studio = list()
        for s in match:
            if '</a>' in s:
                studio.append(s.replace('</a>','').replace('</div>','').rstrip())
        info['studio'] = '|'.join(studio)
    else:
        info['studio'] = None
    
    return info