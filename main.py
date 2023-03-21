numbers = [3, 7, 9, 12]
first, second, third, four = numbers
sum = first + second + third + four
print(sum)

def najmniejsza(list):
    min = list[0 ]
    for i in numbers:
        if i < min:
            i = min
    return min

print(najmniejsza(numbers))

students = [
    {"imie": "Jan", "wiek": 20},
    {"imie": "Karolina", "wiek": 15},
    {"imie": "Brunhilda", "wiek": 185}
]

students.sort(key = lambda student:student["wiek"])
print(students[0])