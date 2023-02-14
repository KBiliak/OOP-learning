class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age




    def barking(self):
        print(f"Dog with name {self.name}, breed {self.breed} and age {self.age} is barking now")

    def wagging(self):
        print(f"Dog with name {self.name}, breed {self.breed} and age {self.age}  is wagging his tale now")

    def all_info(self):
        print(f"My dog's name is {self.name}, it is a {self.breed}. "
              f"My {self.name} is {self.age} years old. Hi is barking now "
              f" and his tail is wagging now")


dog = Dog("Rokki", "spaniel", 0.6)
dog.barking()
dog.all_info()


