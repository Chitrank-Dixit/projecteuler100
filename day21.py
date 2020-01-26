import csv

alphabet_score = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

with open("p022_names.txt", 'r') as file:
    names = []
    for row in csv.reader(file, delimiter=','):
        for element in row:
            names.append(element)
    sorted_names = sorted(names)
    total_score = 0
    for counter, name in enumerate(sorted_names):
        char_score = 0
        for char in name:
            char_score += alphabet_score[char]
        total_score += (char_score * (counter + 1))

print(total_score)
