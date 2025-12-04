NOT_TRUTH_TABLE = [
    [0, 1],
    [1, 0]
]
AND_TRUTH_TABLE = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]
NAND_TRUTH_TABLE = [
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
OR_TRUTH_TABLE = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
NOR_TRUTH_TABLE = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0]
]
XOR_TRUTH_TABLE = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
XNOR_TRUTH_TABLE = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]


NOT_TRUTH_TABLE_DICT = {
    (0,): 1,
    (1,): 0
}
AND_TRUTH_TABLE_DICT = {
    (0, 0): 0,
    (0, 1): 0,
    (1, 0): 0,
    (1, 1): 1
}
NAND_TRUTH_TABLE_DICT = {
    (0, 0): 1,
    (0, 1): 1,
    (1, 0): 1,
    (1, 1): 0
}
OR_TRUTH_TABLE_DICT = {
    (0, 0): 0,
    (0, 1): 1,
    (1, 0): 1,
    (1, 1): 1
}
NOR_TRUTH_TABLE_DICT = {
    (0, 0): 1,
    (0, 1): 0,
    (1, 0): 0,
    (1, 1): 0
}
XOR_TRUTH_TABLE_DICT = {
    (0, 0): 0,
    (0, 1): 1,
    (1, 0): 1,
    (1, 1): 0
}
XNOR_TRUTH_TABLE_DICT = {
    (0, 0): 1,
    (0, 1): 0,
    (1, 0): 0,
    (1, 1): 1
}


TRUTH_TABLES = {
    "NOT": NOT_TRUTH_TABLE,
    "AND": AND_TRUTH_TABLE,
    "NAND": NAND_TRUTH_TABLE,
    "OR": OR_TRUTH_TABLE,
    "NOR": NOR_TRUTH_TABLE,
    "XOR": XOR_TRUTH_TABLE,
    "XNOR": XNOR_TRUTH_TABLE,
}

TRUTH_TABLES_DICT = {
    "NOT": NOT_TRUTH_TABLE_DICT,
    "AND": AND_TRUTH_TABLE_DICT,
    "NAND": NAND_TRUTH_TABLE_DICT,
    "OR": OR_TRUTH_TABLE_DICT,
    "NOR": NOR_TRUTH_TABLE_DICT,
    "XOR": XOR_TRUTH_TABLE_DICT,
    "XNOR": XNOR_TRUTH_TABLE_DICT,
}