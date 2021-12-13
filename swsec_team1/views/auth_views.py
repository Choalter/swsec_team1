from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from .. import db
from ..Forms import UserCreateForm, UserLoginForm
from ..Models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register/', methods=('GET', 'POST'))
def register():
    if not session.get('logged_in'):
        form = UserCreateForm()
        if request.method == 'POST' and form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            email = User.query.filter_by(email=form.email.data).first()
            if not user:
                user = User(username=form.username.data, password=generate_password_hash(form.password1.data),
                            email=form.email.data, access=form.access.data)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('auth.login'))
            else:
                if email:
                    flash('Email Already Exists')
                elif user:
                    flash('User Already Exists')
                else:
                    flash('User and Email Already Exist')
    else:
        flash('Already logged in')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)


@bp.route('/login/', methods=('GET', 'POST'))
def login():
    if not session.get('logged_in'):
        form = UserLoginForm()
        if request.method == 'POST' and form.validate_on_submit():
            error = None
            user = User.query.filter_by(username=form.username.data).first()
            if not user:
                error = 'Username {} does not exist.'.format(form.username.data)
            elif not check_password_hash(user.password, form.password.data):
                error = 'Incorrect password.'
            if error is None:
                session.clear()
                session['user_id'] = user.id
                session['logged_in'] = True
                return redirect(url_for('main.index'))
            flash(error)
    else:
        flash("Already logged in")
        return redirect(request.url)
    return render_template('auth/login.html', form=form)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)
        session['logged_in'] = True


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))
