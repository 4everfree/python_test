from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

app.run(port='8000')