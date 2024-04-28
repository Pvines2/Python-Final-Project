from PyQt5.QtWidgets import *
from league_database import LeagueDatabase
from league import League
from team import Team
from team_member import TeamMember


class LeagueManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Curling League Manager')
        self.setGeometry(100, 100, 600, 400)
        self.league_list_widget = QListWidget()
        LeagueDatabase.load('data/Leagues.pkl')
        self.refresh_league_list()
        self.init_ui()

    def init_ui(self):

        # Menu bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        loadAction = QAction('Load', self)
        loadAction.triggered.connect(self.load_league)
        fileMenu.addAction(loadAction)

        saveAction = QAction('Save', self)
        saveAction.triggered.connect(self.save_league)
        fileMenu.addAction(saveAction)

        self.league_list_widget = QListWidget()
        self.refresh_league_list()

        self.add_button = QPushButton("Add League")
        self.add_button.clicked.connect(self.add_league)

        self.delete_button = QPushButton("Delete League")
        self.delete_button.clicked.connect(self.delete_league)

        self.edit_button = QPushButton("Edit League")
        self.edit_button.clicked.connect(self.edit_league)

        layout = QVBoxLayout()
        layout.addWidget(self.league_list_widget)
        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.edit_button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_league(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Load League", "", "Pickle Files (*.pkl)")
        if file_path:
            LeagueDatabase.load(file_path)
            self.refresh_league_list()
            QMessageBox.information(self, "Load League", "League loaded successfully.")

    def save_league(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Save League", "", "Pickle Files (*.pkl)")
        if file_path:
            LeagueDatabase.save(file_path)
            self.refresh_league_list()
            QMessageBox.information(self, "Save League", "Leagues saved successfully!")

    def refresh_league_list(self):
        self.league_list_widget.clear()
        for league_name in LeagueDatabase.get_league_names():
            self.league_list_widget.addItem(league_name)

    def add_league(self):
        league_name, ok = QInputDialog.getText(self, "Add League", "Enter league name:")
        if ok and league_name:
            new_league = League(LeagueDatabase.instance().next_oid(), league_name)
            LeagueDatabase.add_league(new_league)
            self.refresh_league_list()

    def delete_league(self):
        selected_league_index = self.league_list_widget.currentRow()
        if selected_league_index >= 0:
            selected_league_name = self.league_list_widget.currentItem().text()
            league_to_remove = LeagueDatabase.league_named(selected_league_name)
            if league_to_remove:
                reply = QMessageBox.question(self, 'Delete League', f'Delete league "{selected_league_name}"?',
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    LeagueDatabase.remove_league(league_to_remove)
                    self.refresh_league_list()

    def edit_league(self):
        selected_league_index = self.league_list_widget.currentRow()
        if selected_league_index >= 0:
            selected_league_name = self.league_list_widget.currentItem().text()
            self.league_editor_window = LeagueEditorWindow(selected_league_name)
            self.league_editor_window.show()

    def load_database(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Load Database", "", "Pickle Files (*.pkl)")
        if file_path:
            LeagueDatabase.load(file_path)
            self.refresh_league_list()

    def save_database(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Save Database", "", "Pickle Files (*.pkl)")
        if file_path:
            LeagueDatabase.save(file_path)


class LeagueEditorWindow(QMainWindow):
    def __init__(self, league_name):
        super().__init__()
        self.setWindowTitle("League Editor")
        self.league_name = league_name
        self.init_ui()

    def init_ui(self):
        self.league_label = QLabel(self.league_name)
        self.team_list_widget = QListWidget()
        self.refresh_team_list()

        self.add_button = QPushButton("Add Team")
        self.add_button.clicked.connect(self.add_team)

        self.delete_button = QPushButton("Delete Team")
        self.delete_button.clicked.connect(self.delete_team)

        self.edit_button = QPushButton("Edit Team")
        self.edit_button.clicked.connect(self.edit_team)

        self.import_button = QPushButton("Import Teams")
        self.import_button.clicked.connect(self.import_teams)

        self.export_button = QPushButton("Export Teams")
        self.export_button.clicked.connect(self.export_teams)

        layout = QVBoxLayout()
        layout.addWidget(self.league_label)
        layout.addWidget(self.team_list_widget)
        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.import_button)
        layout.addWidget(self.export_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def refresh_team_list(self):
        self.team_list_widget.clear()
        league = LeagueDatabase.league_named(self.league_name)
        if league:
            for team in league.teams:
                self.team_list_widget.addItem(team.name)

    def add_team(self):
        team_name, ok = QInputDialog.getText(self, "Add Team", "Enter team name:")
        if ok and team_name:
            league = LeagueDatabase.league_named(self.league_name)
            if league:
                new_team = Team(LeagueDatabase.instance().next_oid(), team_name)
                league.add_team(new_team)
                self.refresh_team_list()

    def delete_team(self):
        selected_team_index = self.team_list_widget.currentRow()
        if selected_team_index >= 0:
            selected_team_name = self.team_list_widget.currentItem().text()
            reply = QMessageBox.question(self, 'Delete Team', f'Delete team "{selected_team_name}"?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                league = LeagueDatabase.league_named(self.league_name)
                if league:
                    team = league.team_named(selected_team_name)
                    if team:
                        league.remove_team(team)
                        self.refresh_team_list()

    def edit_team(self):
        selected_team_index = self.team_list_widget.currentRow()
        if selected_team_index >= 0:
            selected_team_name = self.team_list_widget.currentItem().text()
            self.team_editor_window = TeamEditorWindow(selected_team_name)
            self.team_editor_window.show()

    def import_teams(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Import Teams", "", "CSV Files (*.csv)")
        if file_path:
            league = LeagueDatabase.league_named(self.league_name)
            if league:
                LeagueDatabase.import_league_teams(file_path)
                self.refresh_team_list()

    def export_teams(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Export Teams", "", "CSV Files (*.csv)")
        if file_path:
            league = LeagueDatabase.league_named(self.league_name)
            if league:
                LeagueDatabase.export_league_teams(league, file_path)


class TeamEditorWindow(QMainWindow):
    def __init__(self, team_name):
        super().__init__()
        self.setWindowTitle("Team Editor")
        self.team_name = team_name
        self.init_ui()

    def init_ui(self):
        self.team_label = QLabel(self.team_name)
        self.member_list_widget = QListWidget()
        self.refresh_member_list()

        self.add_button = QPushButton("Add Member")
        self.add_button.clicked.connect(self.add_member)

        self.delete_button = QPushButton("Delete Member")
        self.delete_button.clicked.connect(self.delete_member)

        self.update_button = QPushButton("Update Member")
        self.update_button.clicked.connect(self.update_member)

        layout = QVBoxLayout()
        layout.addWidget(self.team_label)
        layout.addWidget(self.member_list_widget)
        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.update_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def refresh_member_list(self):
        self.member_list_widget.clear()
        team = LeagueDatabase.team_named(self.team_name)
        if team:
            for member in team.members:
                self.member_list_widget.addItem(member.name)

    def add_member(self):
        member_name, ok = QInputDialog.getText(self, "Add Member", "Enter member name:")
        member_email, ok = QInputDialog.getText(self, "Add Member", "Enter member email:")
        if ok and member_name and member_email:
            team = LeagueDatabase.team_named(self.team_name)
            if team:
                new_member = TeamMember(LeagueDatabase.instance().next_oid(), member_name, member_email)
                team.add_member(new_member)
                self.refresh_member_list()

    def delete_member(self):
        selected_member_index = self.member_list_widget.currentRow()
        if selected_member_index >= 0:
            selected_member_name = self.member_list_widget.currentItem().text()
            reply = QMessageBox.question(self, 'Delete Member', f'Delete member "{selected_member_name}"?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                team = LeagueDatabase.team_named(self.team_name)
                if team:
                    member = team.member_named(selected_member_name)
                    if member:
                        team.remove_member(member)
                        self.refresh_member_list()

    def update_member(self):
        selected_member_index = self.member_list_widget.currentRow()
        if selected_member_index >= 0:
            selected_member_name = self.member_list_widget.currentItem().text()
            new_member_name, ok = QInputDialog.getText(self, "Update Member", "Enter new member name:",
                                                       QLineEdit.Normal, selected_member_name)
            new_member_email, ok = QInputDialog.getText(self, "Update Member", "Enter new member email:",
                                                        QLineEdit.Normal, selected_member_name)
            if ok and new_member_name and new_member_email:
                team = LeagueDatabase.team_named(self.team_name)
                if team:
                    member = team.member_named(selected_member_name)
                    if member:
                        member.name = new_member_name
                        member.email = new_member_email
                        self.refresh_member_list()
