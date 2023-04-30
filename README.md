# QnA Platform API

The QnA Platform API is a service-oriented application for creating and managing questions and answers. Users can log in, post questions, and provide pro or con answers with a level from 1 to 5.

## Features

- User authentication
- Post, edit, and delete questions
- Post, edit, and delete pro or con answers with levels 1-5
- Retrieve questions and answers with filtering and sorting options

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:

   git clone https://github.com/yourusername/QnA-Platform-API.git

2. Set up the environment variables for your database and other configurations in the app/config.py and docker-compose.yml files.

3. Run the application using Docker Compose:

   cd QnA-Platform-API
   docker-compose up -d

The API will be accessible at http://localhost:5000/api/v1/. MySQL will be running in a separate Docker container.

## API Documentation

For detailed information on the available API endpoints and their usage, please refer to the [API Documentation](API_DOCUMENTATION.md).

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - ORM for database management
- [Flask-CORS](https://flask-cors.readthedocs.io/) - For handling Cross-Origin Resource Sharing
- [Docker](https://www.docker.com/) - Containerization platform
- [MySQL](https://www.mysql.com/) - Database system

