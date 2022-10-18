input_string = open('input_string.txt').read()[:-1]
import string
def function1(input_string: str) -> str:
    alphabet=list(string.ascii_lowercase)
    for i in len(input_string):
        for x in alphabet:
            if i==x:
                input_string.remove(i)
    return input_string