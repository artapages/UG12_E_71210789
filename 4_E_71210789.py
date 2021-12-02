# Test Case 1

# 5 deret bilangan yang tertera pada soal
mark = [3, 20, 100, -35, 50]

#proses
def nilai1(deret):
  nilai_max = deret[0]
  for nilai in deret:
    if nilai > nilai_max:
      nilai_max = nilai

  return nilai_max

def nilai2(deret):
  nilai_min = deret[0]
  for nilai in deret:
    if nilai < nilai_min:
      nilai_min = nilai

  return nilai_min

# tampilan
print("Test Case 1")
print(mark)
print('Nilai terbesar:', nilai1(mark))
print('Nilai terkecil:', nilai2(mark))

print(" ")

# Test Case 2

# 5 deret bilangan yang tertera pada soal
winwin = [3, 20, 90, 35, 75]

#proses
def nilai1(deret):
  nilai_max = deret[0]
  for nilai in deret:
    if nilai > nilai_max:
      nilai_max = nilai

  return nilai_max

def nilai2(deret):
  nilai_min = deret[0]
  for nilai in deret:
    if nilai < nilai_min:
      nilai_min = nilai

  return nilai_min

# tampilan
print("Test Case 2")
print(winwin)
print('Nilai terbesar:', nilai1(winwin))
print('Nilai terkecil:', nilai2(winwin))