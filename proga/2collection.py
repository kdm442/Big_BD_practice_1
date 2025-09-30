# fruits = ["apple" , "orange","coconut", "banana"]
# vegetables = ["calery","carrots","potapos"]
# meats = ["chiken","fish","beef"]

# groceries = [fruits,vegetables,meats]

# for collection in groceries:
#     for food in collection:
#         print(food,end=" ")
#     print()

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))
for row in num_pad:
    for num in row:
        print(num,end = " ")
print()