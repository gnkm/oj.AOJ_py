"""ネストされた Dict の値の更新処理の確認

b = '1', f = '1', r = '3', v = 8 として、下記式を実行すると
r = '3' の値がすべて更新されてしまう。

```
residents[b][f][r] += v
```

この原因を探す。
"""

import icecream
debug = icecream.ic

residents = {'1': {'1': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}, '2': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}, '3': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}}, '2': {'1': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}, '2': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}, '3': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}}, '3': {'1': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}, '2': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}, '3': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}}, '4': {'1': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}, '2': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}, '3': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}}}

def main():
    # case1()
    # case2()
    # case3()
    # case4()
    case5()


def case1():
    d1 = {
        '1': 100,
        '2': 200,
    }
    debug(d1)

    d1['1'] += 1
    debug(d1)

def case2():
    d2 = {
        str(i): {
            str(j): 0 for j in range(1, 3)
        } for i in range(1, 5)
    }
    debug(d2)
    # ic| d2: {'1': {'1': 0, '2': 0},
    #          '2': {'1': 0, '2': 0},
    #          '3': {'1': 0, '2': 0},
    #          '4': {'1': 0, '2': 0}}

    d2['1']['1'] += 10
    debug(d2)
    # ic| d2: {'1': {'1': 10, '2': 0},
    #          '2': {'1': 0, '2': 0},
    #          '3': {'1': 0, '2': 0},
    #          '4': {'1': 0, '2': 0}}

def case3():
    d3 = {
        str(i): {
            str(j): {
                str(k): 0 for k in range(1, 7)
            } for j in range(1, 5)
        } for i in range(1, 3)
    }
    debug(d3)
    # ic| d3: {'1': {'1': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0},
    #                '2': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0},
    #                '3': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0},
    #                '4': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}},
    #          '2': {'1': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0},
    #                '2': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0},
    #                '3': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0},
    #                '4': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}}}

    d3['1']['2']['1'] += 10
    debug(d3)
    # ic| d3: {'1': {'1': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0},
    #                '2': {'1': 10, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0},
    #                '3': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0},
    #                '4': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}},
    #          '2': {'1': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0},
    #                '2': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0},
    #                '3': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0},
    #                '4': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}}}


def case4():
    residents['1']['1']['3'] += 8
    debug(residents)  # => OK


def case5():
    b = '1'
    f = '1'
    r = '3'
    v = 8
    residents[b][f][r] += v
    debug(residents)  # => OK


if __name__ == '__main__':
    main()
