#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   gaofei
#   Date    :   18/01/20 09:59:42
#   Desc    :

import media
import fresh_tomatoes

class Entertainment_center(object):
    ''' collect your favor movies '''
    def __init__(self):
        super(Entertainment_center, self).__init__()
        self.movies = []

    def __add__(self, movie):
        if isinstance(movie, list):
            self.movies.extend(movie)
        else:
            self.movies.append(movie)
        return self

    def show(self):
        return fresh_tomatoes.open_movies_page(self.movies)

# These movies put in another independent config files maybe better
tomb_girl = media.Movie(
    title = "tomb girl",
    trailer_url = "http://v.youku.com/v_show/id_XMzMzMTU1MjQyNA==.html",
    poster_image_url = 'http://ykimg.alicdn.com/product/image/2018-01-19/41517801f1ac91a86256c8bb3e97decb.jpg',
)

catch_monster = media.Movie(
    title = "catch monster",
    trailer_url = "http://v.youku.com/v_show/id_XMzMzMDE1MDQ2NA==.html",
    poster_image_url = 'http:////ykimg.alicdn.com/product/image/2018-01-19/0e1e5a8e91a31beaa8048c36285b60a7.jpg',
)

mobile_maze = media.Movie(
    title = "mobile maze",
    trailer_url = "http://v.youku.com/id_XMzMzMTUzODE4NA==.html",
    poster_image_url = 'http://ykimg.alicdn.com/product/image/2018-01-19/898ec69a6516613eed12b1bd27dbcef0.jpg',
)

def main():
    # add movies into Entertainment center
    favor_movies = Entertainment_center()
    favor_movies += [tomb_girl, catch_monster, mobile_maze]
    favor_movies.show()

if __name__ == '__main__':
    main()
