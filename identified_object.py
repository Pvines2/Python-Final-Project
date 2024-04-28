from abc import ABC, abstractmethod


class IdentifiedObject(ABC):
    def __init__(self, oid):
        self._oid = oid

    @property
    def oid(self):
        return self._oid

    def __eq__(self, other):
        if not isinstance(other, IdentifiedObject):
            return NotImplemented
        return self._oid == other._oid

    def __hash__(self):
        return hash(self._oid)