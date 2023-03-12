
def speak(animal='dog'):
    animals=['dog','pig','duck','cat']
    animal_sounds=['woof','oink','quack','meow']
    animal_lang={animals[i]:animal_sounds[i] for i in range(len(animals))}
    if animal not in animals:
        return '?'
    return animal_lang[animal]
print(speak('pig'))
print(speak())
print(speak('mamo kupa'))