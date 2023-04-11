# 解答なので、配布ミスに注意
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
    for i in range(1, num + 1):

        if i % 15 == 0:
            print("Fizz Buzz!")
        elif i % 3 == 0:
            print("Fizz!")
        elif i % 5 == 0:
            print("Buzz!")
        else:
            print(i)

