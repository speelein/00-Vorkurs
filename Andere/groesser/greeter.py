import sys
print(sys.version)

v = [2, 3, 2, 4, 5]
c = [5, 6, 7, 8]
print(v)
print(c)
print(v + c)

k = v + c

print(k)

k = k + [14, "hallo"]  # Typen sind nicht eindeutig
