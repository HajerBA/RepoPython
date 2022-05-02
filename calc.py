  
def add(num1, num2): 
    return num1 + num2 
  
def subtract(num1, num2): 
    return num1 - num2 
  
def multiply(num1, num2): 
    return num1 * num2 
  
def divide(num1, num2): 
    return num1 / num2 
  
print("choix de  l operation -\n" 
        "1. Addition\n" 
        "2. Soustraction\n" 
        "3. Multiplication\n" 
        "4. Division\n") 
  
  
select = int(input("Choisis une operation :")) 
  
number_1 = int(input("Entrez premier nombre: ")) 
number_2 = int(input("Entrez deuxieme nombre: ")) 
  
if select == 1: 
    print(number_1, "+", number_2, "=", 
                    add(number_1, number_2)) 
  
elif select == 2: 
    print(number_1, "-", number_2, "=", 
                    subtract(number_1, number_2)) 
  
elif select == 3: 
    print(number_1, "*", number_2, "=", 
                    multiply(number_1, number_2)) 
  
elif select == 4: 
    print(number_1, "/", number_2, "=", 
                    divide(number_1, number_2)) 
else: 
    print("Entree invalid") 