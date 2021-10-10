value1 = int(input("Enter first value: ",))
value2 = int(input("Enter second value: ",))
value3 = str(input("choice operator: add,substract,multiply,divide,power : "))

if value3 == 'add':
    print(f"{value1} + {value2} =",value1+ value2)
elif value3 == 'substract':
    print(f"{value1} + {value2} =",value1 - value2)
elif value3 == 'multiply':
    print(f"{value1} * {value2} =",value1 * value2)
elif value3 == 'divide':
    print(f"{value1} / {value2} =",value1 / value2)
else:
    print(pow(value1,value2))
