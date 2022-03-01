# imports and dependencies
import numpy as np
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, distinct
from flask import Flask, jsonify, render_template, request
import datetime as dt

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect = True)

# Save references to each table
Measurement = Base.classes.measurement

Station = Base.classes.station

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
     return (
        f"<h1> Welcome to Joshua Moon's HW 10 Assignment!</h1>"
        f"<h2> Here are the available routes: </h2><br/>"
        f"<h3> (0) Precipitation Data: <a href=\"/api/v1.0/precipitation\">/api/v1.0/precipitation<a></h3><br/>"
        f"<h3> (0) Station Data: <a href=\"/api/v1.0/stations\">/api/v1.0/stations<a></h3><br/>"
        f"<h3> (0) Temp Observation (TOBS) Data:  <a href=\"/api/v1.0/tobs\">/api/v1.0/tobs<a></h3><br/>"
        f"<h3> (0) Min, Average, & Max Temperatures for Date Range (Pre-filled Jan - Dec 2014): <a href=\"/api/v1.0/2014-01-01/2014-12-31\">/api/v1.0/2014-01-01/2014-12-31<a></h3><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create session to link to database
    session = Session(engine)

    # Query and summarize precipitation across all stations     
    sel = [Measurement.date, Measurement.prcp]
    result = session.query(*sel).all()
    session.close()

    precipitation = []
    for date, prcp in result:
        prcp_dict = {}
        prcp_dict["Date"] = date
        prcp_dict["Precipitation"] = prcp
        precipitation.append(prcp_dict)

    return jsonify(precipitation)


@app.route("/api/v1.0/stations")
def stations():
    # Create session to link to database
    session = Session(engine)

    # Query all stations
    sel = [Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation]
    result = session.query(*sel).all()
    session.close()

    stations = []
    for station, name, lat, lng, elv in result:
        station_dict = {}
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Lat"] = lat
        station_dict["Lng"] = lng
        station_dict["Elevation"] = elv
        stations.append(station_dict)

    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create session to link to database
    session = Session(engine)

    # Find the latest date for querying
    latest_str = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    latest_date = dt.datetime.strptime(latest_str, '%Y-%m-%d')
    query_date = dt.date(latest_date.year -1, latest_date.month, latest_date.day)

    # Query all tobs
    sel = [Measurement.date, Measurement.tobs]
    result = session.query(*sel).filter(Measurement.date >= query_date).all()
    session.close()
    
    # Parse through query and append to dict then to list
    all_tobs = []
    for date, tobs in result:
        tobs_dict = {}
        tobs_dict['Date'] = date
        tobs_dict['Tobs'] = tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)


@app.route("/api/v1.0/<start>")
def Start(start):
    # Create session to link to database
    session = Session(engine)

    # Query
    result = session.query(func.min(Measurement.tobs),
                            func.avg(Measurement.tobs),
                            func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).all()    
    session.close()

    # Create dict from row data and append to a list
    start_list = []
    for min, avg, max in result:
        start_dict = {}
        start_dict["Min"] = min
        start_dict["Average"] = avg
        start_dict["Max"] = max
        start_list.append(start_dict)

    return jsonify(start_list)


@app.route("/api/v1.0/<start>/<end>")
def Start_end(start, end):
    # Create session to link to database
    session = Session(engine)

    # Query
    results = session.query(func.min(Measurement.tobs),
                            func.avg(Measurement.tobs),
                            func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()

    # Create dict from data and append to list
    start_end_list = []
    for min, avg, max in results:
            start_end_dict = {}
            start_end_dict["Min"] = min
            start_end_dict["Average"] = avg
            start_end_dict["Max"] = max
            start_end_list.append(start_end_dict)

    return jsonify(start_end_list)

if __name__ == "__main__":
    app.run(debug = True)