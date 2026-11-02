# Docker-Based IT Helpdesk & Ticket Management System

## Project Overview
A simple web-based IT Helpdesk Management System that allows employees to submit technical support tickets and track their status.

The application is developed using Python Flask and SQLite and deployed using Docker and Docker Compose.

## Features
- Submit technical support tickets.
- View all submitted tickets.
- Update ticket status.
- Store ticket information in SQLite.
- Docker-based application deployment.
- Docker Compose for container management.
- Docker volume for persistent data storage.

## Technologies Used
- Python
- Flask
- HTML and CSS
- SQLite
- Docker
- Docker Compose
- GitHub Codespaces

## Project Structure
```text
dockerhelpdesk/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## How to Run the Project

### 1. Build and start the application
```bash
docker compose up -d --build
```

### 2. Check running containers
```bash
docker compose ps
```

### 3. View application logs
```bash
docker compose logs
```

### 4. Stop the application
```bash
docker compose down
```

### 5. Start the application again
```bash
docker compose up -d
```

## Database Storage
SQLite stores ticket records in `/app/data/helpdesk.db`.

A Docker named volume is mounted at `/app/data` to preserve database information when the container is removed and recreated.

## Application Access
The application runs on port 5000.

Open port 5000 through the GitHub Codespaces Ports tab to access the website.

## Conclusion
This project demonstrates basic web application development, database integration, Docker containerisation, Docker Compose, and persistent storage using Docker volumes.