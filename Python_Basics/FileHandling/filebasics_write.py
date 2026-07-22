"""
mode = "w" - rewrites the entire exiting file
mode = "a" - append the exiting file with available data

"""

file_obj = open(file="demo_w.txt",mode="w")
# complete rewrite 
file_obj.write("Hello from write function")
file_obj.close()



file_obj = open(file="demo_w.txt",mode="a")
# complete rewrite 
file_obj.write("\nHello from append function")
file_obj.close()
