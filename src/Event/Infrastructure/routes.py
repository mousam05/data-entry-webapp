from flask import render_template, Blueprint
from src.Event.Application.Event import Event


event_blueprint = Blueprint('event', __name__)
@event_blueprint.route('/', methods=['GET'])
def event():
    event_instance = Event()
    events_list = event_instance.event_list_collection()
    return render_template('event.html', events=events_list)