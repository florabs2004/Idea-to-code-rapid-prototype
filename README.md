# Idea-to-code-rapid-prototype
Rapid prototype with Gemini CLI command

## Conference Event Tracker Prototype

This project demonstrates the power and efficiency of using the Gemini CLI for rapid prototyping. It guides you from a conceptual idea to a running web application prototype by leveraging the CLI's custom commands.

The Gemini CLI significantly shortens the prototyping cycle, allowing for faster iteration and experimentation. By using the CLI, developers can quickly validate ideas and focus on the core logic and unique aspects of their application while automating boilerplate code generation and setup.

### Core Features
- **Dashboard:** View all scheduled events sorted by date and time.
- **Add Event:** Easy-to-use form for inputting event details.
- **Event Details:** View full information for specific sessions.
- **Responsive UI:** Styled with Bootstrap 5 for mobile and desktop compatibility.

---

## Getting Started

### Custom Commands

The custom commands for this project are defined in the `.gemini/commands` directory.

- `/idea-to-spec`: Transforms a user's idea into a detailed specification.
- `/spec-to-code`: Generates a running application from a detailed specification.

### Running the Application

1. **Navigate to the application folder:**
   ```bash
   cd Event_track
   ```

2. **Setup virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the application:**
   ```bash
   python app.py
   ```

---

## Gemini CLI Demo Instructions

This guide walks you through the following steps:

1.  Prepare the environment
1.  Build a specification for an application idea
1.  Implement application using the specification
1.  Test application and iterate on the features

### Requirements

To follow this demo, you need:

- A Google Cloud project with the `Owner` role.
- Gemini CLI: Installed and configured.

### Start prototyping

1.  Run Gemini CLI:
    ```bash
    gemini
    ```

2.  Type `/spec` to confirm the custom commands are loaded and available.

### Idea to running application

1.  Send prompt to create specification for your idea:
    ```text
    /idea-to-spec build a web app to track conference events, add new events and view lists of upcoming events.
    ```

2.  Send prompt to build the application:
    ```text
    /spec-to-code build the application using the spec
    ```
