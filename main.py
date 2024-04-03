print("Hi, Hello! This is Harish, these are my Python Essential 1 - codes")


#1 printing arrow
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
print("    @")
print("   @ @")
print("  @   @")
print(" @     @")
print("@@@   @@@")
print("  @   @")
print("  @   @")
print("  @   @")
print("  @@@@@")



#2 octal and hexadecimal numbers
print(0o123)
print(0x123)


#3 Esacpe characters
print("I like \"Watching movies\"")
print('I like "Watching movies"')


#4 Using Code Strings two=',""
print('I\'m an employee.')
print("I'm an employee.")

#5 Boolean values
print(True > False)
print(True < False)

#5.1 LAB-code
print("\"I'm\"\n\"\"watching\"\"\n\"\"\"my code\"\"\"\n")

#6 Operators
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

#6.1 Division
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

#6.2 Integer division
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
print(6 // 4)
print(6. // 4)
print(-6 // 4)
print(6. // -4)

#6.3 Operators: remainder (modulo)
print(14 % 4)
print(14 // 4)
print(3 * 4)
print(12 % 4.5)

#6.4 Operators: addition
print(-4 + 4)
print(-4. + 8)

#6.5 The subtraction operator, unary and binary operators
print(-4 - 4)
print(4. - 8)
print(-1.1)
print(-5. - 5)

#6.6 Operators and their bindings
print(9 % 6 % 2)
#6.61 ex:
print(2 ** 2 ** 3)

#6.7 List of priorities-1.,2.+,-(unary),3.*, /, //, %,4.+,-(binary)
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
#6.71 Exercise1
print((2 ** 4), (2 * 4.), (2 * 4))
#6.72 Exercise2
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
#6.73 Exercise3
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
var = 1
print(var)

#7 Assigning a new value to an already existing variable
var = 1
print(var)
var = var + 1
print(var)

#8 mathematical problem
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c=", c)

#8.1 LAB code:
john = 3
marry = 5
adam = 6
total_apples = john + marry + adam
print("total_apples=", total_apples)
aigyf = 20
iyfyf = 10
poiu = 50
total_apples = aigyf * poiu + iyfyf
print("Total number of apples:", total_apples)

#8.2 LAB-CODE
kilometers = 12.25
miles = 7.38
miles_to_kilometers = 11.88
kilometers_to_miles = 7.61
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#9 The input() function
print("Tell me anything...")
anything = input()
print("Heyyyyy...", anything, "... hello!?")

#10 Type casting
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
#10.1 EX:
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypot = (leg_a ** 2 + leg_b ** 2) ** .5
print("Hypotenuse length is", hypot)

#11 String operators:
fnam = input("first name, please? ")
lnam = input("last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

#12 code
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#13 Type conversion: str()
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a ** 2 + leg_b ** 2) ** .5))

#14 Adding elements to a list
my_list = []
for i in range(5):
    my_list.append(i + 1)
print(my_list)
my_list = [10, 1, 8, 3, 5]
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)


#15 Sorting a  LIST
my_list = [8, 10, 6, 2, 4]
for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
my_list = [8, 10, 6, 2, 4]
swapped = True
while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)

#16 Inner life of lists
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

#17 The in and not in operators
my_list = [0, 3, 12, 8, 2]
print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#18 Lists - some simple programs
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]
print(largest)

#19 Lists - some simple programs
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
if found:
    print("Element found at index", i)
else:
    print("absent")

#20 Lists in lists: two-dimensional arrays - continued
EMPTY = "-"
ROOK = "ROOK"
board = []
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
print(board)

#21 Positional parameter passing
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

#22 Effects and results: lists and functions - continued
def strange_list_fun(n):
    strange_list = []
    for i in range(0, n):
        strange_list.insert(0, i)
    return strange_list
print(strange_list_fun(5))


print("Thank you!")