# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy
# import psycopg2


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://vygftypudfazeb:da70bc2df3dd735266a1f1c951f52ff8a41dbbf74937ad66e655c9fc5a0d1762@ec2-184-72-237-95.compute-1.amazonaws.com:5432/dmnbrba78au9k"

db = SQLAlchemy(app)


class ParkingTickets(db.Model):
    __tablename__ = 'parking_tickets'

    id = db.Column(db.Integer, primary_key=True)
    date_of_infraction = db.Column(db.Integer, nullable=True)
    infraction_code = db.Column(db.Integer, nullable=True)
    infraction_description = db.Column(db.String(1000), nullable=True)
    set_fine_amount = db.Column(db.Float, nullable=True)
    time_of_infraction = db.Column(db.Integer, nullable=True)
    location2 = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return '<ParkingTickets %r>' % (self.location2)


@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()


@app.route("/")
def home():
    parking_ticket = ParkingTickets()

    db.session.add(parking_ticket)
    db.session.commit()

    return render_template("index.html")


@app.route("/api/data")
def list_pets():
    results = db.session.query(
        ParkingTickets.date_of_infraction,
        ParkingTickets.infraction_code,
        ParkingTickets.infraction_description,
        ParkingTickets.set_fine_amount,
        ParkingTickets.time_of_infraction,
        ParkingTickets.location2,
    ).all()

    parking_tickets = []

    for result in results:
        parking_tickets.append({
            "date_of_infraction": result[0],
            "infraction_code": result[1],
            "infraction_description": result[2],
            "set_fine_amount": result[3],
            "time_of_infraction": result[4],
            "location2": result[5],
        })

    return jsonify(parking_tickets)




if __name__ == "__main__":
    app.run()
