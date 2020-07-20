def add(num1,num2):
    return num1 + num2

def substract(num1,num2):
    return num1 - num2

def multi(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

a = ("Please select operation -\n"
        "1. Add\n"  
        "2. Subtract\n" 
        "3. Multiply\n" 
        "4. Divide\n")
print("\033[1m" + "Calculator" + "\033[0m")
print("\033[1m" + a + "\033[0m")
select = float(input("Select operations form 1, 2, 3, 4 :"))


num1 = float(input("First Number  :"))
num2 = float(input("Second Number :"))

if select == 1:
    print(f"Total : {num1}+{num2} = {add(num1,num2)}")

elif select == 2:
    print(f"Total :{num1} - {num2} = {substract(num1,num2)}")

elif select == 3:
    print(f"Total : {num1}*{num2} = {multi(num1,num2)}")
elif select == 4:
    print(f"Total : {num1}/{num2}= {divide(num1,num2)}")

elif select >=5:
    print("\033[1m" + "\n\tEror selection" + "\033[0m")


