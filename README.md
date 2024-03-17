# Fix the Bug - Elan

Welcome to the "Fix the Bug" event organized by Lambda, the software development club at IIT Hyderabad!

## Introduction

In this question you are given a backend application codebase with several bugs. Your task is to identify and fix these bugs to ensure that the application, built using the FastAPI framework, functions correctly.

### Storyline

Tom Holland, a beginner developer, attempted to create an application allowing users to post questions and answers. However, he watched some youtube tutorials without fully grasping the concepts, resulting in several bugs that he couldn't resolve on his own. Seeking assistance, he turned to you for help.

Now he is counting on you for fixing these bugs!

## Task Description

Your primary objective is to ensure that __each route in the application is functioning correctly__. Although the logic behind the routes is correct, there are bugs present in the codebase that need to be resolved.

### Files in the Codebase

- **Router Folder**: Contains `answer.py` and `question.py` files, which define the routes for answering questions and posting questions, respectively.
- **Database Connection File**: Manages the connection to the database.
- **Main File**: Entry point for the application.
- **Models File**: Defines the database models.
- **Schemas File**: Contains Pydantic schemas for data validation.

### Important Note

- **Route Logics**: The logic for each route is correct, so there's no need to modify it. Your focus should be on identifying and fixing bugs elsewhere in the codebase, just try accessing each route.
- **How to create a question in the /create route given in the question.py file?**

    Follow these steps:

    1. Open Postman.
    2. Select the HTTP method (e.g., POST) and enter the URL for the create question route.
    3. In the Body section, select the raw option.
    4. Enter the following JSON object:

          ```json
          {
              "content": "Rate this question: 1 - 10"
          }
          ```
    5. Click Send button. Check your database.

- **How to add an answer in the /add route given in the answer.py file?**

    Steps are same as that followed in creating a question.
    Just change the JSON text:

   ```json
  {
      "content" : "I rate it 10/10"
  }
    ```



## Getting Started

To participate in this event, follow these steps:

1. Clone the repository containing the codebase.
    ```bash
    git clone https://github.com/LambdaIITH/ftb_FastAPI-Git-CodeBase
    cd ftb_FastAPI-Git-CodeBase/Question_1
    ```
2. Set up a virtual environment. If you're using venv, you can create a virtual environment using the following command:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment.
   - **Windows**:
      ```bash
      venv\Scripts\activate
      ```
   - **Linux/macOS**:
      ```bash
      source venv/bin/activate
      ```

4. Install dependencies from the requirements.txt file.
    ```bash
    pip install -r requirements.txt
    ```
5. Install the pre-commit hooks.
    ```bash
    pre-commit install
    ```
6. Setting Up the Database
    Before using the API, you need to set up a database on your local machine. Follow these steps:

    1. Make sure you have a database server installed (e.g., PostgreSQL, MySQL, SQLite).

    2. Once the database is created, navigate to the `database.py` file and locate the SQLALCHEMY_DATABASE_URL.

    4. Replace the placeholder `"<your_database_connection_string>"` with the connection string for your database. For example, for a local PostgreSQL database, the connection string might look like:

        ```python
        SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/mydatabase"
        ```

       Replace `"postgresql://username:password@localhost/mydatabase"` with your actual connection string.

7. Run the application.
    ```bash
    uvicorn app.main:app --reload
    ```

8. Once the application is running, you can access the API at `http://localhost:8000` (if no bugs are present :P).

## Additional Tools

- **Postman**: You may use Postman for testing API endpoints.
- **pgAdmin**: If you're using PostgreSQL, pgAdmin can be helpful for database management.

## Instructions

### FastAPI:
1. Start by examining the codebase provided.
2. Identify and fix any bugs present in the code.
3. Ensure that each route is accessible and functioning correctly.
4. Test the application thoroughly to validate your fixes.
5. Once you're confident in your changes, submit your corrected code.

### Misc bugs:
1. Tom Holland tried to use black which is a formatter for python code as a hook that runs before every commit. He followed some tutorial found online and copied exactly, but he couldn't set it up properly. Can you help him with that?

Good luck, and Happy debugging👍🏻 !

# Hints: 
1. Tom is importing A in B from C also importing A in C from B. Can you see it? Is this possible? This is the __main__ part for first bug.
2. Thoroughly test all the APIs.
3. There might be an inherent defect in the models/schemas itself.
4. (Misc Bug): Why is the formatter not running?
