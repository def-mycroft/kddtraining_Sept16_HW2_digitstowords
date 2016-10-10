""" Renders the main page and manipulates the model and view.
"""
import model
from flask import Flask, jsonify, render_template, request

application = Flask(__name__)


@application.route('/')
def render_index():
    """ Renders the main page"""
    return render_template('index.html')


@application.route('/send/', methods=['GET'])
def return_output():
    """ Communication between the view and the model"""
    # Gets user input from the view.
    input_object = {'value': request.args.get('input_text')}
    # Calls the model function to convert the digit to text.
    input_object['value'] = model.convert_numberstring(input_object['value'])
    return jsonify(input_object)


if __name__ == '__main__':
    application.run(port=5000, debug=True)
