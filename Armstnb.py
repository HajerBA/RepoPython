number = 165
temp = number
add_sum = 0
while temp!=0:
    k = temp%10
    add_sum +=k*k*k
    temp = temp//10
if add_sum==number:
    print('est nombre Armstrong')
else:
    print('Non Armstrong ')