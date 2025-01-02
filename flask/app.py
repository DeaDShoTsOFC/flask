# CPA Task App Backend

This repository contains the backend code for a CPA (Cost Per Action) task management app. The app allows users to register, log in, complete tasks, and earn rewards.

## Features

- User Registration and Login
- Task Listing
- Task Completion with Rewards
- User Balance Tracking
- JWT-Based Authentication

## Prerequisites

Before running the app, ensure you have the following installed:

- Python 3.7 or later
- Pip (Python package manager)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cpa-task-app.git
cd cpa-task-app
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Initialize the database and start the server:

```bash
python app.py
```

The server will start at `http://127.0.0.1:5000/`.

## API Endpoints

### User Routes

- **Register**: `POST /register`
  - Request Body:
    ```json
    {
      "username": "testuser",
      "password": "password123"
    }
    ```
- **Login**: `POST /login`
  - Request Body:
    ```json
    {
      "username": "testuser",
      "password": "password123"
    }
    ```
  - Response: JWT token for authentication.

### Task Routes

- **Get Tasks**: `GET /tasks`
  - Response: List of available tasks.
- **Complete Task**: `POST /complete_task`
  - Headers:
    ```
    Authorization: <JWT Token>
    ```
  - Request Body:
    ```json
    {
      "task_id": 1
    }
    ```

### Balance Route

- **Get Balance**: `GET /balance`
  - Headers:
    ```
    Authorization: <JWT Token>
    ```

## Folder Structure

```plaintext
cpa-task-app/
│
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── cpa_tasks.db        # SQLite database file (created after running the app)
└── README.md           # Project documentation
```

## Dependencies

The following Python packages are required:

- Flask
- Flask-SQLAlchemy
- Werkzeug
- PyJWT

To install them, run:

```bash
pip install -r requirements.txt
```

## Contributing

Feel free to fork this repository and make changes. Pull requests are welcome!

## License

This project is licensed under the MIT License.

## Contact

For any issues or questions, contact [your email or GitHub profile].
