from flask import Flask, request
from mythril.mythril import MythrilAnalyzer
import json

app = Flask(__name__)

@app.route('/audit', methods=['POST'])
def audit_contract():
    # Get the contract code from the request body
    contract_code = request.json['contract_code']

    # Run the Mythril analysis on the contract code
    mythril = MythrilAnalyzer()
    issues = mythril.analyze_string(contract_code)

    # Convert the issues to a JSON string and return it in the response
    response_data = {'issues': issues}
    return json.dumps(response_data)

if __name__ == '__main__':
    app.run()
