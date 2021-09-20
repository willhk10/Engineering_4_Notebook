#Python Program 03
#made by William Keenan
#9.20.21

txt = input("Type in a random sentence")
split1 = txt.split(" ")
print(split1)

for i in split1:
    print("-")
    for b in i:
        print(b)
print("-")