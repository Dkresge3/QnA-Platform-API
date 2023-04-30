
QnA Platform API - Database

This directory contains the necessary files for setting up the database for the QnA Platform API project. The database is implemented using MySQL.

Database Schema

The QnA Platform API database consists of three main tables:

1. users: Stores information about registered users.
2. questions: Stores information about questions submitted by users.
3. answers: Stores information about answers provided by users for the questions, including answer types (pro or con) and answer levels (1-5).

Setup

To set up the database, you can use the provided QnA_Platform_DB_Setup.sql file, which creates the qna_platform database and sets up the users, questions, and answers tables with the necessary columns and constraints.

Manual Setup

To set up the database manually, you can run the following command:

mysql -u <username> -p < QnA_Platform_DB_Setup.sql

Replace <username> with your MySQL username. You will be prompted to enter your password.

Docker Compose Setup

If you're using Docker Compose to deploy the QnA Platform API and MySQL database, the QnA_Platform_DB_Setup.sql file will be automatically executed during the initial setup. See the main README.md file for instructions on using Docker Compose.

Contributing

For information on how to contribute to this project, please see the CONTRIBUTING.md file in the root directory.

