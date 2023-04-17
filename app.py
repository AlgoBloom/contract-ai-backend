from flask import Flask, request
from mythril.mythril import Mythril

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Mythril backend API!"

@app.route('/audit', methods=['POST'])
def audit():
    contract_code = request.json['contract_code']
    analysis_report = Mythril.analyze(contract_code)
    return analysis_report.as_json()

if __name__ == '__main__':
    app.run()
