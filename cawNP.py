#Pythonで数独(caw用)

def encode(grid):
    "テキストから２次元配列のvaluesを作成する"
    values = []
    digits = "123456789"
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    grid_int = map(lambda x: int(x) if x != "." else 0, chars)

    count = 0
    row = []
    for i in grid_int:
        row.append(i)
        count += 1
        if count % 9 == 0: #行毎に分割
            values.append(row)
            row = []
    return values

def main(data):
  if solve(0, 0, data):
    #printtable(data)
    return data
  else:
    print ("This problem is unsolvable")

def solve(x, y, table):
  if x == 0 and y == 9:
    return True

  if table[y][x] == 0:
    for t in range(1, 10):
      table[y][x] = t
      if check(x, y, table):
        (nx, ny) = next(x, y)
        if solve(nx, ny, table):
          return True
    table[y][x] = 0
    return False
  else:
    (nx, ny) = next(x, y)
    if solve(nx, ny, table):
      return True

def next(x, y):
  x += 1
  if x > 8:
    x = 0
    y += 1
  return (x, y)

def check(x, y, table):
  return row(x, y, table) and column(x, y, table) and block(x, y, table)

def column(x, y, table):
  for yt in range(9):
    if yt != y:
      if table[y][x] == table[yt][x]:
        return False
  return True

def row(x, y, table):
  for xt in range(9):
    if xt != x:
      if table[y][x] == table[y][xt]:
        return False
  return True

def block(x, y, table):
  xbase = (x // 3) * 3
  ybase = (y // 3) * 3
  for yt in range(ybase, ybase + 3):
    for xt in range(xbase, xbase + 3):
      if xt != x and yt != y:
        if table[y][x] == table[yt][xt]:
          return False
  return True

def printtable(table):
  for y in range(9):
    for x in range(9):
      print (table[y][x])
    print ("")

def output(data):
    for i in range(9):
        for j in range (9):
            if data[i][j] == 0:
                print (".", end="")
            else:
                print (data[i][j], end="")

            if (j+1) % 3 == 0 and j < 8:
                print ("|", end="")
        print("")
        if (i+1) % 3 == 0 and i < 8:
            print ("-----------")
    print("")

if __name__ == "__main__":
    datafile = "data.txt"
    datalinefile = "dataline.txt"
    f = open(datalinefile)
    numbers = f.read()
    f.close
    values = encode(numbers)
    print("This is the problem!")
    output(values)
    main(values)
    print("This is the answer!")
    output(values)

    print("sucess!")
