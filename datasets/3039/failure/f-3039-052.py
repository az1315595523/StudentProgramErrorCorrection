ls1 = eval(input())
a = max(ls1)
b = min(ls1)
for i in ls1:
    if i ==a:
        del(i)
else:
    pass
for i in ls1:
    if i ==b:
        del(i)
else:
    pass
print(ls1)        

    
