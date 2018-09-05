from flask import request
from flask_restplus import Resource

from main import api, db
from server.models import Todo
from middlewares.todo_validator import validate_todo
from utilities.model_serializers.TodoSchema import TodoSchema

@api.route('/todos')
class TodoResource(Resource):
    """
    Resource class for getting todos
    """

    def get(self):
        todos = Todo.query.all()
        todo_schema = TodoSchema(many=True)

        return {
            'status': 'success',
            'data': todo_schema.dump(todos).data
        }

    @validate_todo
    def post(self):
        request_data = request.get_json()
        todo_data = TodoSchema().load(request_data).data
        todo = Todo(**todo_data)

        db.session.add(todo)
        db.session.commit()
        
        return {
            'status': 'success',
            'data': TodoSchema().dump(todo).data
        }, 201
        

