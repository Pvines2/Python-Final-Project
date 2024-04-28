from exceptions import DuplicateEmail
from identified_object import IdentifiedObject


class Team(IdentifiedObject):
    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self._members = []

    @property
    def members(self):
        return self._members

    def add_member(self, member):
        if any(m.email.lower() == member.email.lower() for m in self.members):
            raise DuplicateEmail(member.email)
        self.members.append(member)

    def member_named(self, name):
        for member in self._members:
            if member.name == name:
                return member
        return None

    def remove_member(self, member):
        if member in self._members:
            self._members.remove(member)

    def send_email(self, emailer, subject, message):
        recipients = [member.email for member in self._members if member.email is not None]
        emailer.send_plain_email(recipients, subject, message)

    def __str__(self):
        return f"Team {self.name}: {len(self._members)} members"
