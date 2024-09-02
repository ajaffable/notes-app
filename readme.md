# Notes API

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the server:
    ```bash
    python manage.py runserver
    ```

5. Access the API at `http://localhost:8000/api/` and Swagger documentation at `http://localhost:8000/swagger/`.

## API Endpoints

- **Create Note**: `POST /api/notes/create/`
- **Fetch Note by ID**: `GET /api/notes/<id>/`
- **Query Notes by Title Substring**: `GET /api/notes/?title=<substring>`
- **Update Note**: `PUT /api/notes/<id>/update/`
