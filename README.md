# weibo_post

self_spider

The following is done.

1. set up the key_word which you want to search, usually key_word should be some account which has already been signed up

2. make use of selenium library to grasp all the posts in the first page;

3. the specific items to be scraped:
                profile --> fans  
                     --> follower
                     --> views
                post --> time_stamp
                     --> content
                     --> reposts
                     --> comments
                     --> likes

4. to frontend page to publish using canvas tech


How to run the spider:

    python get_data.py

How to run the express:
    cd /myapp
    set DEBUG=myapp:* & npm start

