# Flask Note-taking API

This repository contains a simple RESTful API developed using Python and Flask. The API is designed to provide CRUD (Create, Read, Update, Delete) operations for a simple note-taking application.

## Features

- Create new notes.
- Retrieve all notes.
- Retrieve a specific note by its ID.
- Update the details of a note.
- Delete a note.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/grausamkeit999/flask-note-api.git
    ```

2. Navigate into the cloned project directory:
    ```
    cd flask-note-api
    ```

3. Create a virtual environment:
    ```
    python -m venv env
    ```

4. Activate the virtual environment:
    - On Windows:
        ```
        env\Scripts\activate
        ```
    - On Unix or MacOS:
        ```
        source env/bin/activate
        ```

5. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Activate the virtual environment:
    - On Windows:
        ```
        env\Scripts\activate
        ```
    - On Unix or MacOS:
        ```
        source env/bin/activate
        ```

2. Run the script:
    ```
    python app.py
    ```

3. The server will be live at `localhost:5000`. You can use tools like Postman or curl to test the API endpoints.

## Contributing

Please feel free to fork this repository, make some changes, and open a pull request. Issues are also welcome.

## License

This project is licensed under the terms of the MIT license.
