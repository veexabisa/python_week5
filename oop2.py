# activity 2:

class Bee:

    def speak(self):
        return 'Buzz'
    
class Cow:

    def speak(self):
        return 'Mooo'
    
class Pig:

    def speak(self):
        return 'Oink'

for animal in [Bee(),Cow(),Pig()]:
    print(animal.speak())

