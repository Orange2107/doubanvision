# -*- coding = utf-8 -*-
# @Time : 2022/1/10 10:50 AM
# @Author : CZJ
# @File  :   wctest.py
# @software : PyCharm

import  sqlite3
import jieba        #分词
from wordcloud import WordCloud
import numpy as np   #转化图片为数组
from PIL import Image

#查询数据库，把结果存为text格式
# db = sqlite3.connect("movie250.db")
# flag = db.cursor()
# sql = '''
#     select sentence from movie
# '''
# words = flag.execute(sql)
# print(type(words))
text ="狗宝宝狗腿子狗鹅鹅宝宝狗狗鹅林狗鹅林凤鹅爱睡觉林狗狗很狗喜欢睡觉洗碗跺脚爱吃喝酒大脸嘟嘴嘴啊狗非洲大草原华南师范上海师范爱吃辣狗住了住在家里爱喝菠萝啤爱吃蛋饼看烟花喜欢去大草原穷很抠合作共赢油头没有胸大长腿爱打台球喜欢发微博狗丫头三院王者万年钻石委屈屈越来越狗打工人提前两个月买新年衣服爱睡觉爱点外卖不知道写什么了注水猪头狗头"
# for item in words:
#      text = text+item[0]  #没有加上[0]取出结果会变成二维数组
result = jieba.cut(text)
result = " ".join(result)

#提取图片
img =Image.open(r"static/assets/img/mask.png", "r")
mask = np.array(img)  #转换成数组
wc = WordCloud(
    scale=10,
    background_color="white",
    font_path="/System/Library/Fonts/Hiragino Sans GB.ttc",
    mask=mask,
    repeat = True,
    contour_width=2,
    contour_color='steelblue',
    max_font_size = 120
).generate(result)
wc.to_file

