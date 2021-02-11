from flask import Flask, request, render_template, redirect
from flask_pymongo import PyMongo
import scrape_app

#create instance
app = Flask(__name__)

mongo = PyMongo(app,uri="mongodb://localhost:27017/mars_app")
# mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html",mars = mars)

@app.route("/scrape")
def scrape():
    mars_dict = mongo.db.mars
    mars_data = scrape_app.scrape()
    print('dictionary from scrape : \n',mars_data)
    mars_dict.update({},mars_data, upsert = True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)
