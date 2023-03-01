input_fruit=input("Enter 10 fruit name separating by space")
fruit_lst=input_fruit.split(" ")
print(fruit_lst)
for x in fruit_lst:
    print(x)
    if x=="cherry":
        break