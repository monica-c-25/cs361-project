from flask import Flask, request, jsonify
import time

app = Flask(__name__)


# serves as a global variable for number of steps
num_steps = 0

# edits the cups consumed based on manual entry
@app.route('/step/edit', methods=['POST'])
def edit_steps():
    success = "Received requests to edit steps."
    print(success)
    time.sleep(1)
    global num_steps
    data = request.json
    num_steps = int(data)
    return jsonify(num_steps)

# resets the cups consumed to 0 
@app.route('/step/reset', methods=['POST'])
def reset_steps():
    success = "Received request to reset steps."
    print(success)
    time.sleep(1)
    global num_cups
    num_steps = 0
    return jsonify(num_steps)

if __name__ == '__main__':
    app.run(debug=True, port = 5002)