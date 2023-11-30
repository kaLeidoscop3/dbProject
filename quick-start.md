deactivate
Remove-Item -Recurse -Force .\env

python -m venv env
.\env\Scripts\Activate
pip install flask-sqlalchemy
pip install python-dotenv
pip install matplotlib
pip install python-dotenv
flask run