from flask import Flask, render_template

app = Flask(__name__)

# Dummy-Daten, diese müssen später durch Otelo-Daten ersetzt werden
data_usage = 7.3  # GB verbraucht
data_limit = 8  # GB limit

@app.route('/')
def index():
    remaining_data = data_limit - data_usage
    percentage = (data_usage / data_limit) * 100
    return render_template('index.html', data_usage=data_usage, data_limit=data_limit, remaining_data=remaining_data, percentage=percentage)

@app.route('/recharge')
def recharge():
    # Hier müsste der API-Aufruf zur Nachbuchung von Datenvolumen stehen
    return "Daten nachgebucht! (Dies ist nur eine Demo)"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
