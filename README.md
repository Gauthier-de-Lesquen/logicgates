## LogicGates
*A Python package to work with logic gates, truth tables, multiplexers, and more.*
### Description

#### Overview
> LogicGates simplified the use of logical operations in Python. (You can now do ```NAND(True, False, False)``` instead of ```not True and not False and not False```!!) 

#### What is on LogicGates?

> The package includes ready-to-use gate functions, truth table constants, multiplexers, demultiplexers, and utilities for evaluating gates dynamically.

### Documentation

#### I. logic gates functions:

* ```NOT(a, b, ...)``` is an equivalent of ```not``` basic keyword and takes a single argument.
* ```AND(a, b, ...)```is an equivalent of ```and```basic keyword, but takes as many arguments as you want.

* ```OR(a, b, ...)```is an equivalent of ```or```basic keyword, but takes as many arguments as you want.

**There are as much functions as logic gates; there is then also: NAND, NOR, XOR, and XNOR functions.** \
**All these functions accept:**
* booleans
* integers (1/0)

#### II. truth tables:
#### 1.*truth table constants:*
>there are two types of truth table constants:
* truth tables of list type
* truth tables of dictionnary type

To have the truth table of XOR gate for instance, you can get the list-type one with ```XOR_TRUTH_TABLE``` constant:
```Python
XOR_TRUTH_TABLE = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
```
To get the dictionnary-type one, use ```XOR_TRUTH_TABLE_DICT```:
```Python
XOR_TRUTH_TABLE_DICT = {
    (0, 0): 0,
    (0, 1): 1,
    (1, 0): 1,
    (1, 1): 0
}
```
#### 2.*truth tables display:*
you can display a truth table by using the function ```display_truth_table("XOR")```. \
**Output:**
```console
|    A    |    B    | A XOR B |
|---------+---------+---------|
|0        |0        |0        |
|0        |1        |1        |
|1        |0        |1        |
|1        |1        |0        |
```

**To help you finding the constant you need,the** ```TRUTH_TABLE``` **and** ```TRUTH_TABLE_DICT``` **constants contain all the truth table constants.**

#### III. Multiplexers and demultiplexers

you can use the 2 to 1 multiplexer integrated on the library using the function ```mux(I0, I1, S)```, and the 1 to 2 demultiplexer using ```demux(I, S)```.

#### IV. Find the output of a logic gate

to find the output of a logic gate, you can use the function ```eval_gate("OR", 0, 1)```. this example will return ```1``` for instance.