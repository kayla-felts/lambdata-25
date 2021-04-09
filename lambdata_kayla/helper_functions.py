class Wrangle():
    def __init__(self, data):
        self.data = data

    def null_count(self):
        return self.data.isnull().sum().sum()

    def train_test_split(self, df, frac):
        from sklearn.model_selection import train_test_split
        split_data = train_test_split(df=self.data, test_size=frac)
        return split_data

class GOT_Characters:
    def __init__(self, name, age, house, sigil, home, location):
        self.name = str(name)
        self.age = int(age)
        self.house = str(house)
        self.sigil = str(sigil)
        self.home = str(home)
        self.location = str(location)

    def travel(self, destination):
        self.destination = str(destination)
        return f'{self.name} is traveling from {self.location} to {destination}'

    def speak(self):
        return f'I am {self.name} of house {self.house}. My home is {self.home}. My house sigil is {self.sigil}'

    def __repr___(self):
        return f'Character: {self.name}, Age: {self.age}, House: {self.house}, Sigil: {self.sigil}, Home: {self.home}, Current Location: {self.location}.'



