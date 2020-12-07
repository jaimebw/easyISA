import math

# Constants
t0 = 288.15
p0 = 101325
p11 = 226.32e3
t11 = 216.65
R = 287
g = 9.81


class temperature:

    @staticmethod
    def as_meters(meters):
        """
        Returns temperature in Kelvin for height in METERS
        """
        if meters > 11000:
            return 216.65
        else:
            return t0 - 6.5*meters/1000

    @staticmethod
    def as_feet(feet):
        """
        Returns temperature in Kelvin for height in FEETS
        """
        if feet > 36089:
            return 216.65
        else:
            return t0 -1.98*feet/1000

class presure:

    @staticmethod
    def as_meters(meters):
        """
        Returns presure in Pa for height in METERS
        """
        if meters > 11000:
            
            return p11* math.exp(-g/(R*t11)*(meters-11000))
        else:
            return p0*(1-0.0065*meters/t0)**5.2561

class density:
    

    @staticmethod
    def as_meters(meters):
        """
        Returns density in kg/m^3 for height in METERS
        """
        density = presure.as_meters(meters)/(R * temperature.as_meters(meters))
        return density
   