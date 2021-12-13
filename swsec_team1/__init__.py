import config
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))

migrate = Migrate()


def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object(config)

    # set optional bootswatch theme
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    # configure session to use sys
    app.config['SESSION_PERMANENT'] = False

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    from . import Models

    from flask import Blueprint
    from .views import main_views, menu_views, review_views, auth_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(menu_views.bp)
    app.register_blueprint(review_views.bp)
    app.register_blueprint(auth_views.bp)

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html')

    return app


app = create_app()
