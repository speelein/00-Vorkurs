a = 34
w = 13
aaa = 2100

x = [3, a, 4, 5, 6, 'wort', 0, None, aaa, 'aaab']
for w in x:  # geht die Liste vom ersten bis letzten Element durch
    print(w)  # und gibt das defienierte w aus. w ist beliebig
print('jetzt wurden alle Elemente ausgegeben')
print('Ende')
print(x[1])
print(x[4])
print(x[-5])
print(x[0])
x[0] = -100
print(x[0])
x = x + [2, 3, 0]
print(x)
