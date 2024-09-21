# Phonebook Web Application

This is a simple Phonebook web application developed using **Flask** (for backend) and **HTML, CSS, JavaScript** (for frontend). It allows users to add, search, import, and export contacts with their associated details. The application also supports dark and light themes.

## Features

- **Add New Contact**: Users can add a new contact by providing a name, phone number, and selecting tags such as "Friend," "Work," or "Family."
- **Search Contacts**: Users can search for a contact by name or phone number.
- **View Contact List**: All added contacts are displayed in a list format.
- **Export Contacts**: Contacts can be exported in CSV format.
- **Import Contacts**: Users can import contacts from a CSV file.
- **Dark/Light Mode**: Toggle between dark and light themes for the app interface.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Data Storage**: Local storage (for temporary browser-side contact storage)

## Prerequisites

To run this project locally, you'll need to have the following installed:

- Python 3.x
- Flask

## How to Run the Project

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/phonebook-app.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd phonebook-app
    ```

3. **Install the required Python dependencies**:
    You can do this by running:
    ```bash
    pip install Flask
    ```

4. **Run the Flask application**:
    Execute the following command:
    ```bash
    python app.py
    ```

5. **Access the application**:
    Open your web browser and navigate to:
    ```
    http://192.168.120.41:5000
    ```

## Project Structure

```bash
phonebook-app/
│
├── app.py                      # Main Flask application
├── static/
│   ├── script.js               # JavaScript for handling interactions and functionality
│   └── styles.css              # CSS for styling the app
└── templates/
    └── index.html              # Frontend HTML template

## Functionality Breakdown

1. **Adding Contacts**
- Users can input a name, phone number, and select tags (Friend, Work, Family) to categorize their contacts.
- The contact information is stored in the browser’s local storage temporarily for display.
2. **Searching Contacts**
- A search bar is provided to allow users to quickly find contacts by name or phone number.
3. **Import/Export Contacts**
- **Export**: Users can export all contacts as a CSV file. The CSV will contain the name, phone number, and tags for each contact.
- **Import**: Users can upload a CSV file to import multiple contacts at once. The file should follow this format:

```Name, Phone, Tag1|Tag2|Tag3```

4. **Theme Toggle**
- The app provides a button to switch between dark and light modes for better user experience.

## Future Enhancements
- Integrating server-side database (e.g., SQLite or MySQL) to store contacts permanently.
- Adding user authentication for managing personal contacts across sessions.
- Enhanced error handling and form validations.
