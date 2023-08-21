def change(L):
    print("Inside function - original id(L):", id(L))
    L.append(5)
    print("Inside function - modified id(L):", id(L))
    return L

l = [1, 2, 3, 4]
print("Outside function - original id(l):", id(l))
print("Original list:", l)

b = change(l[:])
print("Modified list:", b)
print("Outside function - modified id(l):", id(b))

print(f"orignal list: {l}")
