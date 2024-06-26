from flask import Flask,render_template

API=Flask(__name__)

@API.route('/errorhari')
def errorhari():
    return 'ErrorHari is good person'

@API.route('/hai')
def hai():
    return render_template('hai.html',Name='Priya',Age=23)
API.run(debug=True)
#API.run(debug=True,host='192.168.215.186',port=5000)