string = ""
cursor = 0
a = 1
list_element = []
x = int(input())
for i in range(x):
    string = string + "1"
string = "@" + string + "@"
string = string.replace("1", "$")
for i in range(len(string)):
    list_element.append(string[i])

cursor = len(list_element) - 2
state = "q1"


def turing_machine(state, cursor, x):
    while a > 0:
        match state:
            case 'q1':
                if list_element[cursor] == "@":
                    list_element[cursor] = "@"
                    cursor = cursor + 1
                    state = "q7"
                else:
                    list_element[cursor] = "1"
                    cursor = cursor - 1
                    state = "q2"

            case 'q2':
                if list_element[cursor] == "$":
                    list_element[cursor] = "$"
                    cursor = cursor - 1
                    state = "q2"
                else:
                    list_element[cursor] = "@"
                    cursor = cursor + 1
                    state = "q3"

            case 'q3':
                if list_element[cursor] == "$":
                    list_element[cursor] = "@"
                    cursor = cursor + 1
                    state = "q4"
                else:
                    list_element[cursor] = "1"
                    cursor = cursor + 1
                    state = "q5"
            case 'q4':
                if list_element[cursor] == "$":
                    list_element[cursor] = "$"
                    cursor = cursor + 1
                    state = "q4"
                else:
                    list_element[cursor] = "1"
                    cursor = cursor - 1
                    state = "q1"
            case 'q5':
                if list_element[cursor] == "1":
                    list_element[cursor] = "1"
                    cursor = cursor - 1
                    state = "q6"
            case 'q6':
                print("x is odd")
                x = (x + 1) / 2
                return x
            case 'q7':
                print("x is even")
                x = x / 2
                return x


print(int(turing_machine("q1", cursor, x)))
# print(list_element)

