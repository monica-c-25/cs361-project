from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# global variable to store memos 
memos = []

@app.route('/memo/list', methods=['GET'])
def get_memos():
    global memos
    success = "Received request to get memos."
    print(success)
    return jsonify(memos)

@app.route('/memo/add', methods=['POST'])
def add_memo():
    global memos
    success = "Received request to add memo."
    print(success)
    time.sleep(1)
    data = request.json
    memo = data.get('memo')
    print(memo)
    if memo:
        memos.append(memo)
        return jsonify({"Success": "Memo Add"}), 200
    return jsonify({"Error": "Unable to Add memo"}), 400

@app.route('/memo/delete', methods=['POST'])
def delete_memo():
    global memos
    success = "Received request to delete memo."
    print(success)
    time.sleep(1)
    data = request.json
    memo_index = data.get('memo')
    memos.pop(memo_index)
    return jsonify({"Success": "Memo Removal"}), 200
0

if __name__ == '__main__':
    app.run(debug=True, port = 5000)