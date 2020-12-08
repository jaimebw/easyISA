from easyISA.equations import temperature,density,presure

def test_isa():
    assert temperature.as_meters(meters=0) == 288.15
    assert (density.as_meters(meters=0) > 1.225)& (density.as_meters(meters=0) < 1.226)
    assert presure.as_meters(meters=0) == 101325
