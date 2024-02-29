from flask import Flask, render_template, request, redirect, url_for
import requests


app = Flask(__name__)
#get your api key from openweathermap api website by signing up
API_KEY = ''


@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    if 'use_location' in request.form:
        lat = request.form['lat']
        lon = request.form['lon']
        # Weather request based on latitude and longitude
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    else:
        # Weather request based on city name
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

    response = requests.get(url)
    weather_data = response.json()
    # Check if the city was found
    if 'cod' in weather_data and weather_data['cod'] != 200:
        return redirect('/not_found')
    return render_template('index2.html', weather_data=weather_data)


@app.route('/not_found')
def not_found():
    return render_template('not_found.html', back_url=url_for('weather'))


if __name__ == '__main__':
    app.run(debug=True)
