import pickle
import csv
import os
from team_member import TeamMember
from team import Team
from league import League


class LeagueDatabaseImpl:
    def __init__(self):
        self._leagues = []
        self._last_oid = 0

    def get_league_names(self):
        return [league.name for league in self._leagues]

    def add_league(self, league):
        if league not in self._leagues:
            self._leagues.append(league)

    def remove_league(self, league):
        if league in self._leagues:
            self._leagues.remove(league)

    def league_named(self, name):
        for league in self._leagues:
            if league.name == name:
                return league
        return None

    def team_named(self, name):
        for league in self._leagues:
            for team in league.teams:
                if team.name == name:
                    return team
        return None

    def next_oid(self):
        self._last_oid += 1
        return self._last_oid


class LeagueDatabase:
    _sole_instance = None

    @classmethod
    def add_league(cls, league):
        cls.instance().add_league(league)

    @classmethod
    def remove_league(cls, league):
        return cls.instance().remove_league(league)

    @classmethod
    def instance(cls):
        if not cls._sole_instance:
            cls._sole_instance = LeagueDatabaseImpl()
        return cls._sole_instance

    @classmethod
    def league_named(cls, name):
        return cls.instance().league_named(name)

    @classmethod
    def team_named(cls, name):
        return cls.instance().team_named(name)

    @classmethod
    def load(cls, file_name):
        if os.path.exists(file_name):
            with open(file_name, 'rb') as f:
                cls._sole_instance = pickle.load(f)
                print(f"Loaded leagues from {file_name}.")
                print(f"Leagues: {cls._sole_instance.get_league_names()}")
        else:
            cls._sole_instance = LeagueDatabaseImpl()

    @classmethod
    def save(cls, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump(cls._sole_instance, f)

    @classmethod
    def get_league_names(cls):
        return cls.instance().get_league_names()

    @classmethod
    def import_league_teams(cls, file_name):
        print(f"Importing teams from {file_name}.")
        try:
            with open(file_name, 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header
                teams = []
                for row in reader:
                    league_name, team_name, member_name, member_email = row
                    league = cls.instance().league_named(league_name)
                    if league is None:
                        new_league_id = cls.instance().next_oid()
                        league = League(new_league_id, league_name)
                        cls.instance().add_league(league)
                        print(f"Added new league: {league_name}")  # Print the name of the new league
                    team = league.team_named(team_name) or Team(cls.instance().next_oid(), team_name)
                    team.add_member(TeamMember(cls.instance().next_oid(), member_name, member_email))
                    if not league.team_named(team_name):
                        league.teams.append(team)
                        print(
                            f"Added new team: {team_name} to league: {league_name}")
                    teams.append(team)
                # Save the teams to a pickle file
                with open('data/Teams.pkl', 'wb') as f:
                    pickle.dump(teams, f)
                print("Teams saved to pickle file.")  # Prints a message after saving the teams to the pickle file
        except Exception as e:
            print(f"An error occurred while importing teams: {e}")

    @classmethod
    def export_league_teams(cls, league, file_name):
        with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Team name', 'Member name', 'Member email'])
            for team in league.teams:
                for member in team.members:
                    writer.writerow([team.name, member.name, member.email])
