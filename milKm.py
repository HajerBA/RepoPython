def ConvertKm(nbvar,klmvar):
    nbvar=float(input("donner la valeur à convertir"))
    
    klmvar = nbvar *1.621371
    print ('%0.3f miles est egale a %0.3f km' %(nbvar,klmvar))
    
    

ConvertKm(2,3)