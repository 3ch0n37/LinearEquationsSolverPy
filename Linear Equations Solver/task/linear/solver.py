i = input()
i = i.split(' ')
a = float(i[0])
b = float(i[1])
c = float(i[2])

i = input()
i = i.split(' ')
d = float(i[0])
e = float(i[1])
f = float(i[2])

y = (f - c * d / a)/(e - b * d / a)

x = (c - b * y) / a
print('{} {}'.format(x, y))
