from swsec_team1 import db


# 메뉴명(String), 가격(String), Ingredient(재료명(String), 재료양 (String)), 판매량(String), 별점(1~5) ,메뉴사진(String, 메뉴사진의 파일명)


class Menu(db.Model):
    __table_name__ = 'menu'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)  # 메뉴명 기본키에 공백 불가능
    price = db.Column(db.String(320), nullable=False)  # 가격
    ingredients = db.Column(db.Text(), nullable=False)  # 재료명 : 열량의 리스트 값이 들어감.
    sales = db.Column(db.Integer)  # 판매량
    rate = db.Column(db.Integer)  # 별점
    uploaded_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('menu_set'))
    # figure: use os.path to set dir, use SUBMIT to save the file (png, jpg)


class Review(db.Model):
    __table_name__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id', ondelete='CASCADE'))
    menu = db.relationship('Menu', backref=db.backref('review_set', cascade='all, delete-orphan'))
    # if delete menu --> delete all related reviews
    rating = db.Column(db.Integer, nullable=False)
    sales = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class User(db.Model):
    __table_name__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    access = db.Column(db.String(120), nullable=False)
