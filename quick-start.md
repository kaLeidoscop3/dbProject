# Run the following commands in a Powershell terminal:
***
deactivate
Remove-Item -Recurse -Force .\env

python -m venv env
.\env\Scripts\Activate
pip install flask-sqlalchemy
pip install python-dotenv
pip install matplotlib
pip install python-dotenv
flask run
***
# To show the tables, do the following in Bashcd: 
cd .\foodtracker\ 
sqlite3 db.sqlite3
.tables