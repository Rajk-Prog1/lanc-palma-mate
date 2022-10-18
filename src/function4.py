def function4(input_int1: int, input_int2: int) -> int:
    kisebbik=min(input_int1,input_int2)
    for i in range(kisebbik):
        if (input_int1%kisebbik==0 and input_int2%kisebbik==0):
            lko=kisebbik
        else:
            kisebbik=kisebbik-1
    return lko
