from student_mark import *

def runner():
    num=int(input("enter the number of students need to added: "))     
    mark_list=add_marks(num)          
    print("output   ",mark_list)

    fname=input("enter the  name for search :")
    searched_name=serch_by_name(fname,mark_list)
    print("serached name   ",searched_name)

    del_name=input("enter the name to delete :")
    deleted_record=delete_record(mark_list,del_name)
    print("record delted  ",deleted_record)

    mark_with_condition_=mark_with_condition(mark_list,70)
    print(mark_with_condition_)

    desecending_order=decending_order_marks(mark_list)
    print(desecending_order)
    
runner()



