#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   gaofei
#   Date    :   18/01/20 09:58:26
#   Desc    :


class Movie(object):
    ''' movie info '''
    def __init__(self, title, trailer_url, poster_image_url):
        super(Movie, self).__init__()
        self.title = title
        self.trailer_url = trailer_url
        self.poster_image_url = poster_image_url



