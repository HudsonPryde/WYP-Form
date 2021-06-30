from flask import Flask, jsonify, request
from flask_cors import CORS
import re


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/validation', methods=['POST'])
def validate():
    response_object = {}
    post_data = request.get_json()
    DATA = {
        'first_name': post_data.get('first_name'),
        'last_name': post_data.get('last_name'),
        'email': post_data.get('email'),
        'address': post_data.get('address'),
        'phone_number': post_data.get('phone_num'),
        'city': post_data.get('city'),
        'country': post_data.get('country'),
        'province': post_data.get('province'),
        }

    # check all the inputs that must be < 255 chars
    max_char = ['first_name', 'last_name', 'address', 'city']
    for name in max_char:
        if len(DATA[name]) > 255:
            response_object[name] = False
        else:
            response_object[name] = True

    # check email
    if not re.match('([\w\.-]+)@([\w\.-]+)', DATA['email']):
        response_object['email'] = False
    else:
        response_object['email'] = True

    # check phone #
    if not re.match('[0-9]{3}-[0-9]{3}-[0-9]{4}', DATA['phone_number']):
        response_object['phone_num'] = False
    else:
        response_object['phone_num'] = True

    return jsonify(response_object)


if __name__ == '__main__':
    app.run()