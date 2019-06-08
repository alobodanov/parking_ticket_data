import pandas as pd
# import pymysql
# pymysql.install_as_MySQLdb()
import numpy as np
import re
from geopy.geocoders import Nominatim
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://vygftypudfazeb:da70bc2df3dd735266a1f1c951f52ff8a41dbbf74937ad66e655c9fc5a0d1762@ec2-184-72-237-95.compute-1.amazonaws.com:5432/dmnbrba78au9k"


db = SQLAlchemy(app)

# from .models import ParkingTickets


def import_data(ParkingTickets):
    try:
        csv_tickets_1 = "Resources/parking_tickets_2018/Parking_Tags_Data_2018_1.csv"
        ticket_df_1 = pd.read_csv(csv_tickets_1, delim_whitespace=True)

        tickets_2015_df = ticket_df_1
        locations = list(tickets_2015_df["location2"])

        clean_locations = []
        for location in locations:
            try:
                if (re.search(r'\d+\w+', location)):
                    clean_locations.append(location)
            except:
                continue

        clean_locations1 = clean_locations[:933495]
        clean_locations2 = clean_locations[933495:]

        clean_locations1 = list(dict.fromkeys(clean_locations1))
        clean_locations2 = list(dict.fromkeys(clean_locations2))

        clean_locations = clean_locations1 + clean_locations2
        clean_locations = list(dict.fromkeys(clean_locations))

        df = pd.DataFrame({'location2': clean_locations})
        clean_df = pd.merge(tickets_2015_df, df, how="right", on='location2')

        index = np.arange(0, len(clean_df))
        clean_df["id"] = index
        clean_df.set_index("id", inplace=True)
        clean_df = clean_df[["date_of_infraction",
                             "infraction_code",
                             "infraction_description",
                             "set_fine_amount",
                             "time_of_infraction",
                             "location2"
                             ]]

        try:
            clean_df.to_sql(con=db, name='parking_tickets', if_exists='append', flavor='mysql', index=False)
        # save successfull

        except:
            pass

        limit = 750

        i = 0

        while (i <= limit):
            try:
                clean_df1 = clean_df.loc[i]
                geolocator = Nominatim(user_agent="parking_ticket_data")
                location = geolocator.geocode(clean_df1['location2'])

                parking_tickets = ParkingTickets(
                    date_of_infraction=clean_df1['date_of_infraction'],
                    infraction_code=clean_df1['infraction_code'],
                    infraction_description=clean_df1['infraction_description'],
                    set_fine_amount=clean_df1['set_fine_amount'],
                    time_of_infraction=clean_df1['set_fine_amount'],
                    location2=clean_df1['location2'],
                    lat=location.latitude,
                    long=location.longitude
                )

                db.session.add(parking_tickets)
                db.session.commit()
                i = i + 1

            except TypeError as e:
                print(e)
                continue
    except:
        print('error')
