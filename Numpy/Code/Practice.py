import numpy as np 


def Numpy_View():

    x1 = np.arange(1,10)
    x2 = np.random.randint(1,10,(9,))

    print(f"X1 - {x1}")
    print(f"X2 - {x2}")

    x3 = np.insert(x1,4,x2)

    print(f"X3 - {x3}")

    x1=np.delete(x1,1)
    
    print(f"X1 - {x1}")
 


if __name__ == "__main__":
    Numpy_View()