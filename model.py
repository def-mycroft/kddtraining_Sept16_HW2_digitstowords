""" Uses inflect package to convert integers to text"""
import inflect

def convert_numberstring(input_string):
    """ Converts the input string to an integer and returns words"""
    try:
        input_number = int(input_string)
        number_engine = inflect.engine()
        return_value = number_engine.number_to_words(input_number)
    except ValueError:
        return_value = 'Please enter an integer'

    return return_value
