from flask import Flask, jsonify, request
from mythril import Mythril

app = Flask(__name__)

@app.route('/audit', methods=['POST'])
def audit():
    code = request.json['code']
    myth = Mythril()
    issues = myth.analyze_code(code)
    return jsonify({'issues': issues})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
