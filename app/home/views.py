# -*- coding: utf-8 -*-
from flask import render_template
from . import home
from config import *


@home.route("/log/index")
def home_head():
    return render_template("home/index.html", title=TITLE_NAME)


@home.route("/log")
def home_log():
    return render_template("home/left/logg.html")


@home.route("/sidebar")
def home_sidebar():
    return render_template("sidebar.html")


@home.route("/left")
def home_left():
    return render_template("home/left/left_main.html")


@home.route('/hd')
def home_hd():
    return render_template("home/header.html")


@home.route('/index')
def home_hello():
    return render_template("index2.html")


@home.route("/")
def home_index():
    return render_template("home/index.html")


@home.route("/header")
def home_header():
    return render_template("home/header.html")


@home.route("/person")
def home_person():
    return render_template("home/left/person.html")


@home.route("/special")
def home_special():
    return render_template("home/specialites.html")


@home.route("/skill")
def home_skill():
    return render_template("home/left/skill.html")


@home.route("/language")
def home_language():
    return render_template("home/language.html")


@home.route("/recognitions")
def home_recognitions():
    return render_template("home/left/recognitions.html")


@home.route("/experience")
def home_experience():
    return render_template("home/experience.html")


@home.route("/edu")
def home_edu():
    return render_template("home/left/edu.html")


@home.route("/interest")
def home_interest():
    return render_template("home/interest.html")


@home.route("/login")
def home_login():
    return render_template("home/login.html")
