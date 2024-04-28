from PyQt5.QtWidgets import *
from league_database import LeagueDatabase
from PyQt5GUI import LeagueManagerWindow
from league import League
import pickle


def main():
    # Import the leagues and teams from the CSV file
    LeagueDatabase.import_league_teams('data/Teams.csv')

    LeagueDatabase.load('data/Leagues.pkl')

    # Load the teams from the pickle file
    try:
        with open('data/Teams.pkl', 'rb') as f:
            teams = pickle.load(f)
        print("Loaded teams from pickle file.")
    except Exception as e:
        print(f"Error has occurred while loading teams: {e}")

    try:
        with open('data/Teams.pkl', 'rb') as f:
            teams = pickle.load(f)
        print("Loaded teams from pickle file.")
    except Exception as e:
        print(f"Error has occurred while loading teams: {e}")
        teams = []

    # Save the updated league database
    LeagueDatabase.save('data/Leagues.pkl')
    print("League database saved with new teams and members.")

    # Initialize and execute the application
    app = QApplication([])
    window = LeagueManagerWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
