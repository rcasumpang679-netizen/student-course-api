import unittest
from app import app


class StudentCourseAPITests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_course_list_endpoint(self):
        response = self.client.get("/api/courses")
        self.assertEqual(response.status_code, 200)
        courses = response.get_json()
        self.assertIsInstance(courses, list)
        self.assertGreaterEqual(len(courses), 5)
        for course in courses:
            self.assertIsInstance(course["id"], int)
            self.assertIn("code", course)
            self.assertIn("name", course)
            self.assertIn("description", course)

    def test_valid_course_endpoint(self):
        response = self.client.get("/api/courses/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["id"], 1)

    def test_unavailable_course_returns_404(self):
        response = self.client.get("/api/courses/9999")
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.get_json())


if __name__ == "__main__":
    unittest.main()
