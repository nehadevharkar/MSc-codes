10.Working and implementation of Software as a service.

# app.py
from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return 'Hello, this is a simple SaaS application!'

if _name_ == '_main_':
    app.run(debug=True)