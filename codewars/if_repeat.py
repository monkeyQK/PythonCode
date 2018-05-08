string = 'Abcdef'


def test1(string):
    li = []
    for i in string:
        li.append(str.lower(i))
    if len(li) == len(set(li)):
        return True
    else:
        return False


def test2(string):
    return len(string) == len(set(str.lower(string)))


print(test1(string))

print(test2(string))
