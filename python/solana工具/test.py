address_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

index = 0

for i, value in enumerate(address_list):
    if value == "4":
        index = i
        break
print(address_list[index:])