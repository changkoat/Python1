import pytest
from television import Television

class TestTelevision:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        self.tv = None

    def test_init(self):
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.tv.power()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
        self.tv.power()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
        self.tv.mute()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"

    def test_channel_up(self):
        self.tv.power()
        self.tv.channel_up()
        assert str(self.tv) == "Power = True, Channel = 1, Volume = 0"
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()  # Should wrap back to 0
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        self.tv.power()
        self.tv.channel_down()
        assert str(self.tv) == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()  # Should stay at MAX_VOLUME
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        self.tv.volume_down()
        self.tv.volume_down()  # Should stay at MIN_VOLUME
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"

