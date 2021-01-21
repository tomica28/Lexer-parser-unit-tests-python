class Expression:
    def attribution(self, argument):
        text = "test string"
        intiger = 10
        floatNum = 1.1
        arg = argument.arg
        argument.arg(1, 2, 3)

    def logic(self, a, b, c, d):
        return a == 0 and b > 1 or c < 2 and d != 3 or a >= 4 and b <= 5 or c is not 7

    def arithmetic(self, x, y):
        a = x + y * x - y / x % y

