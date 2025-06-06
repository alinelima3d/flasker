from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'my super secret key that no one is suppose to know'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cvv.db'
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Juju56537@localhost/cvv'
# db = SQLAlchemy(app)
#
# # Create a form class
# class NamerForm(FlaskForm):
#     name = StringField("What's your name", validators=[DataRequired()])
#     email = StringField("Email", validators=[DataRequired()])
#     role = StringField("Role", validators=[DataRequired()])
#     submit = SubmitField("Submit")
#
# @app.route('/user/add', methods=['GET', 'POST'])
# def add_user():
#     name = None
#     form = NamerForm()
#     if form.validate_on_submit():
#         user = Members.query.filter_by(email=form.email.data).first()
#         if user is None:
#             user = Members(name=form.name.data, email=form.email.data, role=form.role.data)
#             db.session.add(user)
#             db.session.commit()
#         name = form.name.data
#         form.name.data = ''
#         form.email.data = ''
#
#     our_users = Members.query.order_by(Members.name)
#     return render_template('add_user.html',
#         form = form,
#         name=name,
#         our_users=our_users)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/form', methods=['GET', 'POST'])
def form():
    name = None
    form = NamerForm()
    # Validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('form.html',
        name = name,
        form = form)

## ERROR
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
