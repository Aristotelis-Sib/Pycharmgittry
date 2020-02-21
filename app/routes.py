from flask import request, jsonify
from app import app, db
from .models import User

baseURL = '/energy/api'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/energy/api/Admin/users', methods=['POST'])
def create_user():
    data = request.get_json()

    new_user = User(is_admin=False, username=data['username'], email=data['email'])

    new_user.hash_password(data['password'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'new user created'})


if __name__ == '__main__':
    app.run(debug=True)
