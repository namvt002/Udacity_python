"""You'll edit this file in Tasks 3a and 3c."""
import operator
import itertools


class UnsupportedCriterionError(NotImplementedError):
    """A filter criterion is unsupported."""


class AttributeFilter:
    """A general superclass for filters on comparable attributes."""

    def __init__(self, op, value):
        """Construct a new `AttributeFilter`."""
        self.op = op
        self.value = value

    def __call__(self, approach):
        """Invoke `self(approach)`."""
        return self.op(self.get(approach), self.value)

    @classmethod
    def get(cls, approach):
        """Get an attribute of interest from a close approach.

        Concrete subclasses must override this method to get an attribute of
        interest from the supplied `CloseApproach`.

        :param approach: A `CloseApproach` on which to evaluate this filter.
        """
        raise UnsupportedCriterionError

    def __repr__(self):
        """Use to return a formatted string that displays the class name."""
        return f"{self.__class__.__name__}"\
               f"(op=operator.{self.op.__name__}, value={self.value})"


class DateFilter(AttributeFilter):
    """A filter DateFilter."""

    @classmethod
    def get(cls, approach):
        """Return the date."""
        return approach.time.date()


class DistanceFilter(AttributeFilter):
    """A filter that DistanceFilter."""

    @classmethod
    def get(cls, approach):
        """Return the distance."""
        return approach.distance


class VelocityFilter(AttributeFilter):
    """A filter that VelocityFilter."""

    @classmethod
    def get(cls, approach):
        """Return the velocity."""
        return approach.velocity


class DiameterFilter(AttributeFilter):
    """A filter that DiameterFilter."""

    @classmethod
    def get(cls, approach):
        """Return the diameter."""
        return approach.neo.diameter


class HazardousFilter(AttributeFilter):
    """A filter that HazardousFilter."""

    @classmethod
    def get(cls, approach):
        """Return the hazardous."""
        return approach.neo.hazardous


def create_filters(
        date=None, start_date=None,
        end_date=None,
        distance_min=None, distance_max=None,
        velocity_min=None, velocity_max=None,
        diameter_min=None, diameter_max=None,
        hazardous=None
):
    """Create a collection of filters from user-specified criteria."""
    filters = []
    if date:
        filters.append(DateFilter(operator.eq, date))
    if start_date:
        filters.append(DateFilter(operator.ge, start_date))
    if end_date:
        filters.append(DateFilter(operator.le, end_date))
    if distance_min:
        filters.append(DistanceFilter(operator.ge, distance_min))
    if distance_max:
        filters.append(DistanceFilter(operator.le, distance_max))
    if velocity_min:
        filters.append(VelocityFilter(operator.ge, velocity_min))
    if velocity_max:
        filters.append(VelocityFilter(operator.le, velocity_max))
    if diameter_min:
        filters.append(DiameterFilter(operator.ge, diameter_min))
    if diameter_max:
        filters.append(DiameterFilter(operator.le, diameter_max))
    if hazardous is not None:
        filters.append(HazardousFilter(operator.eq, hazardous))

    return filters


def limit(iterator, n=None):
    """Limit the."""
    if not n:
        return iterator
    else:
        return itertools.islice(iterator, n)
