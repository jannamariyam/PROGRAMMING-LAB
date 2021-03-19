def isAmstrongnumber(num):
    cube_sum=0;number=num
    while num > 0:
        cube_sum = cube_sum + (num % 10)**3
        num = num // 10
    return cube_sum == number