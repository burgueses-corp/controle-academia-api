from flask import Flask, render_template
#from pymongo import MongoClient

app = Flask(__name__)

#client = MongoClient('localhost', 27017)

#db = client.flask_db
#todos = db.todos

@app.route('/')
def index():
    return render_template('main/home.html')

if __name__ == '__main__':
    app.run(debug=True)