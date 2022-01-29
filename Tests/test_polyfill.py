### For testing and debugging purposes outside the robot ###
### run tests using pytest
### Also serves as examples of code usage ###

import mpy_robot_tools.hub_stub as hub

def test_hub():
    assert hub.Image("abc") == "abc"

def test_hub2():
    assert hub.display.show(hub.Image("abc")) == "abc"

from neopixel import NeoPixel

def test_np():
    np = NeoPixel(21,24)
    np.fill((1,2,3))
    assert np.buf[-1] == 3
    assert np.buf[-2] == 1
    assert np.buf[-3] == 2
    

