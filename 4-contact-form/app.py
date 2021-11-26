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
# https://www.geeksforgeeks.org/create-contact-us-using-wtforms-in-flask/
########################################################################

from flask import Flask, render_template
from form import ContactForm

app = Flask(__name__)

# import secrets
# secrets.token_hex(16)
app.secret_key = '2283fe9058fe7c38c1ca61c55c5540ed'

@app.route("/", methods=["GET", "POST"])
def contact_form():

    form = ContactForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        return render_template('thank_you.html', name=name, email=email, message=message)

    return render_template('contact_form.html', form=form)

if __name__ == "__main__":
    app.run(host='::')
