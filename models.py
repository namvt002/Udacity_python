from helpers import cd_to_datetime, datetime_to_str
import math

class NearEarthObject:

    def __init__(self, designation, name, diameter, hazardous):

        self.designation = designation
        self.name = name if name else None
        self.diameter = diameter if diameter else float('nan')
        self.hazardous = hazardous

        self.approaches = []

    @property
    def fullname(self):
        if self.name:
            return f"{self.designation} ({self.name})"
        else:
            return f"{self.designation}"

    def __str__(self):

        notification = f"NEO {self.fullname} has a diameter of"
        if self.diameter is not None and not math.isnan(self.diameter):
            notification = notification + f" {self.diameter:.3f} km and "
        if not self.hazardous:
            notification = notification + "is not potentially hazardous."
        else:
            notification = notification + "is potentially hazardous."
        return notification

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    
    def __init__(self, designation = '', time = None, distance = 0.0, velocity = 0.0, neo = None ):

        self._designation = designation
        self.time = cd_to_datetime(time)
        self.distance = distance
        self.velocity = velocity

        self.neo = neo

    @property
    def time_str(self):
        return datetime_to_str(self.time)

    def __str__(self):
        notification_close = f"On {self.time}, '{self._designation}' approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."
        return notification_close

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
