from flask import Flask, jsonify, request, render_template
from salarycalc import SalaryCalculator

# Initialize Flask app
app = Flask(__name__)

# Initialize the SalaryCalculator instance
calculator = SalaryCalculator(hourly_rate=20)

@app.route('/')
def home():

    return "Welcome to salary calculator"

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

    # Get the JSON payload from the request
    data = request.get_json()

    # Validate the input
    if not data or 'hourly_rate' not in data:
        # Return error if input is missing or invalid
        return jsonify({"error": "Invalid input. Provide 'hourly_rate'"}), 400

    try:
        # Convert the input to a float and update the calculator
        new_rate = float(data['hourly_rate'])
        calculator.hourly_rate = new_rate  # Update hourly rate
        calculator.pay_per_second = new_rate / 3600  # Update pay per second

        # Return success message
        return jsonify({"message": f"Hourly rate updated to ${new_rate:.2f}"}), 200
    except ValueError:
        # Handle invalid numbers
        return jsonify({"error": "Invalid rate. Must be a number."}), 400

@app.route('/ui')
def ui():

    return render_template('index.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
