import cpu_memory
import cpu_input


'''
==================   SYSTEM DESIGN   ==================

- CPU functions:
    * ADD
    * SUBTRACT
    * MULTIPLY
    * DIVIDE
    * RAISE TO POWER
    * REMAINDER
    * STORE TO REGISTER

- Specs:
    * Inputs are 24 bits long, written as strings
      bits 1-4: OPCODE
      bits 5-8: FUNCTION
      bits 9-16: REGISTER 1
      bits 17-24: REGISTER 2
    * Only numbers up to 255
    * Division is floor only
    * main memory contains 256 'permanent' slots
    * register index stored in cache temporarily
    
+------+------+--------------------------------------+
|  OP  | FUNC | Execution                            |
| 0000 | 0001 | ADD two numbers from registers       |
| 0000 | 0010 | SUBTRACT two numbers from registers  |
| 0000 | 0011 | MULTIPLY two numbers from registers  |
| 0000 | 0100 | DIVIDE two numbers from registers    |
| 0000 | 0101 | REMAINDER of division from registers |
| 0001 | 0000 | STORE value to next register         |
| 0010 | 0000 | SHOW all register values             |
| 0011 | 0000 | END all executions                   |
+------+------+--------------------------------------+
'''


# CPU FUNCTIONS
memory = cpu_memory.Storage()


def add(num1, num2):
    result = num1 + num2
    print(f"Result: {result}")
    store(result)


def sub(num1, num2):
    result = num1 - num2
    print(f"Result: {result}")
    store(result)


def mult(num1, num2):
    result = num1 * num2
    print(f"Result: {result}")
    store(result)


def div(num1, num2):
    result = num1 // num2
    print(f"Result: {result}")
    store(result)


def rem(num1, num2):
    result = num1 % num2
    print(f"Result: {result}")
    store(result)


def store(num):
    if num in memory.cache:
        print("Value already stored in cache.")
    elif num not in memory.cache and 0 in memory.cache:
        memory.cache_insert(num)
    elif num in memory.main_memory:
        print("Value already store in main memory.")
    else:
        memory.main_insert(num)


def show():
    memory.print_main()


# CPU MAIN CODE
def welcome():
    name = input("Enter name: ")
    print(f"\nCalculator initialized for {name}.")
    print("Calculator specs: \n"
        "* Only input positive integers up to 255\n"
        "* Division is floor only")
    

def farewell():
    print("\nCalculator processes completed.")


def cpu_isa():
    while True:
        code = cpu_input.get_input()
        op = code[:4]
        func = code[4:8]
        reg1 = int(code[8:16], 2)
        reg2 = int(code[16:24], 2)
        num = int(code[8:24], 2)

        if op == '0011':
            return
        elif op == '0010':
            show()
        elif op == '0001':
            store(num)
        else:
            # Retrieve values from cache or from main memory
            if reg1 < 4:
                num1 = memory.cache[reg1]
            else:
                num1 = memory.main_memory[reg1]
            if reg2 < 4:
                num2 = memory.cache[reg2]
            else:
                num2 = memory.main_memory[reg2]

            # Execute function based on input
            if func == '0001':
                add(num1, num2)
            elif func == '0010':
                sub(num1, num2)
            elif func == '0011':
                mult(num1, num2)
            elif func == '0100':
                div(num1, num2)
            elif func == '0101':
                rem(num1, num2)
            else:
                print("Error: code inputed does not "
                      "match any existing processes.")


if __name__ == '__main__':
    welcome()
    cpu_isa()
    farewell()
