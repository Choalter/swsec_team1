from flask import Blueprint, render_template, g, redirect, url_for
from ..Models import Menu

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    if g.user is None:  # no login
        return redirect(url_for('menu._list'))
    elif g.user.access == 0:    # operator
        return redirect(url_for('menu.sales'))
    else:   # customer
        return redirect(url_for('menu._list'))


@bp.route('menu_list/')
def menus_list():
    menu_list = Menu.query.order_by(Menu.uploaded_date.desc())
    return render_template('menu/menu_list.html', menu_list=menu_list)
