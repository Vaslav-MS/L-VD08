from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
    return render_template('index.html', weather=weather)

def get_weather(city):
    api_key = '90cce4dee05643c6b82233622242312'
    base_url = 'http://api.weatherapi.com/v1/current.json'
    complete_url = f'{base_url}?q={city}&key={api_key}&lang=ru'
    response = requests.get(complete_url)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)


