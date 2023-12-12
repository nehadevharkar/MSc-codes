Working and implementation of Platform as a service.

pip install Flask
# app.py
from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return 'Hello, this is a simple PaaS application!'

if _name_ == '_main_':
    app.run(debug=True)