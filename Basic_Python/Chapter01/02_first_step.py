#Fibonacci Series:
# 两个元素的总和确定了下一个数
a,b=0,1
while b<1000:
    print(b,end=" ")
    a,b=b,a+b
print(" ")
# 这个例子介绍了几个新特征。
# 第一行包含了一个复合赋值：变量 a 和 b 同时得到新值 0 和 1。
# 最后一行再次使用了同样的方法，可以看到，右边的表达式会在赋值变动之前执行。
# 右边表达式的执行顺序是从左往右的。

i = 2 * 3
print('The value of i is',i)
