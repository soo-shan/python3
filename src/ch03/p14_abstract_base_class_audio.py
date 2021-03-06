import abc


class MediaLoader(metaclass=abc.ABCMeta):
    # @abc.abstractclassmethod # deprecated
    # source: https://docs.python.org/3/library/abc.html#abc.abstractstaticmethod
    @staticmethod
    @abc.abstractmethod
    def play(self):
        pass

    # @abc.abstractproperty # deprecated
    @property
    @abc.abstractmethod
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            # '<=' operator checks wheather attrs is superset
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented


class Wav(MediaLoader):
    pass


class Ogg(MediaLoader):
    ext = ".ogg"

    def play(self):
        print('This will play an ogg file')
        pass


## Since Wav class does not implement abstract attributes, its not possible to instantiate that class
# w = Wav()

## Ogg provides both the attributes
o = Ogg()
## We can define Ogg class as a subclass of the MediaLoader class
##  without actually extending MediaLoader class
print("issubclass(Ogg, MediaLoader):",issubclass(Ogg, MediaLoader))
print("isinstance(Ogg(),MediaLoader):",isinstance(Ogg(),MediaLoader))