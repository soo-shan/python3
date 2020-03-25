import abc

class MediaLoader(metaclass=abc.ABCMeta):
    # @abc.abstractclassmethod # deprecated
    # source: https://docs.python.org/3/library/abc.html#abc.abstractstaticmethod
    @staticmethod
    @abc.abstractmethod
    def play(self):
        pass

    # @abc.abstractproperty
    @property
    @abc.abstractmethod
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls,C):
        if cls is  MediaLoader:
            attrs =  set(dir(C))
            if set(cls.__abstractmethods__) <= attrs
                return True

        return NotImplemented

class Wav(MediaLoader):
    pass

class Ogg(MediaLoader):
    ext = ".ogg"
    