# Proj5-POIMap
This is a class project. It creates an interactive map with Leaflet, Mapbox, and OpenStreetMaps.

## Author
Jared Paeschke, paeschke@cs.uoregon.edu

## Overview
This project is built with Flask and Jinja2. It uses Leaflet for managing interation with
the map object. To display map tiles it uses Mapbox and OpenStreetMaps. When loaded a few
markers are automatically displayed. These markers are pulled from a data file containing
only the name of the location and the latitude and longitude.

With this data it uses Mapbox reverse Geocoding API to get street addresses for the
places of interest. In addition to the markers, the user make click the map to see the
coordinates of the clicked location. They may place a single marker, by shift+clicking, 
to indicate their own location as well.

## Installation
When writing and testing this program, the test machine was a Raspberry Pi 3 running
Raspian Jesse. This is the best sure fire way that the install will go smoothly. 
However you should have success as long as you have bash and make on your server machine

1. git clone https://github.com/mahananaka/proj5-poimap.git < install directory >
2. cd < install directory >
3. bash ./configure
4. You will need to create a secrets.py file in the main directory
  * On the first line place your Mapbox access token.
  * On the second line place your Mapbox project id.
5. make run

The program should then sit idle and wait for page requests. The default port is
port 5000, to get the main page surf to http://yourserverip:5000/ or if you're on 
the server machine http://localhost:5000/. To stop the program at any time use ctrl+c.

## Issues
If you do not properly configure the secrets.py file it will likely not work. I have it 
set to default a public key I use, but if people use it accessively I'll have to trash 
that key, which will make it no longer work for people who have not correctly created the
secrets.py file.

## Usage
Using this program is pretty straight forward if you have used any other interactive maps.
The basic functions like zooming and exploring the map are all the same. By default I have a
few comic book stores located around Eugene, Oregon as the points of interest. If you 
wish to change this just open ./data/poimarkers.txt and alter this file. The format is
self explanitory from looking at this file. You could also change where the the program
searches for POIs by altering the CONFIG.py file after it is created when you install.
