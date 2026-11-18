# Assignment 3 — Architecture Questions

Use this as a draft for Task C. Personalize it with your own deployment experience before submitting.

## 1. What is the role of the backend in your application?

The backend handles requests sent by a client, processes the requested operation, and returns a response. In this Student Course API, the Flask backend provides course information through HTTP GET endpoints. It keeps the sample course data, finds a requested course by ID, and returns the result in JSON format. It also reports whether the service is running and sends an appropriate error response when a course cannot be found.

## 2. What is the difference between an API endpoint and a database?

An API endpoint is a URL and HTTP method through which another application can request a service or data. A database is a system used to store and manage data persistently. For example, `/api/courses` is an endpoint that returns course information. A database could store that course information permanently. This prototype uses a Python list instead of a database.

## 3. Why does the backend return JSON?

JSON is a lightweight, structured data format that is easy for different programming languages and applications to exchange. A frontend can read the JSON response and display course names, codes, and descriptions. Returning consistent JSON also makes API responses easier to test and debug.

## 4. What is the difference between deploying a backend and integrating a frontend with it?

Deploying a backend means hosting the server-side application so it can receive HTTP requests through a public URL. Integrating a frontend means configuring a website or mobile application to send requests to that backend URL and use the returned data. Deployment makes the API accessible; integration makes the frontend use the API's services.

## 5. How could your existing Lesson 1 website and Lesson 2 mobile app use the same deployed API?

Both applications can send HTTP GET requests to the same public Render API URL. The website and mobile app can request `/api/courses` to display the course list or `/api/courses/1` to show one course. Since the API returns JSON, each frontend can parse the same response and present it using its own interface. The website's origin must be allowed by the API's CORS configuration when requests are made by a browser.

## 6. Why is the current application a prototype rather than a complete student information system?

It is a prototype because it only returns fictional course data. It does not have a database, user accounts, authentication, authorization, student records, enrollment features, or create, update, and delete operations. Its in-memory sample data is not persistent. A complete student information system would need secure access controls, persistent storage, validation, privacy protections, and additional features.

## Reflection draft (150–200 words)

This activity helped me understand how a backend API connects applications to data and how a small Python project can be deployed to the cloud. I learned that Flask can define API endpoints that respond to HTTP requests and return information in JSON format. I also learned the purpose of a health-check endpoint and why an API should return the correct HTTP status code when a requested course does not exist.

Creating the course-list and single-course endpoints helped me understand how routes and sample data work together. Testing the endpoints is important because a project should not be considered correct just because the code has been generated. Each endpoint must be opened or tested, and its response must be checked.

I also learned that Render needs the correct build and start commands to run a Flask application. GitHub provides the source repository that Render can use for deployment. This project is only a prototype because it uses fictional data stored in memory and has no database or authentication. In a future project, I would improve it by connecting a database and adding secure user access.

---

## Submission checklist

- [ ] Replit project link
- [ ] GitHub repository link
- [ ] Public Render API URL
- [ ] Screenshot of `/api/health`
- [ ] Screenshot of `/api/courses`
- [ ] Screenshot of `/api/courses/1`
- [ ] Screenshot of `/api/courses/9999` showing HTTP 404
- [ ] Screenshot of successful Render deployment or service dashboard
- [ ] Completed and personalized architecture answers
- [ ] Reflection reviewed and personalized
