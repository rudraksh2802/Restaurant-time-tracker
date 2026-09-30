# Design and Workflow

1. Start the program.
2. Load saved data if available.
3. Display current restaurant status.
4. User selects an operation.
5. Input is validated.
6. Data is updated.
7. Waiting time is calculated.
8. Customer can enter travel time.
9. Total expected time is displayed.
10. Data can be saved.
11. Program continues until Exit.

The design keeps the project understandable: `main.py` handles interaction, `restaurant.py` handles logic, `storage.py` handles files, and `test_project.py` checks important behaviour.

The waiting-time value is an estimate based on an average table turnover time, not a guaranteed prediction.
