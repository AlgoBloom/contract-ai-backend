from mythril.analysis import AnalyzeContract
from mythril.exceptions import CompilerError, NoContractFoundError
from mythril.support.loader import read_sol_file, read_code
from mythril.solidity.soliditycontract import SolidityContract


class Mythril:
    @staticmethod
    def analyze(contract_code: str):
        contract = SolidityContract(code=contract_code)
        return AnalyzeContract(contract)

    @staticmethod
    def get_source_code(file_path: str) -> str:
        try:
            return read_sol_file(file_path)
        except FileNotFoundError:
            try:
                with open(file_path) as f:
                    return f.read()
            except FileNotFoundError:
                return None

    @staticmethod
    def get_bytecode(file_path: str) -> str:
        try:
            return read_code(file_path)
        except FileNotFoundError:
            return None
