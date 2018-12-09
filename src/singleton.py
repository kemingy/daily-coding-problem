# Implement the singleton pattern with a twist. First, instead of storing one 
# instance, store two instances. And in every even call of getInstance(), return 
# the first instance and in every odd call of getInstance(), return the second 
# instance.

class Singleton(type):
    _instance = []
    odd = True
    def __call__(cls, *args, **kwargs):
        if len(cls._instance) < 2:
            instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instance.append(instance)
        cls.odd = True if not cls.odd else False
        return cls._instance[cls.odd]


class Twist(metaclass=Singleton):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    twists = [Twist(i) for i in range(5)]
    for t in twists:
        print(t.name)
