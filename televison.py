
class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__prev_volume = Television.MIN_VOLUME

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            if self.__muted:
                self.__volume = self.__prev_volume
                self.__muted = False
            else:
                self.__prev_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
                self.__muted = True

    def channel_up(self):
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
