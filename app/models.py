# -*- coding: utf-8 -*-
from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))

    def __repr__(self):
        return "<User %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, pwd)


class Info(db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String)
    value = db.Column(db.String)

    def __repr__(self):
        return "<Info %r>" % self.key


class Template(db.Model):
    __tablename__ = 'template'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    css = db.Column(db.CLOB)
    html = db.Column(db.CLOB)
    js = db.Column(db.CLOB, default=None)
    category = db.Column(db.String(64), unique=True)
    order = db.Column(db.Integer)

    isValid = db.Column(db.Boolean, default=True)
    # TODO 解决一个模板在Header, Right, Left, Footer各个层的分类
    # temp_orders = db.Column(db.Integer, db.ForeignKey('templateorder.temp_id'))

    def __repr__(self):
        return "<template %r>" % self.content


# class TemplateOrder(db.Model):
#     __tablename__ = 'templateorder'
#     temp_id = db.Column(db.Integer, primary_key=True)
#     category = db.Column(db.String(64), unique=True)
#     order = db.Column(db.Integer)
#     isValid = db.Column(db.Boolean)
#
#     templates = db.relationship('Template', backref='TemplateOrder')


if __name__ == '__main__':

    # db.drop_all()
    db.create_all()
    from werkzeug.security import generate_password_hash

    user = User(
        name="admin",
        password=generate_password_hash("admin")
    )
    db.session.add(user)
    db.session.commit()
