numbers = ["0","1","2","3","4","5","6","7","8","9"]

file = "/home/ec2-user/environment/sudoku/test.txt"


with open(file, mode='w') as f:
    for i in range(len(numbers)):
        f.write(numbers[i])

with open(file) as f:
    print(f.read())