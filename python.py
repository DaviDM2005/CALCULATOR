print("Hello there. That's CALCULATOR ")


int1 = input("First number:   ")
int2 = input("Second number:     ")
moqmedeba = input("Operation(+, -, *, /):    ")

if moqmedeba == "+":
    print(str(int(int1)+int(int2))) 
elif moqmedeba == "-":
    print(str(int(int1)-int(int2)))
elif moqmedeba == "*":
    print(str(int(int1)*int(int2)))
elif moqmedeba == "/":
    if int2 == "0":
        print("UNDEFINED")
    else:
        print(str(int(int1)/int(int2)))    
else:
    print("incorrect reference")