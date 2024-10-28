# User Management System

This project is a user management system that enables adding, updating, deleting, and displaying user information through a graphical user interface (GUI) developed in Python using the Tkinter library. User data is stored in a JSON file, which allows easy manipulation and persistence of information.
## Deployment: https://drive.google.com/file/d/1z8suVDkeVA2p8HFNAw-B05X407xn7v5a/view?usp=sharing
## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [File Structure](#file-structure)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)


## Project Description

The system allows users to perform the following actions:

- **Add a new user**: Input data such as ID, name, email, and date of birth.
- **Update user information**: Modify specific fields of existing users.
- **Delete a user**: Remove a user from the system by their ID.
- **Display user information**: Search and display user details.

## Features

- Intuitive, user-friendly graphical interface.
- Data validation to ensure correct input.
- Persistent data storage using JSON.
- Support for multiple user management operations.

## Technologies Used

- **Python**: Programming language used for development.
- **Tkinter**: Library used to create the graphical user interface.
- **JSON**: Data format used for storing user information.
- **Pip**: Dependency management (tkinter).

## Architecture
data_manager/ <br>
├── data/ <br>
│   └── users.json  <br>
├── src/ <br>
│   ├── __init__.py <br>
│   ├── file_handler.py  <br>
│   ├── menu.py <br>
│   ├── user_manager.py  <br>
│   └── validation.py  <br>
└── tests/ <br>
    └── test_user_manager.py

## Installation Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TheRedPill-exe/data_manager