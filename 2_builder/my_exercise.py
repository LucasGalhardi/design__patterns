
class Field:
    def __init__(self, typee, value):
        self.typee = typee
        self.value = value

    def __str__(self):
        return f'\t\tself.{self.typee} = {self.value}\n'


class Code:

    def __init__(self, name=''):
        self.name = name
        self.fields = []

    def __str__(self):
        representation = f'class {self.name}:\n\tdef __init__(self):\n'
        for f in self.fields:
            representation += str(f)
        return representation


class CodeBuilder:
    __root = Code()

    def __init__(self, name):
        self.__root.name = name

    def add_field(self, typee, value):
        self.__root.fields.append(Field(typee, value))
        return self

    def __str__(self):
        return self.__root.__str__()


cb = CodeBuilder('Animal').add_field('nome', '""').add_field('quantidade_media_filhos', '0')
print(cb)
