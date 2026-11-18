# Student Course API

A beginner-friendly, read-only REST API built with Python and Flask. It uses fictional course data stored in memory. It does not use a database, authentication, or real student records.

## Features

- `GET /api/health` — confirms that the API is running.
- `GET /api/courses` — returns six fictional courses.
- `GET /api/courses/<id>` — returns one course or a JSON 404 error.
- JSON responses and basic HTTP error handling.
- Configurable CORS for browser-based frontend projects.
- Gunicorn production server configuration for Render.

## Project structure

```text
student-course-api/
├── app.py
├── requirements.txt
├── render.yaml
├── Procfile
├── README.md
└── tests/
    └── test_app.py
```

## Run locally

Python 3.10 or newer is recommended.

1. Create and activate a virtual environment:

   **Windows**
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the development server:

   ```bash
   python app.py
   ```

4. Open `http://127.0.0.1:5000/api/health` in a browser.

The app reads the `PORT` environment variable and listens on `0.0.0.0`, as required by Render.

## API endpoints

| Method | Endpoint | Successful response |
|---|---|---|
| GET | `/api/health` | HTTP 200 and JSON service status |
| GET | `/api/courses` | HTTP 200 and an array of six courses |
| GET | `/api/courses/1` | HTTP 200 and course ID 1 |
| GET | `/api/courses/9999` | HTTP 404 and a JSON error |

Every course has an integer `id`, a `code`, a `name`, and a short `description`.

Example course response:

```json
{
  "id": 1,
  "code": "CS101",
  "name": "Introduction to Computing",
  "description": "Explore computer systems, problem-solving, and basic programming concepts."
}
```

Example not-found response:

```json
{
  "error": "Course not found",
  "message": "No course exists with ID 9999."
}
```

## Run the tests

From the project root, run:

```bash
python -m unittest discover -s tests -v
```

The test suite checks the health endpoint, course list, valid course ID, and unavailable course ID. A test result is verified only when you run the command and see it pass.

## CORS configuration

For classroom demonstrations, CORS allows all origins by default. Before using a real frontend deployment, set the `FRONTEND_ORIGINS` environment variable to the exact frontend origin(s), separated by commas.

Example:

```text
FRONTEND_ORIGINS=https://your-frontend.example.com,http://localhost:3000
```

Do not put secrets in source code or commit `.env` files.

## Deploy to Render

1. Push this project to a GitHub repository named `student-course-api`.
2. Sign in to [Render](https://render.com/).
3. Choose **New** → **Web Service** and connect the GitHub repository.
4. Configure:
   - **Runtime:** Python 3
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`
   - **Health check path:** `/api/health` (if the dashboard offers this field)
5. Create the Web Service and wait for the deployment to finish.
6. Copy the actual public URL shown in the Render dashboard.

The `app:app` start command means: load the Flask variable named `app` from the Python file `app.py`. If you rename the file or Flask variable, update the command.

### Test the deployed API

Replace `YOUR-RENDER-URL` with the actual URL from your Render dashboard:

```text
https://YOUR-RENDER-URL/api/health
https://YOUR-RENDER-URL/api/courses
https://YOUR-RENDER-URL/api/courses/1
https://YOUR-RENDER-URL/api/courses/9999
```

Expected status codes: `200`, `200`, `200`, and `404`, respectively. Open each URL and inspect its response before marking it verified. The example URL in this README is not a live deployment.

## GitHub upload

If Git is installed, run these commands in the project directory:

```bash
git init
git add .
git commit -m "Create Student Course API"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/student-course-api.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If the repository already has a remote, do not add it a second time.

## Architecture overview

- **Backend entry point:** `app.py`; the Flask application object is named `app`.
- **Routes:** Flask GET route functions in `app.py`.
- **Sample data:** the `COURSES` Python list in `app.py`.
- **Response format:** JSON, with HTTP status codes.
- **Dependencies:** Flask, Flask-Cors, and Gunicorn, listed in `requirements.txt`.
- **Production server:** Gunicorn, started with `gunicorn app:app`.
- **Hosting:** Render runs the web service and supplies its listening port through the `PORT` environment variable.

## Limitations

This is a classroom prototype, not a production student information system. Course data is held in memory and is reset when the process restarts. There is no database, authentication, authorization, student data, or write endpoint. Free hosting may sleep when inactive, so the first request can be delayed.
