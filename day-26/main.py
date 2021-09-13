new_list = [a + a for a in range(1, 5)]
print(new_list)

names = ["Alex", "beth", "dave", "caroline", "freddie"]

short_names = [name.upper() for name in names if len(name) > 5]
print(short_names)

result = [ int(num.strip("\n")) for num in open("file1.txt").readlines() if num in open("file2.txt").readlines() ]

# Write your code above 👆

print(result)


