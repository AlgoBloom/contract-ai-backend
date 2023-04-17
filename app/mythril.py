from mythril.analysis.symbolic import SymExecWrapper
from mythril.analysis.security import fire_lasers
from mythril.laser.ethereum.state.global_state import GlobalState
from mythril.laser.ethereum.state.calldata import Calldata
from mythril.laser.ethereum.transaction.transaction_models import (
    ContractCreationTransaction,
    MessageCallTransaction,
)
from mythril.laser.ethereum.transaction.symbolic import execute_message_call
from mythril.laser.ethereum.util import get_current_instruction, get_call_parameters

class Mythril:
    def analyze_code(self, code):
        """
        Analyzes the given code and returns a list of issues.
        """
        # Convert hex code to binary
        bytecode = bytes.fromhex(code[2:])

        # Create symbolic execution wrapper
        sym = SymExecWrapper()

        # Create initial global state
        global_state = GlobalState(sym, None, None, None, None, None)

        # Create initial transaction
        transaction = ContractCreationTransaction(
            None, None, None, None, None, 0, bytecode, None
        )

        # Execute symbolic analysis
        try:
            fire_lasers(global_state, transaction)
        except Exception as e:
            return [{'error': str(e)}]

        # Collect results
        issues = []
        for node in global_state.nodes:
            if node.function_name != 'fallback':
                for issue in node.issues:
                    issues.append({
                        'title': issue.title,
                        'description': issue.description,
                        'swc_id': issue.swc_id,
                        'contract': issue.contract_name,
                        'function': node.function_name
                    })
        return issues
