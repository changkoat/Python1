from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute_behavior():
    tv = Television()
    tv.power()
    tv.volume_up()  # Vol = 1
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_channel_up():
    tv = Television()
    tv.power()
    for _ in range(5):
        tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

def test_volume_up_and_limit():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down_and_limit():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    tv.volume_down()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
