# cat 第一年算15岁 第二年算9岁 第三年以后每年算4岁
# dog 第一年算15岁 第二年算9岁 第三年以后每年算5岁

def human_years_cat_years_dog_years(human_years):
    return [human_years,15 +min(human_years-1,1)*9+max(human_years-2,0)*4,15 +min(human_years-1,1)*9+max(human_years-2,0)*5]
print(human_years_cat_years_dog_years(4))
