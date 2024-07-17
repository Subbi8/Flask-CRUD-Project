# Flask-CRUD Project

## Project Overview

The **Flask-CRUD Project** is a simple web-based To-Do List application where users can add, delete, and update tasks. The application uses Flask as the web framework, and all task data is stored in a file named `data.tb`. The project is developed in a virtual environment named `env`.

## Tech Stack

- **HTML**: For structuring the web pages.
- **CSS**: For styling the web pages.
- **Python**: For backend development.
- **Flask**: As the web framework.

## Features

- **Add Task**: Users can add new tasks to the to-do list.
- **Delete Task**: Users can delete existing tasks from the to-do list.
- **Update Task**: Users can update the details of existing tasks.

## Project Setup

### Prerequisites

- Python 3.x
- Virtualenv

### Installation

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd Flask-CRUD-Project
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv env
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source env/bin/activate
        ```

### Running the Application

1. **Start the Flask development server**:
    ```sh
    flask run
    ```

2. **Open your web browser and visit**:
    ```
    http://127.0.0.1:5000
    ```

## Project Structure

Flask-CRUD-Project/
│
├── env/
│ └── ... (Virtual environment files)
├── static/
│ └── css/
│ └── styles.css
├── templates/
│ ├── index.html
│ └── layout.html
├── app.py
├── data.tb
└── requirements.txt


### Explanation of Files

- `env/`: Contains the virtual environment files.
- `static/css/styles.css`: Contains the CSS styles for the application.
- `templates/`: Contains the HTML templates for the application.
- `app.py`: The main Flask application file.
- `data.tb`: The file where task data is stored.


## Usage

1. **Add Task**:
    - Go to the home page.
    - Enter the task details in the provided form and click "Add Task".

2. **Delete Task**:
    - Click the "Delete" button next to the task you want to remove.

3. **Update Task**:
    - Click the "Edit" button next to the task you want to update.
    - Update the task details in the form and click "Update Task".

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.


