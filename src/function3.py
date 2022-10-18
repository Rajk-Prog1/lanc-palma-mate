input_list1 = [6, 8, 6]
input_list2 = [12, 45, 40]
start_of_the_course = [18, 0, 0]

def function3(input_list1: list, input_list2: list, start_of_the_course: list):
    msp_list1=input_list1[0]*3600+input_list1[1]*60+input_list1[2]
    msp_list2=input_list2[0]*3600+input_list2[1]*60+input_list2[2]
    msp_start_of_the_course=start_of_the_course[0]*3600+start_of_the_course[1]*60+start_of_the_course[2]
    elso=msp_start_of_the_course-msp_list1
    masodik=msp_start_of_the_course-msp_list2
    return(elso,masodik)
    pass