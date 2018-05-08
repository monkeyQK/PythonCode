#第一个字母一次，第二个字母二次，以此类推，首字母大写
def accum(s):
    n = 1
    s_new=''
    for i in s:
        s_new=s_new+i.upper()+i.lower()*(n-1)+"-"
        n= n +1
    return s_new[:-1:]

print(accum("ZpglnRxqenU"))
