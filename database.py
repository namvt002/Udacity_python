"""A database encapsulating collections of near-Earth."""


class NEODatabase:
    """A database of near-Earth objects and their close approaches."""

    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`."""
        self._neos = neos
        self._approaches = approaches
        self.neos_dict_des = dict()
        self.neos_dict_name = dict()
        for neo in self._neos:
            self.neos_dict_des[neo.designation] = neo
            if neo.name:
                self.neos_dict_name[neo.name] = neo
        for approach in self._approaches:
            approach.neo = self.neos_dict_des[approach._designation]
            self.neos_dict_des[approach._designation].approaches.append(
                approach
            )

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation."""
        return self.neos_dict_des.get(designation, None)

    def get_neo_by_name(self, name_neo):
        """Find and return an NEO by its name."""
        return self.neos_dict_name.get(name_neo, None)

    def query(self, filters=()):
        """Query close approaches."""
        if len(filters) == 0 and len(filters) < 0:
            yield from self._approaches
            return
        else:
            for approach in self._approaches:
                flg = True
                for filter_func in filters:
                    if not filter_func(approach):
                        flg = False
                        break
                if flg:
                    yield approach
