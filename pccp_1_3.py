
input_list = [[1,1],[3,7],[3,15]]
beans = {1:"RR",2:"Rr",3:"Rr",4:"rr"}

def search(order, length) :
    global beans
    total_beans = 4**(length - 1)

    if total_beans == 1 and order == 1 :
        print("Rr")
        return 

    if total_beans <= 4 :
        print(beans[order])
        return
    
    if order <= total_beans / 4 :
        print("RR")
        return
    elif order > total_beans * 3 / 4 :
        print("rr")
        return
    elif order <= total_beans / 2 :

        search(order - total_beans/4, length - 1)
        return
    else :
        search(order - total_beans/2, length - 1)
        return
           
for input_val in input_list :
    search(input_val[1], input_val[0] )
