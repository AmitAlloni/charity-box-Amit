from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class OrganizationForm(FlaskForm):
    name = StringField('שם', validators=[DataRequired()])
    street = StringField('רחוב', validators=[DataRequired()])
    city = StringField('עיר', validators=[DataRequired()])
    country = StringField('מדינה', validators=[DataRequired()])
    submit = SubmitField('צור אירגון')

class OrganizationUpdateForm(FlaskForm):
    name = StringField('שם', validators=[DataRequired()])
    address = StringField('כתובת', validators=[DataRequired()])
    submit = SubmitField('עדכן אירגון')
