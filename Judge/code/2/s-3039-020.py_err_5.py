lst = eval(input())
a = max(lst)
b = min(lst)
lst1 = lst.copy()
for x in lst:
    if x == a:
        lst1.remove(x)
print(lst1)
