from flask import Blueprint, render_template, request, redirect, url_for, flash
from swsec_team1.Forms import MenuUploadForm
from swsec_team1.Models import Review, Menu
from swsec_team1 import db
from werkzeug.utils import secure_filename, redirect
from datetime import datetime
import os

bp = Blueprint('review', __name__, url_prefix='/review')


@bp.route('/create/<int:menu_id>', methods=('POST',))
def create(menu_id):
    menu = Menu.query.get_or_404(menu_id)
    rating = request.form['rating']
    sales = request.form['sales']
    review = Review(rating=rating, sales=sales, create_date=datetime.now())
    menu.review_set.append(review)
    db.session.commit()
    total_sales = 0
    total_sales += int(sales)
    return redirect(url_for('menu.detail', menu_id=menu_id))
