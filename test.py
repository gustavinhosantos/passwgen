#path = r"C:\Users\Gustavo\vscode\Python\insta_basic\passgen\savings.py"

#file = open(path, 'a')
#file.write('gpopooppoopopop')
#file.close()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name},{self.age}"

p1 = Person("John", 36)

print(p1)