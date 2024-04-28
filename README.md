<<<<<<< HEAD
# Curling League Manager

## Overview

The Curling League Manager is a PyQt5-based interface designed to facilitate the management of curling leagues, including the ability to manage leagues, teams, and team members. This README provides an overview of the application's features, usage instructions, and technical details for developers.



## Features

The application offers the following functionalities:

1. **Main Window**:
   - Displays a list of leagues in the current database.
   - Provides options to load and save league data.
   - Allows users to add, delete, and edit leagues.

2. **League Editor**:
   - Displays a list of teams in the selected league.
   - Supports importing and exporting league data.
   - Allows users to add, delete, and edit teams within the league.

3. **Team Editor**:
   - Displays a list of team members in the selected team.
   - Enables users to add, delete, and update team members.

## Usage

### Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application using `python main.py`.

### Main Window

- Upon launching the application, the main window will display a list of existing leagues.
- Use the **Load** button to load league data from a file.
- Use the **Save** button to save league data to a file.
- Click on a league to select it for editing.
- Use the **Add League** button to create a new league.
- Use the **Delete League** button to remove a selected league.
- Click on the **Edit League** button to open the league editor window.
#### Saving Data
- When saving league information, ensure to save the data to the `Leagues.pkl` file.
- This is the default data file that the application loads upon startup.

### League Editor

- The league editor window allows you to manage teams within the selected league.
- Use the **Add Team** button to create a new team within the league.
- Click on a team to select it for editing.
- Use the **Delete Team** button to remove a selected team.
- Click on the **Edit Team** button to open the team editor window.
#### Importing Data
- Within the data file, there is a Test_Import.csv with sample data. 
- The file contains data for two new teams that belong to the "Senior league"

### Team Editor

- The team editor window allows you to manage team members within the selected team.
- Use the **Add Member** button to add a new member to the team.
- Click on a member to select it for editing.
- Use the **Delete Member** button to remove a selected member.
- Use the **Update Member** button to modify the details of a selected member.

## Development

### Dependencies

- Python 3.x
- PyQt5
- pickle (for data serialization)
- logging (for error logging)

### File Structure

- `main.py`: Entry point of the application.
- `gui.py`: Contains PyQt5-based GUI classes.
- `league_database.py`: Manages the storage and retrieval of league data.
- `league.py`: Defines the League class.
- `team.py`: Defines the Team class.
- `team_member.py`: Defines the TeamMember class.
- `exceptions.py`: Custom exception classes.
- `identified_object.py`: Base class for identified objects.
=======
# Curling-League-PyQt5
>>>>>>> b56e1d0c76fd42be0b2de40d0c18146ffe48dc6e
