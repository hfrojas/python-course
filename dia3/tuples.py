mi_tuple = (1, 2, 3, 4)

print(type(mi_tuple))

t = ("fff",5,12.65)
print(t)
print(t[0])
print(t[-2])

#Esto genera error las tuplas son inmutables
#t[0] = 5


mi_tuple2 = (1, 2, 3, (10,20))
print(type(mi_tuple2))
print(mi_tuple2[0])
print(mi_tuple2[3][0])

mi_tuple= list(mi_tuple)
print(type(mi_tuple))

mi_tuple= tuple(mi_tuple)
print(type(mi_tuple))

t2 = (1,2,3,2,4)
x, y, z, k, m = t2
print(x, y, z)

print(len(t2))
print(t2.count(2))
print(t2.index(3))

