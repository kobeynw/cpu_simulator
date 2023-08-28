import time


"""
CPU ISA
bits 1-4: OPCODE
bits 5-8: FUNCTION
bits 9-16: REGISTER 1
bits 17-24: REGISTER 2
+------+------+--------------------------------------+
|  OP  | FUNC |             EXECUTION                |
| 0000 | 0001 | ADD two numbers from registers       |
| 0000 | 0010 | SUBTRACT two numbers from registers  |
| 0000 | 0011 | MULTIPLY two numbers from registers  |
| 0000 | 0100 | DIVIDE two numbers from registers    |
| 0000 | 0101 | REMAINDER of division from registers |
| 0001 | 0000 | STORE value to next register         |
| 0010 | 0000 | SHOW all register values             |
| 0011 | 0000 | END all executions                   |
+------+------+--------------------------------------+
"""

example = """
EXAMPLE CODE FOR INPUTS
+--------+----------+----------+---------------+-------------------------------------------+
| OPCODE |   FUNC   | ARGUMENT |   EXAMPLE     |              RESULT                       |
+--------+----------+----------+---------------+-------------------------------------------+
|  store |          | integer  | store 25      | integer stored in open register           |
|  show  |          | n/a      | show          | prints all occupied registers             |
|  end   |          | n/a      | end           | ends program                              |
|        |   add    | integers | add 15, 2     | adds nums from given registers, prints    |
|        |   sub    | integers | sub 25, 4     | subtracts nums from registers, prints     |
|        |   mult   | integers | mult 13, 90   | multiplies nums from registers, prints    |
|        |   div    | integers | div 16, 4     | divides nums from registers, prints       |
|        |   rem    | integers | rem 24, 10    | remainder of nums from registers, prints  |
+--------+----------+----------+-----------------------------------------------------------+

NOTE: You must first store a number to be able to access it later!
"""


def to_bin(num):
    bin_num = str(bin(int(num))[2:])
    if len(bin_num) > 8:
        print("\nInvalid input.\n")
        get_input()
    while len(bin_num) < 8:
        bin_num = '0' + bin_num
    return bin_num


def get_input():
    help = input("\nSee input options? Type 'y' or 'n': ")
    if help == 'y':
        print(f"Enter a valid input using an opcode/function and argument(s) where applicable. Examples of options below:\n{example}\n")
    command = input("Enter an input command with any arguments separated by spaces: ")
    values = command.split()
    op_func = values[0].strip(", ")
    bin1 = None
    bin2 = None
    if len(values) >= 2:
        if not values[1].strip(", ").isnumeric():
            print("\nInvalid input.\n")
            get_input()
        num1 = values[1].strip(", ")
        bin1 = to_bin(num1)
    if len(values) > 2:
        if len(values) > 3 or not values[2].strip(", ").isnumeric():
            print("\nInvalid input.\n")
            get_input()
        num2 = values[2].strip(", ")
        bin2 = to_bin(num2)

    code = ''
    if op_func == 'store':
        code += '00010000'
    elif op_func == 'show':
        code += '00100000'
    elif op_func == 'end':
        code += '00110000'
    elif op_func == 'add':
        code += '00000001'
    elif op_func == 'sub':
        code += '00000010'
    elif op_func == 'mult':
        code += '00000011'
    elif op_func == 'div':
        code += '00000100'
    elif op_func == 'rem':
        code += '00000101'
    else:
        print("\nInvalid input.\n")
        get_input()

    if bin1 and not bin2:
        code += '00000000' + bin1
    elif bin1 and bin2:
            code += bin1 + bin2
    else:
        code += '0000000000000000'
    time.sleep(1)
    print(f"\nEntering binary instruction: {code}")
    time.sleep(1)
    return code