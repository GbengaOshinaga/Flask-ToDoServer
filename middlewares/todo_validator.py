from functools import wraps

from flask import request


def validate_todo(function):

    @wraps(function)
    def decorated_function(*args, **kwargs):
        request_data = request.get_json()
        day = request_data.get('day')
        todo = request_data.get('todo')

        if not day:
            return { 
                'status': 'error',
                'message': '"day" is required'
            }, 400

        if not todo:
            return { 
                'status': 'error',
                'message': '"todo" is required'
            }, 400

        if not isinstance(day, str):
            return { 
                'status': 'error',
                'message': '"day" must be a string'
            }, 400

        if not isinstance(todo, str):
            return { 
                'status': 'error',
                'message': '"todo" must be a string'
            }, 400

        return function(*args, **kwargs)
    
    return decorated_function