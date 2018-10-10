for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3),end = " ")
    print(repr(x*x*x).rjust(4))
    # 字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
#另一个方法 zfill(), 它会在数字的左边填充 0，

