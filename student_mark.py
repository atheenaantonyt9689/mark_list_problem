def add_marks(num):
    mark_list=[]    
    for i in range(0,num):
        inner_side=[]       
        name=input("enter the name of students need to added: ")
        marks=int(input("enter the marks of students need to added: ") )
        inner_side.append(name)
        inner_side.append(marks)    
        mark_list.append(inner_side)
    return mark_list

#get the mark of a student given her name, from this string
def serch_by_name(fname,mark_list):
    for i in mark_list: 

        if i[0]==fname:            
            return i[1]
        else:
            return False #"{} not found in the record ".format(fname)


def delete_record(mark_list,del_name):
    for i in mark_list:
        if i[0]==del_name:
            mark_list.remove(i)
            return mark_list
        else:
            return False  #"{} not found in the record ".format(del_name) 

def mark_with_condition(mark_list,mark): 
      
    for i in mark_list:               
        if i[1]>=mark:
            return i[0]
        else:
            return False


def decending_order_marks(mark_list):
    for i in mark_list:
        sorted_=sorted(mark_list)
        return sorted_    

def filter_with_firstname():
        pass