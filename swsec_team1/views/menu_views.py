from flask import Blueprint, render_template, request, redirect, url_for, flash, g, session
from swsec_team1.Forms import MenuUploadForm
from swsec_team1.Models import Menu
from swsec_team1 import db
from werkzeug.utils import secure_filename, redirect
from Menu_func import allowed_file, get_extension, calc, get_suggestion
from datetime import datetime
import os

bp = Blueprint('menu', __name__, url_prefix='/menu')
temp_db = 'swsec_team1/static/uploads'


@bp.route('/upload', methods=('GET', 'POST'))
def upload():
    form = MenuUploadForm()
    if request.method == 'POST' and g.user.access == 0:
        menu = Menu(name=form.name.data, price=form.price.data,
                    ingredients=form.ingredients.data, uploaded_date=datetime.now(), user=g.user)
        db.session.add(menu)
        db.session.commit()
        image = request.files['figure']
        if image and allowed_file(image.filename):
            ext = get_extension(image.filename)
            filename = secure_filename(form.name.data + ext)
            image.save(os.path.join(temp_db, filename))
        flash("Successfully Uploaded!")
        return redirect(url_for('menu.detail', menu_id=menu.id))
    elif g.user.access == 1:
        flash("CANNOT ACCESS")
        return redirect(url_for('menu._list'))
    return render_template('menu/menu_upload.html', form=form)


@bp.route('/menu_list', methods=['GET'])
def _list():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    menu_list = Menu.query.order_by(Menu.uploaded_date.desc())

    if kw:
        search = '%%{}%%'.format(kw)
        menu_list = menu_list.filter(Menu.name.ilike(search)
                                     | Menu.ingredients.ilike(search)).distinct()

    menu_list = menu_list.paginate(page, per_page=10)

    return render_template('menu/menu_list.html', menu_list=menu_list, page=page, kw=kw)


@bp.route('/detail/<int:menu_id>')
def detail(menu_id):
    menu = Menu.query.get_or_404(menu_id)
    menu.uploaded_date = menu.uploaded_date  # 날짜 표현 수정 필요. SQL ERROR 발생

    rating = calc(menu)[0]
    sales = calc(menu)[1]

    menu.rate = rating
    menu.sales = sales

    db.session.add(menu)
    db.session.commit()

    suggestion = get_suggestion(menu)

    filenames = [(menu.name + ".jpg"), (menu.name + ".png")]
    file_list = os.listdir(temp_db)
    file = ''
    for i in file_list:
        for n in filenames:
            if i == n:
                file = i
                break

    figure = 'uploads/' + file

    return render_template('menu/menu_detail.html', menu=menu, rating=rating, figure=figure, suggestion=suggestion)


@bp.route('/sales')
def sales():
    menus = list()
    total_sales = 0
    total_reviews = 0
    earnings = 0

    for m in db.session.query(Menu).all():
        menus.append([m, get_suggestion(m)])
        total_sales += int(m.sales)
        total_reviews += int(len(m.review_set))
        earnings += total_sales * int(m.price)

    return render_template('menu/sales.html', menus=menus, total_sales=total_sales, total_reviews=total_reviews,
                           earnings=earnings)
