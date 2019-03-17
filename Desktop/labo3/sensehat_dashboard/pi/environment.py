# Import the libraries
from flask import Flask, jsonify, render_template, request

# Define the environment route
@app.route('/environment', methods=['GET'])
def environment():
  environment_obj = {
    'temperature': {
      'value': round(sense.get_temperature()),
      'unit': u'C'
    },
    'humidity': {
      'value': round(sense.get_humidity()),
      'unit': u'%'
    },
    'pressure': {
      'value': round(sense.get_pressure()),
      'unit': u'mbar'
    }
  }
  return render_template('environment.html', environment=environment_obj)
