from flask import Flask, request, jsonify
import time
import random

app = Flask(__name__)

# holds all the workout ideas
workout_ideas = ["run for 30 minutes", "walk for 45 minutes", "take a yoga class", "take a pilates class", "stretch", "do 50 jumping jacks"]


@app.route('/workout', methods=['GET'])
def get_workout():
    success = "Received request to get workout."
    print(success)
    time.sleep(1)
    global workout_ideas
    workout = random.choice(workout_ideas)
    return jsonify(workout)

if __name__ == '__main__':
    app.run(debug=True, port = 5003)