ls1 = eval(input())
a = min(ls1)
a = min(ls1)
ls2 = ls1.copy()
for i in ls1:
    if i == a:
        ls2.remove(i)
print(ls2)
