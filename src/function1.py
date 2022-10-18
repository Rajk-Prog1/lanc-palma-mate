import string
input_string = open('input_string.txt').read()[:-1]

def function1(input_string: str) -> str:
    alphabet=list(string.ascii_lowercase)
    for i in input_string:
        for x in alphabet:
            if i==x:
                input_string=input_string.replace(i,"")
    return input_string

function1("edf56")