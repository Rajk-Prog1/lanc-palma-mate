def function2(input_string: str) -> str:
    for i in input_string:
        if i == "+":
            input_string = input_string.replace(i, ",")
        elif i == "-":
             input_string = input_string.replace(i, "#")
    return input_string