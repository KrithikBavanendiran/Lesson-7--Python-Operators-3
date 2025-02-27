x=5
if(type(x)is not int):
    print("True")
else:
    print("False")

x=5.7
if(type(x)is not float):
    print("True")
else:
    print("False")

x=20
y=20
if (x is y):
    print("x&y have the SAME identity")
y=30
if(x is not y):
    print("x&y have a DIFFERENT identity")