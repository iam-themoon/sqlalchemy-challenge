# sqlalchemy-challenge
Repository for HW 10 - SQLAlchemy!

# Climate Jupyter Notebook
* Create engine and session to connect to sqlite database
* Find the most recent recorded data by querying Measurement.date, descending
* Use that date to query all dates and precipitation data from twelve months prior
* Save the query results into a dataframe and drop any null values, then sort the dates
* Show the oldest and newest records
* Create a bar chart with this query dataframe, plotting the index (date) on the x-axis and precip values on the y
* Use .describe() to show overview stats on dataframe
* Create query .count() for total number of stations (by station ID)
* Create query to find most active stations 
* Using the most active station, query min, max, and avg temps
* Find previous 12 month data from most active station, then create a dataframe from the results
* Create a histogram of this data distribution
* Don't forget to close the session!

# App
* Create engine and session to connect to database
* Save references to the Measurement and Station tables 
* Create app with Flask
* (1) Create welcome page with brief info and href links to pages
* (2) Create precipitation page
    * Query all dates and prcp data
    * Create a dictionary of the date and prcp data
    * Append the dict values to list
    * Jsonify the list
* (3) Create stations page
    * Query all station, name, lat, lng, and elevation data
    * Create a dictionary of the queried data
    * Append the dict values to list
    * Jsonify the list
* (4) Create the tobs page
    * Find the oldest date by querying all dates and then sorting in desc order
    * Convert this date (currently string) to datetime y-m-d format
    * Create query_date variable from this
    * Query all dates and tobs where date is the same or after the query date
    * Create a dictionary of the queried data
    * Append the dict values to list
    * Jsonify the list
* (5) Create the start page
    * Query the min, avg, and max of all tobs data where the date is equal to or after the (to be inputted) start date
    * Create a dictionary of the queried data
    * Append the dict values to list
    * Jsonify the list
* (6) Create the start_end page
    * (Again) query the min, avg, and max of all tobs data where the date is equal to or after the (to be inputted) start date AND before the (to be inputted) end date
    * Create a dictionary of the queried data
    * Append the dict values to list
    * Jsonify the list
* Add this necessary if clause to make the app run:
    * "if __name__ == "__main__":
         app.run(debug = True)"

* And we're done! 
* Just for clarification, I went ahead and added a start date of 2014-01-01 and an end date of 2014-12-31
* These dates can be changed to render different results for the different range!

* Thanks!