from flask import Flask, render_template, request
import sys
import math
#import request

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ?~@~X/?~@~Y URL is bound with home_page() function.
def home_page():
    return render_template('index.html')

# render inch2cm html
@app.route('/inch2cm')
def inch2cm():
    return render_template('inch2cm.html')

# inch2cm program
@app.route('/inch2cm_action')
def inch2cm_action():
    result = ''
    inches = 0.0
    try:
        inches = float(request.args.get('inches'))
        result += 'Inches = ' + str(inches) + ', Centimeters = ' + str(inches * 2.54)
    except ValueError:
        result += 'You did not enter a number.'
    return result

# render ft2m.html
@app.route('/ft2m')
def ft2m():
    return render_template('ft2m.html')

# ft2m program
@app.route('/ft2m_action')
def ft2m_action():
    result = ''
    ft = 0.0
    try:
        ft = float(request.args.get('ft'))
        result += 'Feet = ' + str(ft) + ', Meters = ' + str(ft / 3.281)
    except ValueError:
        result += 'You did not enter a number.'
    return result

# render mi2km.html
@app.route('/mi2km')
def mi2km():
    return render_template('mi2km.html')

# mi2km program
@app.route('/mi2km_action')
def mi2km_action():
    result = ''
    mi = 0.0
    try:
        mi = float(request.args.get('mi'))
        result += 'Miles = ' + str(mi) + ', Kilometers = ' + str(mi * 1.609)
    except ValueError:
        result += 'You did not enter a number.'
    return result

# render factorial html
@app.route('/factorial')
def factorial():
    return render_template('factorial.html')

# inch2cm program
@app.route('/factorial_action')
def factorial_action():
    result = ''
    try:
        num = int(request.args.get('num'))
        if num < 0:
            raise ValueError
        result += 'factorial(' + str(num) + ') = ' + str(factorial_core(num))
    except ValueError:
        result += 'You did not enter a non-negative integer. The factorial of a negative integer is a complex number, but it is not implemented, yet.'
    return result

# factorial core function
def factorial_core(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial_core(num - 1)

# render statapp html
@app.route('/statapp')
def statapp():
    return render_template('statapp.html')

# statapp action program
@app.route('/statapp_action')
def statapp_action():
    result = ''
    try:
        num_list = str(request.args.get('num_list')).split(',')
        for i in range(len(num_list)):
            num_list[i] = float(num_list[i])
        mean = sum(num_list) / len(num_list)
        res = sum((x - mean) ** 2 for x in num_list) / len(num_list)
        sd = math.sqrt(res)
        median = median_calculation(num_list)
        result += 'The mean of the list is: ' + str(mean) + '<br>'
        result += 'The variance of the list is: ' + str(res) + '<br>'
        result += 'The standard deviation is: ' + str(sd) + '<br>'
        result += 'The median is: ' + str(median) + '<br>'
        result += horizontal_histogram(num_list, 0, 100, 10)
    except ValueError:
        result += 'At least one of the input is not a number.'
    return result

## median
#  param: num_list: a list of numbers
#  return: the median of the list
def median_calculation(num_list):
    if len(num_list) % 2 == 1:
        return num_list[int(len(num_list) / 2)]
    return (num_list[int(len(num_list) / 2)] + num_list[int(len(num_list) / 2) - 1]) / 2

## method horizontal_histogram draws a histogram according to scores,
#  with bounds from lb to ub
#  returns a formatted string
def horizontal_histogram(scores, lb, ub, inc):
    scores.sort()
    j = 0
    i = lb
    result = ''
    while (i <= ub):
        count = 0
        while (j < len(scores) and scores[j] >= i and scores[j] < i + inc):
            count=count+1
            j = j + 1
        result += '{:0>3}'.format(i) + ' ' + '*' * count + '<br>'
        i = i + inc
    return result

# main driver function
if __name__ == '__main__':

        # run() method of Flask class runs the application
        # on the local development server.
        app.run(host='127.0.0.1', port=5090)

