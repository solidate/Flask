from flask import Flask
app = Flask(__name__)
"""
Flask constructor takes the name of current module(__name__)
as argument.
"""
@app.route('/')
def hello_world():
    return 'Hello WOrld'

"""
The route() function of the Flask class is a decorator, which tells
the application which URL should call the associated function

There are two parameters:
    1. rule - The rule parameter represents URL binding with the funcion
    2. options - The options is a list of parameters to be forwarded to the underlying 
                Rule object.
"""

if __name__ == '__main__':
    app.run()