#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cgi
import cgitb
import os
import sqlite3

cgitb.enable()

filename = "qiita_scrapy.db"
html_boxs = ""

db = sqlite3.connect(os.path.join(os.getcwd(), filename))
cursor = db.cursor()
rows = cursor.execute("SELECT * FROM post")



print("Content-Type: text/html")
print("")

html_1= """
<!DOCTYPE html>
<html>
  <head>
    <title>scraping</title>
    <meta charset="utf-8">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Cache-Control" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <link rel="stylesheet" href="../stylesheet.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script>
    $(window).on("load resize", function() {
        var width = $("#target").width();
        $(".box").css({"height": width});
      })
    </script>
  </head>
  <body>
    <header>
      <p>Scraping</p>
      <ul>
        <li class="tech">技術</li>
        <li class="news">ニュース</li>
        <li class="ivent">イベント</li>
      </ul>
    </header>
    <div class="main">
    """

for row in rows:
    html_boxs += """<div class="box" id="target">
    <img src="../python_18894.png">
    <p class="title">{0}</p>
    <a href="https://qiita.com{1}"></a>
    <p class="date">{2}</p>
    </div>""".format(row[0], row[1], row[2])

html_2 = """
    </div>
  </body>
</html>
"""

print(html_1 + html_boxs + html_2)
