
class MyClass(object):
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name', 'no name')
        self.surname = kwargs.get('surname', 'no surname')
    
    def __str__(self):
        return("The full name is {} {}".format(self.name, self.surname))
