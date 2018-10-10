# Python 循环
# Python中的循环语句有 for 和 while。
# Python循环语句的控制结构图如下所示：
# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum += counter
#     counter = counter + 1

# print('Sum of 1 until %d: %d' % (n, sum))

# languages = ["C", "C++", "Perl", "Python"]
# for x in languages:
#     print(x)

# edibles = ["ham", "spam","eggs","nuts"]
# for food in edibles:
#     if food == 'spam':
#         print('No more spam please')
#         break
#     else:
#         print('I\'m so glad: No spam!')
#     print("Great, delicious " + food)
# print('Finally, I finished stuffig myself')
        
# for i in range(-1,20,2):
#     print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    if i == 2:
        break
    print(i,a[i])
