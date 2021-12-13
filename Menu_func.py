from swsec_team1 import db
from swsec_team1.Models import Menu
import os

ALLOWED_EXTENSIONS_DATASET = {'csv', 'json', 'txt', 'xlsx'}
ALLOWED_EXTENSIONS_FIGURE = {'jpg', 'png'}


def allowed_file(fname):
    return '.' in fname and fname.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_DATASET


def is_figure(fname):
    return '.' in fname and fname.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_FIGURE


def get_extension(fname):
    extension = '.' + fname.rsplit('.', 1)[1].lower()
    return extension


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error. Creating Directory. " + directory)


# calc[0] : rating, calc[1] : sales
def calc(menu):
    rating_sum = 0

    sales = 0

    if menu.sales:
        sales = int(menu.sales)

    x = 0

    for review in menu.review_set:
        rating_sum += review.rating
        x += review.sales

    if x != sales:
        sales = x

    if len(menu.review_set) == 0:
        rating = 0
    else:
        rating = round(rating_sum / len(menu.review_set), 2)

    return rating, sales


def get_suggestion(menu):
    total_sales = 0
    rating = calc(menu)[0]
    sales = int(calc(menu)[1])

    for m in db.session.query(Menu).all():
        total_sales += int(m.sales)

    weight = 0.5
    score = (rating * 2 * weight) + ((sales / total_sales) * (1 - weight))
    suggestion = 5

    if sales > 30:
        if score < 5:
            suggestion = 0  # change
        elif score < 8:
            suggestion = 1  # good
        elif score <= 10:
            suggestion = 2  # best
    elif sales > 10:
        if score < 3:
            suggestion = 0  # change
        elif score < 6:
            suggestion = 1  # good
        elif score <= 8:
            suggestion = 2  # best
    else:
        suggestion = None   # low sales

    return suggestion
