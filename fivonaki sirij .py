def fivo(n):
    if n <= 1:
        return n
    else:
        return fivo(n-1) + fivo(n-2)
n =10
print("fivo series...:")
for i in range(n):
        print(fivo(i), end=" ")