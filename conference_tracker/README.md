# Conference Event Tracker Prototype

A simple web application to track conference events, add new ones, and view lists of upcoming activities.

## Features
- **Dashboard:** View all scheduled events sorted by date and time.
- **Add Event:** Easy-to-use form for inputting event details.
- **Event Details:** View full information for specific sessions.
- **Responsive UI:** Styled with Bootstrap 5 for mobile and desktop compatibility.

## Tech Stack
- **Backend:** Python / Flask
- **Frontend:** HTML / Jinja2 / Bootstrap 5
- **State Management:** In-memory list (restarts with app)

## Setup and Installation

1. **Navigate to the project folder:**
   ```bash
   cd conference_tracker
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - **On macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```
   - **On Windows:**
     ```bash
     .venv\Scripts\activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Testing the Prototype
1. Open the Dashboard (landing page).
2. Click "Add New Event" and fill out the form.
3. Click "Save Event" and verify it appears on the Dashboard.
4. Click on the event in the list to view its full details.
