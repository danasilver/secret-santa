from flask import render_template, redirect, request, url_for
from flask.ext.login import login_user, logout_user, current_user

from . import auth
from .. import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

