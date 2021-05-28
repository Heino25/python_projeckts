#3-1
names = ['Eric', 'Belthus', 'Braam', 'Mike']
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#3-2
message =f"Thank you for being my friend {names[0]}"
print(message)

#3-3
transportation = ['drive', 'fly', 'walk by foot']
sentance1 = "My favourite transportation is to"
print(f"{sentance1} {transportation[1]}")

#3-4
sentance2 = "I would like to invite you to dinner"
print(f"{sentance2} {names}")

#3-5
names.remove('Eric')
print(names)
print(f"{sentance2} {names}")

#3-6
names.append('Chris')
print(names)

names.insert(2,'Steph')
names.insert(3,'Roux')
print(names)

sentance2 = "I would like to invite you to dinner"
print(f"{sentance2} {names}")

#3-7
sentance2 = "I would like to invite you to dinner"
print(f"{sentance2} \n{names} \nSorry I can only invite 2 people for dinner.")

names.pop()
print(names)

names.pop()
print(names)

names.pop()
print(names)

names.pop()
print(names)

sentance3 = "You are still invited"
print(f"{names}, {sentance3}")

del names[0]
print(names)

del names[0]
print(names)