def test(arry):
    dict_arr={}
    for i in arry:
        if i in dict_arr:
            dict_arr[i]=dict_arr[i]+1
        else:
            dict_arr[i]=1
    return sorted(dict_arr.items(),key=lambda x:x[1],reverse=True)

print(test(["abc","aaa","ds",'aaa']))
