from .consts import TRUTH_TABLES_DICT

def eval_gate(gate_name, *inputs):
    table = TRUTH_TABLES_DICT[gate_name.upper()]
    return table[tuple(inputs)]