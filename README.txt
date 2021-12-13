Windows Powershell

$env:FLASK_APP='swsec_team1'
$env:FLASK_ENV='development'
flask run

Mac, LINUX

export FLASK_APP='swsec_team1'
export FLASK_ENV = 'development'
flask run

Windows Command

set FLASK_APP='swsec_team1'
set FLASK_ENV='development'
flask run

------------------------------------------------

when you run the server first in your PC,
do:

flask db init
flask db migrate
flask db upgrade

flask run

------------------------------------------------

python version = 3.9

do install (pip or pip3):

pip install Flask
pip install Flask-sqlalchemy
pip install Flask-wtf
pip install Flask-migrate
pip install werkzeug
pip install wtforms
