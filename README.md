### Linter status:
[![CI](https://github.com/Dzigr/quiz/actions/workflows/CI.yml/badge.svg)](https://github.com/Dzigr/quiz/actions/workflows/CI.yml)

# Quiz app

**Stack:**
* Python
* FastAPI
* PostgreSQL
* Docker

----

### Start project with Docker ###

----

###### Note: Required Python & Poetry ######
1. Clone the repository
    ```comandline
    git clone git@github.com:Dzigr/quiz && cd quiz
    ```

2. Initiate configuration with Makefile command
    ```commandline
    make docker-install
    ```
   This will create .env file with necessary variables, requirements file and build docker containers

3. Run application by
    ```commandline
    make docker
    ```

<details><summary>
Without poetry
</summary>

---

1. Create virtual environment
    ```commandline
    python3 -m venv venv
    ```
2. Activate virtual environment
    ```commandline 
    source venv/bin/activate
    ```
3. Install requirements via pip
    ```commandline 
    pip install -r requirements.txt
    ```
4. Run docker-compose
    ```bash
    docker-compose up --build
    ```
---
</details>

### Finally:

[View endpoints][docs]

---

### Usage:

*GET  /api/ping/* - checking application availability

*POST /api/v1/questions/* - receive the body with number questions for further downloading, return the last uploaded question

<details><summary>Request example</summary>

```json lines
{
    "questions_num": 5
}
```

</details>

<details><summary>Response example</summary>

```json lines
{
  "question": "Sandburg called Chicago the \"City of Big\" these",
  "answer": "Shoulders",
  "created_at": "2022-12-30T19:21:03.128000Z"
}
```
</details>

<!-- links -->

[docs]: http://127.0.0.1:8000/docs