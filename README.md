# doubanvision
 ### 豆瓣爬虫数据的可视化

- 利用flask框架搭建网页
![image](https://user-images.githubusercontent.com/70784569/148787048-e83151ee-4e37-4bb3-b291-bd55d657ec5b.png)


- 实现从sqlite数据库查询数据，在网页的实现。
![image](https://user-images.githubusercontent.com/70784569/148787143-2f624420-b78a-4488-9f6d-b84beecef2f8.png)


  ### Pycharm中sqlite的使用

  #### sqlite简介

  - SQLite是一个**进程内的库**，实现了自给自足的、无服务器的、零配置的、事务性的 SQL 数据库引擎。它是一个零配置的数据库，这意味着与其他数据库不一样，您不需要在系统中配置。

  - 就像其他数据库，SQLite 引擎**不是一个独立的进程**，可以按应用程序需求进行静态或动态连接。SQLite 直接访问其存储文件。
  - **不需要**一个单独的**服务器**进程或操作的系统（无服务器的）。
  - SQLite **不需要配置**，这意味着不需要安装或管理。
  - 一个完整的 SQLite 数据库是存储在一个单一的跨平台的磁盘文件。
  - SQLite 是非常小的，**是轻量级的**，完全配置时小于 400KiB，省略可选功能配置时小于250KiB。
  - SQLite 是自给自足的，这意味着不需要任何外部的依赖。
  - SQLite 事务是完全兼容 ACID 的，允许从**多个进程或线程**安全访问。
  - SQLite 支持 SQL92（SQL2）标准的**大多数查询语言**的功能。
  - SQLite 使用 ANSI-C 编写的，并提供了简单和易于使用的 API。
  - SQLite 可在 UNIX（Linux, Mac OS-X, Android, iOS）和 Windows（Win32, WinCE, WinR）

  #### sqlite常用操作

  #### 1. sqlite的准备和关闭（Python）

  ```python
  import sqlite3  		#引入包
  db = sqlite3.connect("company.db")
  flag = db.cursor()   #创建数据库游标
  #数据库操作完成后
  db.commit()   #在对表作出变化时需要
  db.close()
  #sql语句的执行
  游标.execute(sql)
  ```

  #### 2.常用的操作

  ```python
  #数据库表的创建
  create table company 
  	(id int primary key not null,
     name tetx not null,
     age int not null,
     address char(50),
     salary real;
    )
  #数据库表的删除
  drop table company
  #表的增插入
  insert into company(id, name, age, address, salary)
   values (2104, "clx",21, "fzu", 15000 );
  #表的删除
  delete from company
  where 判断条件;
  #表的查询
  select *
  from XXX
  where XXX;
  #表的更新
  update table's name
  set value1 = "XXX",value2 = "xxx", value3 = "xxx"
  where 判断条件
  #sql语句的执行
  flag.execute(sql)
  ```

  #### 3. 一些常用语句

  ```python
  #order语句
  select * from student 
  where sdept = 'cs'
  order by score asc/desc
  #group语句 SQLite 的 GROUP BY 子句用于与 SELECT 语句一起使用，来对相同的数据进行分组。
  select name, sum(salary)
  from company
  group by name
  order by sum(salary);   
  result： [('xmu', 47000.0), ('fzu', 80000.0)]  #输出的结果
  result： [(11, 'cz', 22, 'xmu', 25000.0), (2107, 'czj', 22, 'fzu', 30000.0)] #输出的结果 select *。因为有group的存在，对结果进行分组
  
  ```

  #### 4.sqlite数据类型

  | NULL    | 值是一个 NULL 值。                                           |
  | ------- | ------------------------------------------------------------ |
  | INTEGER | 值是一个带符号的整数，根据值的大小存储在 1、2、3、4、6 或 8 字节中。 |
  | REAL    | 值是一个浮点值，存储为 8 字节的 IEEE 浮点数字。              |
  | TEXT    | 值是一个文本字符串，使用数据库编码（UTF-8、UTF-16BE 或 UTF-16LE）存储。 |
  | BLOB    | 值是一个 blob 数据，完全根据它的输入存储。                   |

  #### 5.遇到的问题

  ![image-20220101215902148](/Users/chenzijie/Library/Application Support/typora-user-images/image-20220101215902148.png)

  **在提取数据库中数据时，出现了该问题**

  原因：在关闭了数据库后，会连同cursor一同关闭。如果没有把游标查找到的数据存储在列表中，数据会丢失。

  ![image-20220101220404686](/Users/chenzijie/Library/Application Support/typora-user-images/image-20220101220404686.png)

  如图所示，cursor查找到的result是cursor类型的对象，需要再次存储才能变成list类型（在数据库关闭后还能继续使用）。

- 简单的使用了一下e-charts实现评分的可视化。

  ![image-20220110225212078](/Users/chenzijie/Library/Application Support/typora-user-images/image-20220110225212078.png)

- 使用wordcloud实现电影名称的可视化。![image-20220110225240187](/Users/chenzijie/Library/Application Support/typora-user-images/image-20220110225240187.png)

### 词云的实现

- 需要引入的包

1. ```python
   import jieba  #对提取的text进行处理，根据词频分割出词。
   ```

2. ```python
   import numpy as np   #转化图片为数组
   ```

3. ```python
   from wordcloud import WordCloud #引入词云包
   ```

4. ```python
   from PIL import Image #实现对图片的处理
   ```

- 操作流程

1. 使用sql数据库语句提取数据库中目标数据，将数据存为字符串。

   ```python
   #查询数据库，把结果存为text格式
   db = sqlite3.connect("movie250.db")
   flag = db.cursor()
   sql = '''
       select sentence from movie
   '''
   words = flag.execute(sql)
   text =""
   for item in words:
       print(item)    			 #发现提取出来的是每一个数组，需要加上下标才是获取内容。
       text = text+item[0]  
   result = jieba.cut(text) 
   result = " ".join(result) #对结果(是一个对象）进行分词
   ```

2. 图片的绘制，一些wordcloud的参数的设置。

   ```python
   #提取图片
   img =Image.open(r"static/assets/img/mask.png", "r")
   mask = np.array(img)  #转换成数组
   wc = WordCloud(
       scale=10,  			#决定了生存图片的清晰度，值越高速度越慢。
       background_color="white",
       font_path="/System/Library/Fonts/Hiragino Sans GB.ttc",   #设置所识别text的字体
       mask=mask,		#设置遮罩层
       repeat = True,  #数字不够时可以重复
       contour_width=2, #图片瞄边
       contour_color='steelblue',
       max_font_size = 120
   ).generate(result)  #生成词云对象
   wc.to_file("gbb.png") 
   ```
词云的流程图
![image](https://user-images.githubusercontent.com/70784569/149539966-a1091847-fd66-42cc-af00-17014727ff59.png)

   
