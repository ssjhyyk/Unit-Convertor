from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

mile_to_km = 1.60934
km_to_mile = 0.621371


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    distance = float(request.form['distance'])
    unit = request.form['unit']

    if unit == 'miles':
        converted_distance = distance * mile_to_km
        converted_unit = 'kilometers'

    elif unit == 'kilometers':
        converted_distance = distance * km_to_mile
        converted_unit = 'miles'

    else:
        return render_template['error.html']

    return render_template('result.html', distance=distance, unit=unit, converted_distance=converted_distance, converted_unit=converted_unit)
