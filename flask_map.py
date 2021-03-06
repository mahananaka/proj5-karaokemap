"""
Very simple Flask web site, with one page
displaying a map with pinned locations.
"""

import flask
from flask import render_template
from flask import request
from flask import url_for
from flask import jsonify # For AJAX transactions

import json
import logging

# Date handling 
import arrow # Replacement for datetime, based on moment.js
import datetime # But we still need time
from dateutil import tz  # For interpreting local times

# Our own module
import pre #processes the poimarkers.txt

###
# Globals
###
app = flask.Flask(__name__)
import CONFIG

import uuid
app.secret_key = str(uuid.uuid4())
app.debug=CONFIG.DEBUG
app.logger.setLevel(logging.DEBUG)


###
# Pages
###

@app.route("/")
@app.route("/index")
@app.route("/map")
def index():
  app.logger.debug("Main page entry")

  try:
    raw = open(CONFIG.mapboxfile)
    flask.session["mapboxtoken"] = raw.readline().strip() #save mapbox token and id to session variables
    flask.session["mapboxid"] = raw.readline().strip()
  except:
    app.logger.debug("Error reading secrets.py; using default values")
    flask.session["mapboxtoken"] = "pk.eyJ1IjoibWFoYW5hbmFrYSIsImEiOiJjaXVydzZkNnMwMDl3Mnpxamc2YnJqdTN6In0.QN32luonRpWSlq5zXruTYA"
    flask.session["mapboxid"] = "mahananaka.1p03d9fb"
    #raise
    
  return flask.render_template('map.html')

@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] =  flask.url_for("map")
    return flask.render_template('page_not_found.html'), 404


###############
#
# AJAX request handlers 
#   These return JSON, rather than rendering pages. 
#
###############
@app.route("/_get_pins", methods = ["POST"])
def set_start():
  """
  Get the places of interest for the map.
  """
  app.logger.debug("Got a JSON set_start post");

  reply = [ ]
  raw = open(CONFIG.pins)   #get points of interest from file
  reply = pre.process(raw)  #processing the file

  return jsonify(result=reply)  

 
#################
#
# Functions used within the templates
#
#################
@app.template_filter( 'fmtdate' )
def format_arrow_date( date ):
    try: 
        normal = arrow.get( date )
        return normal.format("ddd MM/DD/YYYY")
    except:
        return "(bad date)"

@app.template_filter( 'fmttime' )
def format_arrow_time( time ):
    try: 
        normal = arrow.get( date )
        return normal.format("hh:mm")
    except:
        return "(bad time)"



#############


if __name__ == "__main__":
    import uuid
    app.secret_key = str(uuid.uuid4())
    app.debug=CONFIG.DEBUG
    app.logger.setLevel(logging.DEBUG)
    app.run(port=CONFIG.PORT, host="0.0.0.0")
