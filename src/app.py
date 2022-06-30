from flask import Flask, jsonify
from flask import request
from flask import json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def todos_list():
    json_todos_list = jsonify(todos)
    return json_todos_list

@app.route('/todos', methods=['POST'])
def add_new_todo():
    global todos
    request_body = request.data
    descoded_object = json.loads(request_body)
    todos.append(descoded_object)
    json_todos_list = jsonify(todos)
    print("Incoming request with the following body", request_body)
    return json_todos_list, 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    global todos
    print("This is the position to delete: ",position)
    new_todos = []
    for index in range(len(todos)):
        if index != position:
            new_todos.append(todos[index])
    return jsonify(new_todos)

# Estas dos líneas siempre seben estar al final de tu archivo app.py.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
