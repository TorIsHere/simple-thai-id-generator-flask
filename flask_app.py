# -*- coding: utf-8 -*-
from flask import Flask, render_template
import random

app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello from Flask!'

def generateID():
    thai_id = [random.randint(1,8) if i == 0 else random.randint(0,9)  for i in xrange(12)]
    mul_t_id = thai_id[:]
    count  = 13
    for i in xrange(len(mul_t_id)):
        mul_t_id[i] = mul_t_id[i] * count
        count -= 1
    last_digit = 11 - (sum(mul_t_id) % 11)
    thai_id.append(last_digit)
    return ''.join([ str(any_num) for any_num in thai_id])

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/generate', methods=['GET'])
def generate():
    return render_template('layout.html', id=generateID())
