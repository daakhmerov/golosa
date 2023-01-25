from app import app
from app.menu import menu
from app.db import DB
from app.interview import get_interview

from flask import render_template, request

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title = 'Главная', mainpage=True, menu=menu, db=DB().db)

@app.route("/stories/<int:id>")
def story(id):
    interview = DB().get_entity(id)
    title = interview.get('title')
    abstract = interview.get('abstract')
    codes = interview.get('codes')
    text = get_interview(interview.get('text_uri'))
    

    return render_template("interview.html", title = title, abstract=abstract, text = text, menu=menu, codes=codes)

@app.route("/stories/<int:id>/about")
def story_about(id):
    interview = DB().get_entity(id)
    title = interview.get('title')
    abstract = interview.get('abstract')
    return render_template("article.html", title = title, subtitle = 'Дополнительная информация', content = abstract, menu=menu, request = request)

@app.route("/about")
def about():
    return render_template("article.html", title = 'О проекте', menu=menu)
