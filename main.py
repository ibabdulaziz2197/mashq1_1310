# 2
for i in range(2, 30, 2):
    print(i)


# 9
sonlar = 0

while True:
    son = int(input())

    if son == 0:
        break

    if son > 10:
        sonlar += 1

print(sonlar)

# 17
fruits = ["olma", "banan", "anor"]
fruits.append('uzum')
print(fruits)

# 24
student = {
    "ism": "Sardor",
    "yosh": 16,
    "sinf": 10
}

print(student["ism"])

# 33
def qoshish(a, b):
    return a + b

natija = qoshish(5, 3)
print(natija)
