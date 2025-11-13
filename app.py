from flask import Flask, render_template, request, flash
import requests

app = Flask(__name__)
app.secret_key = 'clavesecreta'

API = "https://trackapi.nutritionix.com/v2/natural/nutrients"
info = {
    "id": "85fe15db",
    "key": "210735866037a97066bc0cc093fcfb42", 
    "json": "application/json"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        id_comida  = request.form['search']
        response = requests.post(API, headers=info, json={"query": id_comida})
        if response.status_code == 200:
            result = response.json()
        else:
            flash('Verifica la clave o el Alimento', 'danger')
            
    return render_template('index.html', result=result)
if __name__ == "__main__":
    app.run(debug=True)