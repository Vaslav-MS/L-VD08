from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    quote = get_quotes()
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
    return render_template('index.html', weather=weather, quote=quote)

def get_weather(city):
    api_key = '90cce4dee05643c6b82233622242312'
    base_url = 'http://api.weatherapi.com/v1/current.json'
    complete_url = f'{base_url}?q={city}&key={api_key}&lang=ru'
    response = requests.get(complete_url)
    return response.json()

def get_quotes():
#    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response_q = requests.get('https://api.api-ninjas.com/v1/quotes', headers={'X-Api-Key': '/SyW0tSCbsdd1mxrH/xtLg==SyuA9xRyzbnBuN8k'})
    if response_q.status_code == requests.codes.ok:
        return response_q.json()

if __name__ == '__main__':
    app.run(debug=True)

