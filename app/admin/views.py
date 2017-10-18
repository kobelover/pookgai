# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, session
from . import admin
from app.models import User, Template
from app.admin.forms import LoginForm, TemplateForm
from app import db


@admin.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=data["name"]).first()
        if user is None:
            return redirect(url_for('admin.login'))
        # user = User.query.filter_by(name=data["name"]).first()
        if not user.check_pwd(data['pwd']):
            flash("密码错误!", "err")
            return redirect(url_for('admin.login'))
        session["user"] = user.name
        session["user_id"] = user.id
        return redirect(url_for('admin.user'))
    return render_template('admin/login.html', form=form)


@admin.route('/template', methods=["GET", "POST"])
def template():
    form = TemplateForm()
    if form.validate_on_submit():
        data = form.data
        print("this is submitted")
        if data.get('name') is None:
            flash("为你的模板输入一个名字!", "err")
            return redirect(url_for('admin.template'))
        if data.get('css') is None:
            flash("一个模板增加css文件吧，不然太没文艺感了!", "err")
            return redirect(url_for('admin.template'))
        if data.get('html') is None:
            flash("一个模板HTML文件都不加？", "err")
            return redirect(url_for('admin.template'))

        template = Template(
            name=data.get("name"),
            css=data.get("css"),
            html=data.get("html"),
            js=data.get("js"),
            category=data.get('category'),
            order=data.get('order')
        )
        db.session.add(template)
        db.session.commit()
        flash("添加模板成功！", "ok")
        return redirect(url_for('admin.template'))

    return render_template('admin/template.html', form=form)


@admin.route("/template/list/<int:page>/", methods=["GET"])
def template_list(page=None):
    if page is None:
        page = 1
    template_data = Template.query.paginate(page=page, per_page=20)

    # TODO 解决一个模板在Header, Right, Left, Footer各个层的分类
    return render_template("admin/templates.html", page_data=template_data)


# search header template
@admin.route("/header/<int:page>/",  methods=["GET"])
def header(page):
    if page is None:
        page = 1
    # page_data = Template.query.filter_by(
    #     category="header"
    # ).order_by(
    #     Template.id.desc()
    # ).paginate(page=page, per_page=10)
    page_data = Template.query.paginate(page=page, per_page=20)
    return render_template("home/header/header.html", page_data=page_data)


@admin.route('cool')
def user():
    return "this is user"


@admin.route('/log')
def log():
    return render_template("home/login.html")
