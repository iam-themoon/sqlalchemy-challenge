# imports and dependencies
import numpy as numpy
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, fuc, distinct
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect = True)

# Save references to each table
measurement = Base.classes.measurement
station = base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the homepage! <br/>"
        f"Available routes: <br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all daily precipitation totals for the last year"""
    # Query and summarize daily precipitation across all stations for the last year of available data 
    
    start_date = '2016-08-23'
    sel = [measurement.date, func.sum(measurement.prcp)]
    precipitation = session.query(*sel).\
        filter(measurement.date >= start_date).\
        group_by(measurement.date).\
        order_by(measurement.date).all()

    session.close()

    # Create dictionary from results and jsonify it
    prcp_dates = []
    prcp_totals = []

    from date, dailytotal in precipitation:
        prcp_dates.append(date)
        prcp_totals.append(dailytotal)

    prcp_dict = dict(zip(prcp_dates, prcp_totals))

    return jsonify(prcp_dict)
        

@app.route("/api/v1.0/stations")
def stations():
    # Create session (link) from Python to the DB
    session = Session(engine)

    """Return list of all weather stations in HI"""
    # Return list of active weather stations in HI
    sel = [measurement.station]
    active_stations = session.query(*sel).\
        group_by(measure.station).all()
    session.close()

    # Convert list of tuples into normal list
    all_stations = lsit(np.ravel(active_stations))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")













# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"


# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)
