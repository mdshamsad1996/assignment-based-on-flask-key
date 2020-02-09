"""
Routes Module

"""
from flask import jsonify, request
from src import app
from src.validating_api_key import require_api_key
from src.Models.schedule_events import Events
from src.Models.user_module import User

user = User()
event = Events()


@app.route('/newuser')
@require_api_key
def register():
    """
    new user registeration
    """
    return jsonify({'message': user.create_user(request.data)})


@app.route('/getusers')
@require_api_key
def get_uers():
    """
    Get list of registered user
    """
    return jsonify({'message': user.get_user()})


@app.route('/login')
@require_api_key
def login():
    """
    Login for registered user     
    """
    return jsonify({'message': user.login_with_proper_credentials(request.data)})


@app.route('/create_event', methods=['POSt'])
@require_api_key
def create_event():
    """
    Create Schedule event
    """
    event_data = request.data
    return jsonify({'message': event.create_event(event_data)})


@app.route('/get_events', methods=['GET'])
@require_api_key
def getevent_details():
    """
    get list of event details
    """
    return jsonify({'message': event.read()})


@app.route('/update_event/<int:event_id>', methods=['PUT'])
@require_api_key
def update_events(event_id):

    """
    Update events
    """
    event_data = request.data
    return jsonify({'message': event.update_event_details(event_data, event_id)})


@app.route('/delete/<int:event_id>', methods=['Delete'])
@require_api_key
def delete_events(event_id):
    """
    Delete particular event for givent event_id
    """
    return jsonify({'message': event.delete_event_detils(event_id)})
