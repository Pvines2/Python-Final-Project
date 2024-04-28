from exceptions import DuplicateOid
from identified_object import IdentifiedObject


class League(IdentifiedObject):
    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self._teams = []
        self._competitions = []

    @property
    def teams(self):
        return self._teams

    @property
    def competitions(self):
        return self._competitions

    def add_team(self, team):
        if any(t.oid == team.oid for t in self.teams):
            raise DuplicateOid(team.oid)
        self.teams.append(team)

    def remove_team(self, team):
        if team in self._teams:
            self._teams.remove(team)

    def team_named(self, team_name):
        for team in self._teams:
            if team.name == team_name:
                return team
        return None

    def add_competition(self, competition):
        if competition not in self._competitions:
            self._competitions.append(competition)

    def teams_for_member(self, member):
        return [team for team in self._teams if member in team.members]

    def competitions_for_team(self, team):
        return [comp for comp in self._competitions if team in comp.teams_competing]

    def competitions_for_member(self, member):
        return [comp for comp in self._competitions for team in comp.teams_competing if member in team.members]

    def __str__(self):
        return f"League {self.name}: {len(self._teams)} teams, {len(self._competitions)}"
