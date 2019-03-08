# -*- conding:utf-8 -*-

import cgi

html_body= """
<!DOCTYPE html>
<html>
  <head>
    <title>scraping</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="stylesheet.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script>
    $(window).on("load resize", function() {
        var width = $("#target").width();
        console.log(width);
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
      <div class="box" id="target">
        <img src="">
        <p class="title"></p>
        <a href="q"></a>
      </div>
      <div class="box">
        <img src="">
        <p class="title"></p>
        <a href="q"></a>
      </div>
      <div class="box">
        <img src="">
        <p class="title"></p>
        <a href="q"></a>
      </div>
      <div class="box">
        <img src="">
        <p class="title"></p>
        <a href="q"></a>
      </div>
      <div class="box">
        <img src="">
        <p class="title"></p>
        <a href="q"></a>
      </div>
      <div class="box">
        <img src="">
        <p class="title"></p>
        <a href="q"></a>
      </div>
      <div class="box">
        <img src="">
        <p class="title"></p>
        <a href="q"></a>
      </div>
      <div class="box">
        <img src="">
        <p class="title"></p>
        <a href="q"></a>
      </div>
      <div class="box">
        <img src="">
        <p class="title"></p>
        <a href="q"></a>
      </div>
      <div class="box">
        <img src="">
        <p class="title"></p>
        <a href="q"></a>
      </div>
    </div>
  </body>
</html>
"""

print(html)
