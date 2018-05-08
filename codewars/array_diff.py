def array_diff(a, b):
    for i in b:
        for j in range(len(a)):
            if i in a:
                a.remove(i)
    return a

def array_diff_god(a,b):
    return [x for x in a if x not in b]

print(array_diff([-10, -8, -3, -10, -17, 20, 4],[13]))

print(array_diff_god([-10, -8, -3, -10, -17, 20, 4],[13]))
