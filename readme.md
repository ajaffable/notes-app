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

5. **Access the API and Swagger documentation:**

    - **API Endpoint:** [http://localhost:8000/api/](http://localhost:8000/api/)
    - **Swagger Documentation:** [http://localhost:8000/swagger-ui/](http://localhost:8000/swagger-ui/)


## API Endpoints

- **Create Note**: `POST /api/notes/create/`
  - Request body: `{"title": "Note Title", "content": "Note Content"}`
  - Description: Create a new note.

- **Fetch Note by ID**: `GET /api/notes/<id>/`
  - Description: Retrieve a note by its ID.

- **Query Notes by Title Substring**: `GET /api/notes/?title=<substring>`
  - Description: Retrieve a list of notes where the title contains the specified substring.

- **Update Note**: `PUT /api/notes/<id>/update/`
  - Request body: `{"title": "Updated Title", "content": "Updated Content"}`
  - Description: Update the note with the given ID.


## Swagger UI

Swagger UI is available for interactive API documentation and testing:

- **Access Swagger UI:** [http://localhost:8000/swagger-ui/](http://localhost:8000/swagger-ui/)
  - Here you can see the API schema, test endpoints, and understand the expected request and response formats.

## Configuration

Ensure that your `settings.py` includes the necessary configuration for `drf-spectacular`:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Notes API',
    'DESCRIPTION': 'A REST API for managing notes',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
