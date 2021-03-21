<<<<<<< HEAD
from easyISA.equations import temperature,density,pressure
=======
from easyISA.equations import temperature,density,pressure, sound_speed
>>>>>>> 85a80d31ddc2f6e2f2661b81cbdf2eead4058c2c

def test_equations():
    tol = 1e-3
    assert temperature.meters(altitude=0) == 288.15
    assert (density.meters(altitude=0) > 1.225)& (density.meters(altitude=0) < 1.226)
    assert pressure.meters(altitude=0) == 101325
    assert round(temperature.meters(altitude=11000),2) == 216.65
    diff_p = abs((abs(pressure.meters(altitude=11000)) - 226.32e2)/pressure.meters(altitude=11000))
<<<<<<< HEAD
    assert abs(tol) - diff_p > 0
=======
    assert abs(tol) - diff_p > 0
    assert abs( round(sound_speed.meters(altitude = 0),1)- 340)-tol >0
    print(sound_speed.meters(altitude = 0))
>>>>>>> 85a80d31ddc2f6e2f2661b81cbdf2eead4058c2c
