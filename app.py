# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

import sqlalchemy as db

app = Flask(__name__)

engine = db.create_engine('dialect+driver://r92rmrsruojzupqe:v10ejjwsi5khwwdo@s3lkt7lynu0uthj8.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/itp11fv3hiub8utw')

connection = engine.connect()

metadata = db.MetaData()
census = db.Table('parking_tickets', metadata, autoload=True, autoload_with=engine)

print(census.columns.keys())


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
