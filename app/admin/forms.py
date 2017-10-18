# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from config import *


class LoginForm(FlaskForm):
    """管理员登录表单"""
    name = StringField(
        label="账号",
        validators=[
            DataRequired("用户名")
        ],
        description="账号",
        render_kw={
            "class": "text",
            "placeholder": "用户名",
            "required": "required"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "password",
            "placeholder": "密码",
            "required": "required"
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "aui-button aui-style aui-button-primary",
        }
    )

    def validate_account(self, field):
        account = field.data
        if USER_NAME != account:
            raise ValidationError("账号不存在！")


class TemplateForm(FlaskForm):
    """template表单"""
    name = StringField(
        label="name",
        validators=[
            DataRequired("  name ")
        ],
        description="css",
        render_kw={
            "class": "template name",
            "placeholder": "template name ",
            # "required": "required"
        }
    )

    css = StringField(
        label="css",
        validators=[
            DataRequired("  CSS ")
        ],
        description="css",
        render_kw={
            "class": "template css",
            "placeholder": "CSS file ",
            "required": "required"
        }
    )

    html = StringField(
        label="html",
        validators=[
            DataRequired("HTMl file")
        ],
        description="html",
        render_kw={
            "class": "template html",
            "placeholder": "HTMl file",
            "required": "required"
        }
    )

    js = StringField(
        label="javascript",
        validators=[
            DataRequired("javascript")
        ],
        description="js",
        render_kw={
            "class": "template js",
            "placeholder": "JS file [ option ]"
            # "required": "required"
        }
    )

    category = StringField(
        label="category",
        validators=[
            DataRequired("category")
        ],
        description="category",
        render_kw={
            "class": "template category",
            "placeholder": "Header , Right, Left, Footer",
            "required": "required"
        }
    )

    order = StringField(
        label="order",
        validators=[
            DataRequired("order")
        ],
        description="order",
        render_kw={
            "class": "template order",
            "placeholder": "order at category",
            "required": "required"
        }
    )

    upload = SubmitField(
        'upload',
        render_kw={
            "class": "upload-button aui-style aui-button-primary"
        }
    )

