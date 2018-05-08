d = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def test():
    total_money = 0
    for i in range(1, 13):
        month_money = (2 * i + 0.01 + d[i] * 0.01) / 2 * d[i]
        total_money += month_money
        print("\t{:2f},{:2f}".format(month_money, total_money))
    print("\t{:2f}".format(total_money))




test()
