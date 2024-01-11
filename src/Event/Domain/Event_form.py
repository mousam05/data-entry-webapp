from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.fields.numeric import IntegerField


class Event_form(Form):
    title = StringField('Title', [validators.Length(min=4, max=500)])
    startDate = IntegerField('Start date', [validators.NumberRange(min=1)])
    imgURL = StringField('Image url', [validators.Length(min=1)])
    endDate = IntegerField('End date', [validators.NumberRange(min=1)])
    country = StringField('Country', [validators.Length(min=4, max=500)])
    city = StringField('City', [validators.Length(min=4, max=500)])
    summary = StringField('Summary', [validators.Length(min=4, max=5000)])
    description = StringField('Description', [validators.Length(min=4, max=5000)])
    originalDescription = StringField('Original description', [validators.Length(min=4, max=5000)])
    address = StringField('Address', [validators.Length(min=4, max=500)])
    ticketURL = StringField('Ticket url', [validators.Length(min=4, max=5000)])
    url = StringField('url', [validators.Length(min=4, max=5000)])
    province = StringField('province', [validators.Length(min=4, max=500)])

