"""Represent models for near-Earth objects."""
from helpers import cd_to_datetime, datetime_to_str
import math


class NearEarthObject:
    """A near-Earth object (NEO)."""

    def __init__(self, designation, name, diameter, hazardous):
        """Create a new `NearEarthObject`."""
        self.designation = designation
        self.name = name if name else None
        self.diameter = diameter if diameter else float('nan')
        self.hazardous = hazardous

        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the fullname of this NEO."""
        if self.name:
            return f"{self.designation} ({self.name})"
        else:
            return f"{self.designation}"

    def __str__(self):
        """Return `str(self)`."""
        notification = f"NEO {self.fullname} has a diameter of"
        if self.diameter is not None and not math.isnan(self.diameter):
            notification = notification + f" {self.diameter:.3f} km and "
        if not self.hazardous:
            notification = notification + "is not potentially hazardous."
        else:
            notification = notification + "is potentially hazardous."
        return notification

    def __repr__(self):
        """Return `repr(self)`."""
        return f"NearEarthObject(designation={self.designation!r},"\
               f"name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """A Closeapproach to Earth by an NEO."""

    def __init__(self, designation: str,
                 time: str = None,
                 distance: float = 0.0,
                 velocity: float = 0.0,
                 neo=None
                 ):
        """Create a new `CloseApproach`."""
        self._designation = designation
        self.time = cd_to_datetime(time)
        self.distance = distance
        self.velocity = velocity

        self.neo = neo

    @property
    def time_str(self):
        """Return a formatted."""
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        notification_close = f"On {self.time}, '{self._designation}' "\
                             f"approaches Earth at a distance" \
                             f"of {self.distance:.2f}" \
                             f"au and a velocity of {self.velocity:.2f} km/s."
        return notification_close

    def __repr__(self):
        """Return `repr(self)`."""
        return f"CloseApproach(time={self.time_str!r}," \
               f"distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
