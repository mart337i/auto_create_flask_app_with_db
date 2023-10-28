import os
import subprocess
import sys

# Step 1: Check if venv module is available
if subprocess.call([sys.executable, '-m', 'venv', '.venv']):
    print("Error: The venv module is not available.")
    sys.exit(1)

# Step 2: Activate virtual environment
activate_file = ".\\.venv\\Scripts\\activate" if os.name == "nt" else "./.venv/bin/activate"
activation_command = f"source {activate_file}"
subprocess.call(["bash", "-c", activation_command])

# Step 3: Install necessary packages in the virtual environment
libs = ["Flask", "Flask-SQLAlchemy", "Flask-Migrate", "PyMySQL"]
subprocess.call([sys.executable, '-m', 'pip', 'install', *libs])

# Step 4: Write the template of the main Flask application file
app_code = """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Database configuration (Change credentials as required)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://YOUR_USERNAME:YOUR_PASSWORD@localhost/YOUR_DATABASE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
"""

with open("app.py", "w") as f:
    f.write(app_code)

print("Template Flask application with MariaDB integration has been created in 'app.py'.")
print("Make sure to update the database credentials in the app configuration.")
print("To run the app, activate the virtual environment and execute 'python app.py'.")