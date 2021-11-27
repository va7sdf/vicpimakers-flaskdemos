########################################################################
# "Hello World!" Flask example.
#
# This script was written for the Victoria Raspberry PiMakers And Others
# Meetup Group presentation on November 27, 2021.
#
# Gordon M. Celesta
# gordo@sdf.lonestar.org
#
# FURTHER READING
#
# Application (flask) object:
# https://flask.palletsprojects.com/en/2.0.x/api/#application-object
#
# Route decorator:
# https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask.route
#
# Run method:
# https://flask.palletsprojects.com/en/2.0.x/api/#flask.Flask.run
#
########################################################################

# import required modules
from flask import Flask

# instantiate flask object ()
app = Flask(__name__)

# register a URL with a function
@app.route("/")         # route decorator
def hello():            # view function
    message = "<p>Hello World!</p>"
    return message      # return message to browser

if __name__ == "__main__":

    # run the app [do not use run() in a porduction setting]
    app.run(host='::')  # host='::' for IPv6 and IPv4 support
