#===================
# imports / m-global
#===================



    # check name (is page a 404?
    not_404, page = is_page_404(movie_name)
    
    if not_404:
        # scrape main info page
        dict_main_info = get_main_info(page)
        # wait between scrapes?
        dict_critic_reviews = get_critic_reviews(page)
        
        # wait between scrapes
        # get_user_reviews
        