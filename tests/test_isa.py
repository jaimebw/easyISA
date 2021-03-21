from easyISA.equations import temperature,density,pressure

def test_equations():
    tol = 1e-3
    assert temperature.meters(altitude=0) == 288.15
    assert (density.meters(altitude=0) > 1.225)& (density.meters(altitude=0) < 1.226)
    assert pressure.meters(altitude=0) == 101325
    assert round(temperature.meters(altitude=11000),2) == 216.65
    diff_p = abs((abs(pressure.meters(altitude=11000)) - 226.32e2)/pressure.meters(altitude=11000))
    assert abs(tol) - diff_p > 0