dictionary = {"lays     ": 50,
              "rice     ": 550,
              "biscuit  ": 100,
              "sugar    ": 120,
              "oil      ": 600,
              "soap     ": 80,
              "chocolate": 70,
              "cake     ": 40
              }
sum = 0
for i in dictionary.values():
    sum += i
    if i > 500:
        print("Product Price Greater Than 500 : ", i)
print("Sum Of All Product Prices : ", sum)
