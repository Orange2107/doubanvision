import sqlite3
import jieba        #分词
from wordcloud import WordCloud
import numpy as np   #转化图片为数组
from PIL import Image
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route("/movie")
def movielist():
    db = sqlite3.connect("movie250.db")
    flag = db.cursor()
    datalist = []
    sql = '''
    select * from movie
    '''
    data = flag.execute(sql)
    for item in data:
        datalist.append(item)
    db.close()
    return render_template("movie.html", datalist = datalist)   #传送到前端页面

@app.route("/score")
def score():
    score = []
    count = []
    db = sqlite3.connect("movie250.db")
    flag = db.cursor()
    sql= '''
        select score,count(score) from movie group by score
    '''
    result = flag.execute(sql)
    for item in result:
        score.append(item[0])
        count.append(item[1])
    flag.close()
    db.close()
    return render_template("score.html", score = score, count = count)

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/word")
def word():
    imagee = Image.open(r"static/assets/img/wordcloud.png")
    if imagee == "":
        db = sqlite3.connect("movie250.db")
        flag = db.cursor()
        sql = '''
            select name from movie
        '''
        names = flag.execute(sql)   #迭代器
        text = ""
        for item in names:
            text = text+item[0]
        flag.close()
        db.close()
        text_cut = jieba.cut(text)
        text_cut = " ".join(text_cut) #用空格进行分割
        #图片的提取
        image = Image.open(r"static/assets/img/mask.png")
        mask = np.array(image)
        wc = WordCloud(
            scale=10,
            background_color="white",
            font_path="/System/Library/Fonts/Hiragino Sans GB.ttc",
            mask=mask,
            repeat=True,
            contour_width=2,
            contour_color='steelblue',
        ).generate(text_cut)
        wc.to_file(r"static/assets/img/wordcloud.png")
        return render_template("word.html")
    else:
      return render_template("word.html")

if __name__ == '__main__':
    app.run()

