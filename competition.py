from identified_object import IdentifiedObject


class Competition(IdentifiedObject):
    def __init__(self, oid, teams, location, date_time=None):
        super().__init__(oid)
        self._teams_competing = teams
        self.location = location
        self.date_time = date_time

    @property
    def teams_competing(self):
        return self._teams_competing

    def send_email(self, emailer, subject, message):
        recipients = set()
        for team in self._teams_competing:
            for member in team.members:
                if member.email is not None:
                    recipients.add(member.email)
        emailer.send_plain_email(list(recipients), subject, message)

    def __str__(self):
        date_str = self.date_time.strftime("%m/%d/%Y %H:%M") if self.date_time else ""
        return f"Competition at {self.location} on {date_str} with {len(self._teams_competing)} teams"