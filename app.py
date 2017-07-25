# -*- coding:utf-8 -*-

from datetime import datetime
from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from controller.douban import douban
from controller.fictionread import fictionread
from controller.jandan import get_articles, get_pics
import json

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    jandans = get_articles()
    doubans = douban()
    pics = get_pics()
    return render_template('index.html', jandans=jandans, doubans=doubans,
                           pics=pics, current_time=datetime.utcnow())

@app.route('/fiction/<number>')
def fiction(number):
    title, post, prev_href, next_href = fictionread(number)
    return render_template('fiction.html', 
                            title=title, post=post, 
                            prev_href=prev_href, next_href=next_href)

@app.route('/games')
def game():
    return render_template('game.html')


if __name__ == "__main__":
    manager.run()