'''
Sensehat Dashboard
--------------------
Author: Jeroenvervaeck
Modified: 03-12-2019
--------------------
Installation:
sudo pip3 -U Flask
Docs: http://flask.pocoo.org/docs/1.0/
'''
# Import the libraries
from flask import Flask, jsonify, render_template, request
from sense_hat import SenseHat

# Create an instance of flask
app = Flask(__name__)

# Create an instance of the sensehat
sense = SenseHat()

def setColor(color_data):
  color = color_data.lstrip('#')
  rgb = tuple(int(color[i:i+2], 16) for i in (0, 2 ,4))
  for x in range(0,8):
    for y in range(0,8):
      sense.set_pixel(x, y, rgb)

# Define the root route
@app.route('/')
def index():
  return 'Look the flask server is running'

# Define the my_ip route
@app.route('/my_ip', methods=['GET'])
def my_ip():
  return jsonify({
    'ip': request.remote_addr
  }), 200

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

# Define the COLORPICKER route
@app.route('/colorpicker', methods=['GET','POST'])
def colorpicker():
  if request.method == 'POST':
    color_obj = {
      'value': request.form['colorField']
      }
    color_data = color_obj['value']
    setColor(color_data)
    print(color_obj)
  else:
    color_obj = {
      'value': '#ffffff'
    }
    print(color_obj)
    


  return render_template('colorpicker.html', colorpicker=color_obj)

# Main method for Flask server
if __name__ == '__main__':
  app.run(host = '192.168.0.157', port = 8080, debug = True)
