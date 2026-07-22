"""
    Files 
        Open  -> file_name , mode (r,w,a,r+,w+,x) :- read,append,write,create
        r  - read total data
        w  - write data
        a  - append 
        r+ - read/write
        w+ - write/read -> overwrite the existing data
        Close

        writelines - list => str
        readline - only 1st line
        readlines - str => list
        seek - change position
        tell - current position
        

"""

print("--------Read-----------")
# read : total data
file_obj = open(file="demo_r.txt",mode="r")
data = file_obj.read()
print(data)
file_obj.close()


print("--------ReadLine-----------")

# readline : read only 1st line
file_obj = open(file="demo_r.txt",mode="r")
# read 1stline 
data_readline = file_obj.readline()
print(data_readline)
file_obj.close()



print("--------ReadLines-----------")

# readline : data convert into list of each line
file_obj = open(file="demo_r.txt",mode="r")
# read complete lines
data_readline = file_obj.readlines()
#read top 2 lines 
data_readline_2 = file_obj.readlines(2)
print(data_readline)
file_obj.close()
