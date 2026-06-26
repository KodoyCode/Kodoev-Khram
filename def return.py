def square(x):
    return x * x
nums = [1,2,3,4,5,6,7,8,9]
squares = list(map(lambda x: x % 2==0, nums))
print(f"{nums}, \n {squares}")