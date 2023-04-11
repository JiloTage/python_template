import numpy as np


def fizzbuzz(num: int):
    """
    fizzbuzzを解く関数.
    1~numまで順に数字をprint文で表示する。ただし、
    ・数字が３の倍数の時には数字の代わりに「Fizz!」
    ・数字が５の倍数の時には数字の代わりに「Buzz!」
    ・数字が３の倍数かつ５の倍数の時には代わりに「Fizz Buzz!」
    を出力する。

    Args:
        num (int): fizzbuzzを実行する数.
    """

    def func(x):
        func_dict = {0: x, 1: "Fizz!", 10: "Buzz!", 11: "Fizz Buzz!"}
        return func_dict[int(x % 3 == 0) + 10 * int(x % 5 == 0)]

    # np_func = np.vectorize(func)

    aranges = np.arange(1, num + 1)
    # aranges = np_func(aranges)

    for a in aranges:
        print(func(a))
    # return func_dict[binary_flag]


if __name__ == "__main__":
    fizzbuzz(int(input()))