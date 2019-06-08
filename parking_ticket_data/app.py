# import necessary libraries
from flask import (
    render_template,
    jsonify, Flask)
from flask_sqlalchemy import SQLAlchemy

import parking_ticket_data.main_code as main_code

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://vygftypudfazeb:da70bc2df3dd735266a1f1c951f52ff8a41dbbf74937ad66e655c9fc5a0d1762@ec2-184-72-237-95.compute-1.amazonaws.com:5432/dmnbrba78au9k"


db = SQLAlchemy(app)

from .models import ParkingTickets


@app.before_first_request
def setup():
    db.drop_all()
    db.create_all()


@app.route("/")
def home():
    parking_ticket = ParkingTickets()
    main_code.import_data()
    db.session.add(parking_ticket)
    db.session.commit()

    return render_template("index.html")


@app.route("/api/data" methods = "POST")
def list_parking_data():
    results = db.session.query(
        ParkingTickets.date_of_infraction,
        ParkingTickets.infraction_code,
        ParkingTickets.infraction_description,
        ParkingTickets.set_fine_amount,
        ParkingTickets.time_of_infraction,
        ParkingTickets.location2,
        ParkingTickets.lat,
        ParkingTickets.long,
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
            "lat": result[6],
            "long": result[7]
        })

    return jsonify(parking_tickets)


@app.route("/api/filter")
def filter_data():
    return 'test'


if __name__ == "__main__":
    app.run()
