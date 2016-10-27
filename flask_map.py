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

try:
  raw = open(CONFIG.mapboxfile)
  #flask.session["mapboxtoken"] = raw.readline().strip()
  #flask.session["mapboxid"] = raw.readline().strip()
except:
    app.logger.debug("Error while reading mapbox file")
    raise

###
# Pages
###

@app.route("/")
@app.route("/index")
@app.route("/map")
def index():
  app.logger.debug("Main page entry")

  raw = open(CONFIG.pins)
  flask.session["pins"] = pre.process(raw)
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
  raw = open(CONFIG.pins)
  reply = pre.process(raw)

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
