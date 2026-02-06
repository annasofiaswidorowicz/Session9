import random
#Write a function that adds 10 random functions
sum_num = 0
for i in range(10):
    num = random.randint(1, 100)
    sum_num += num
print(sum_num)