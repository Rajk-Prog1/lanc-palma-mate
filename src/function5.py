def function5(input_string: str, input_int: int) -> str:
    input_string2=""
    for i in range(len(input_string)):
        if i%input_int==0:
            input_string2+=input_string[i]
    return input_string2
