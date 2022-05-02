def multiplication(valeur, max=10):
    for i in range(1, max):
        print("{:3}".format(valeur * i), end="  ")
    print("{:3}".format(valeur * max))
multiplication(5)
