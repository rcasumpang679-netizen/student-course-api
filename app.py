import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Configure allowed browser origins with FRONTEND_ORIGINS, comma-separated.
# Example: https://your-frontend.example.com,http://localhost:3000
_origins = os.getenv("FRONTEND_ORIGINS", "*")
_allowed_origins = "*" if _origins.strip() == "*" else [
    origin.strip() for origin in _origins.split(",") if origin.strip()
]
CORS(app, resources={r"/api/*": {"origins": _allowed_origins}})

# Fictional sample data only. No database or real student records are used.
COURSES = [
    {
        "id": 1,
        "code": "CS101",
        "name": "Introduction to Computing",
        "description": "Explore computer systems, problem-solving, and basic programming concepts."
    },
    {
        "id": 2,
        "code": "WEB201",
        "name": "Web Development Fundamentals",
        "description": "Learn how websites work through HTML, CSS, JavaScript, and web concepts."
    },
    {
        "id": 3,
        "code": "DBS110",
        "name": "Database Concepts",
        "description": "Understand data organization, relational models, and introductory SQL."
    },
    {
        "id": 4,
        "code": "NET205",
        "name": "Computer Networking",
        "description": "Study network devices, addressing, protocols, and basic network security."
    },
    {
        "id": 5,
        "code": "UX120",
        "name": "User Experience Design",
        "description": "Practice user-centered design, wireframing, and usability evaluation."
    },
    {
        "id": 6,
        "code": "PY150",
        "name": "Python Programming",
        "description": "Build problem-solving skills using Python syntax, functions, and data structures."
    }
]


@app.get("/")
def index():
    return jsonify({
        "message": "Student Course API",
        "status": "running",
        "available_endpoints": [
            "/api/health",
            "/api/courses",
            "/api/courses/1"
        ]
    }), 200


@app.get("/api/health")
def health_check():
    return jsonify({
        "status": "ok",
        "message": "Student Course API is running"
    }), 200


@app.get("/api/courses")
def get_courses():
    return jsonify(COURSES), 200


@app.get("/api/courses/<int:course_id>")
def get_course(course_id):
    course = next((item for item in COURSES if item["id"] == course_id), None)
    if course is None:
        return jsonify({
            "error": "Course not found",
            "message": f"No course exists with ID {course_id}."
        }), 404
    return jsonify(course), 200


@app.errorhandler(404)
def not_found(_error):
    return jsonify({
        "error": "Not found",
        "message": "The requested endpoint does not exist."
    }), 404


@app.errorhandler(405)
def method_not_allowed(_error):
    return jsonify({
        "error": "Method not allowed",
        "message": "This API endpoint supports GET requests only."
    }), 405


@app.errorhandler(500)
def internal_server_error(_error):
    return jsonify({
        "error": "Internal server error",
        "message": "An unexpected server error occurred."
    }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
