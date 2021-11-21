########################################################################
# Simple web page example
#
# This script was written for the Victoria Raspberry PiMakers And Others
# Meetup Group presentation on November 27, 2021.
#
# Gordon M. Celesta
# gordo@sdf.lonestar.org
#
# FURTHER READING
#
# render_template()
# https://flask.palletsprojects.com/en/2.0.x/api/#flask.render_template
#
########################################################################

import random
from flask import Flask, render_template

app = Flask(__name__)

def door_status():
    """
    Return a random door status
    """
    return random.choice(['open','closed'])

def pond_temp():
    """
    Return a random water temperature in Fahrenheit between 35 °F
    and 85 °F (the survivable range for koi fish) and its equivalent
    in celsius
    """
    temp_f = round(random.uniform(35,85),1)
    temp_c = round((temp_f - 32) / 1.8, 1)
    return (temp_f, temp_c)

@app.route("/")
def house_info():
    # render the template and with the optional
    # context (variable, value pair(s))
    return render_template('house_info.html',
                           front_door = door_status(),
                           back_door = door_status(),
                           garage_door = door_status(),
                           pond_temp = pond_temp())

if __name__ == "__main__":
    app.run(host='::')
