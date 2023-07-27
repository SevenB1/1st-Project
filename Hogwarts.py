students = [
    {"Name": "Hermione", "House": "Gryffindor", "Patronus": "Otter"},
    {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
    {"Name": "Ron", "House": "Gryffindor", "Patronus": "Jack Russell Terrier"},
    {"Name": "Draco", "House": "Slytherin", "Patronus": None},
]

for student in students:
    print(student["Name"], student["House"], student["Patronus"], sep=", ")
