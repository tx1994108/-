# -*- coding:utf-8 -*-
import os



movie_name = os.listdir('/home/tx/BaiduImageSpider/dog/')
count = 51
print(len(movie_name))

for temp in movie_name:
  new_name = count

  os.rename('/home/tx/BaiduImageSpider/dog/' + temp, '/home/tx/BaiduImageSpider/cat2/' + str(new_name)+'.jpg')
  count+= 1