from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
	name = StringField(label='Name', validators=[DataRequired()])
	email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
	message= TextAreaField(label='Message', validators=[DataRequired()])
	submit = SubmitField(label="Send")
