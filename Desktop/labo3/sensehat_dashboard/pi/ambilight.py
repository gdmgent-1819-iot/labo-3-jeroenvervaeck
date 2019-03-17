# Import the libraries
from flask import Flask, jsonify, render_template, request
from sense_hat import SenseHat

# Create an instance of the sensehat
sense = SenseHat()

# Function for display on senseHat
def setColor(color_data):
  color = color_data.lstrip('#')
  rgb = tuple(int(color[i:i+2], 16) for i in (0, 2 ,4))
  for x in range(0,8):
    for y in range(0,8):
      sense.set_pixel(x, y, rgb)
      
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
