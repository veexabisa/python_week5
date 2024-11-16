# activity 1:

class SuperHero :
    name = 'Queen'
    def __init__(self, name):
        self.name = name
    def speak(self):
     print('My name is {}, I am the mother of dragons '.format(self.name))

class Hero:
    name = 'Khaleesi'
    def __init__(self, aka):
        self.aka = aka
    def speak(self):
      print('I am also known as the {}'.format(self.aka))

class Super:
    name = 'HOD'
    def __init__(self, hair):
        self.hair = hair
    def speak(self):
     print('My hair is as {} as snow'.format(self.hair))
     

Queen = SuperHero('Daenerys')
Khaleesi = Hero('Breaker of chains')
HOD = Super('white')

Queen.speak()
Khaleesi.speak()
HOD.speak()










