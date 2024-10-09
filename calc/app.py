# Put your app in here.
from flask import Flask,request
from operations import add,sub,mult,div

app = Flask(__name__)

'''Returns A added to B.'''
@app.route('/add')
def add_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{add(a,b)}'

'''Returns A subtracted from B.'''
@app.route('/sub')
def sub_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{sub(a,b)}'

'''Returns A multiplied by B.'''
@app.route('/mult')
def mult_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{mult(a,b)}'

'''Returns A divided by B.'''
@app.route('/div')
def div_nums():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{div(a,b)}'

'''Stores operations'''
operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

'''Returns answer depending on operation(add,sub,mult,div) from operations dict with A and B.'''
@app.route('/math/<operation>')
def math_ops(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])

    return f'{operations[operation](a,b)}'
