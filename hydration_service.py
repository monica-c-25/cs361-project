# This microservice utilizes Flask as a backend to provide endpoints which enable communication with the hydration tracker.
# The functionalities include retrieving the current hydration count, incrementing cups, decrementing cups,
#      manually editing cups, and ressetting the cup count to 0. 
# The program will seamlessly integrate into the existing Tkinter application using APIS to call the aforementioned endpoints. 

from flask import Flask, request, jsonify
import time

app = Flask(__name__)


# serves as a global variable for number of cups consumed
num_cups = 0

# retrieves the current amount of cups consumed
@app.route('/hydration', methods=['GET'])
def get_cups():
    success = "Received request to get cups."
    print(success)
    time.sleep(1)
    return jsonify({'num_cups': num_cups})

# increments the cups consumed by 1
@app.route('/hydration/increment', methods=['POST'])
def increment_cups():
    success = "Received request to increment cups."
    print(success)
    time.sleep(1)
    global num_cups
    num_cups += 1
    return jsonify(num_cups)

# decrements the cups consumed by 1
@app.route('/hydration/decrement', methods=['POST'])
def decrement_cups():
    success = "Received request to decrement cups."
    print(success)
    time.sleep(1)
    global num_cups
    num_cups -= 1
    return jsonify(num_cups)

# edits the cups consumed based on manual entry
@app.route('/hydration/manual', methods=['POST'])
def manually_edit_cups():
    success = "Received requests to manually edit cups."
    print(success)
    time.sleep(1)
    global num_cups
    data = request.json
    num_cups = int(data)
    return jsonify(num_cups)

# resets the cups consumed to 0 
@app.route('/hydration/reset', methods=['POST'])
def reset_cups():
    success = "Received request to reset cups."
    print(success)
    time.sleep(1)
    global num_cups
    num_cups = 0
    return jsonify( num_cups)

if __name__ == '__main__':
    app.run(debug=True, port=5001)