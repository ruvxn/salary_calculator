from flask import Flask, jsonify, request, render_template
from flask_cors import CORS  # Import CORS
from salarycalc import SalaryCalculator

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize the SalaryCalculator instance
calculator = SalaryCalculator(hourly_rate=20)

@app.route('/')
def home():
    return "Welcome to Salary Calculator"

@app.route('/start', methods=['POST'])
def start():
    if not calculator.is_running:
        calculator.start_shift()
        return jsonify({"message": "Shift started"}), 200
    else:
        return jsonify({"error": "Shift has already been started"}), 400

@app.route('/stop', methods=['POST'])
def stop():
    if calculator.is_running:
        calculator.stop_shift()
        return jsonify({
            "message": f"Shift ended. Total earnings for shift: ${calculator.earned_salary:.2f}"
        }), 200
    else:
        return jsonify({"error": "No shift is in progress"}), 400

@app.route('/get_salary', methods=['GET'])
def get_salary():
    salary = calculator.get_earned_salary()
    return jsonify({"earned_salary": f"${salary:.2f}"}), 200

@app.route('/reset', methods=['POST'])
def reset():
    calculator.reset()
    return jsonify({"message": "Calculator has been reset"}), 200

@app.route('/set_rate', methods=['POST'])
def set_rate():
    data = request.get_json()

    if not data or 'hourly_rate' not in data:
        return jsonify({"error": "Invalid input. Provide 'hourly_rate'"}), 400

    try:
        new_rate = float(data['hourly_rate'])
        calculator.hourly_rate = new_rate
        calculator.pay_per_second = new_rate / 3600
        return jsonify({"message": f"Hourly rate updated to ${new_rate:.2f}"}), 200
    except ValueError:
        return jsonify({"error": "Invalid rate. Must be a number."}), 400

@app.route('/ui')
def ui():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Allow access from other devices
