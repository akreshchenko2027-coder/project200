# Платформа онлайн-навчання (Online Learning Platform)

Проєкт розроблено в рамках дисципліни «Розробка клієнт-серверних застосунків» (Етап 1).

## Стек технологій
- **Python 3.11+**
- **Django 5.0+**
- **Django REST Framework**

## Запуск проєкту локально

1. Клонувати репозиторій:
   ```bash
   git clone [https://github.com/akreshchenko2027-coder/project200.git](https://github.com/akreshchenko2027-coder/project200.git)
   cd project200
   
   ## Domain Overview & ER Diagram

```mermaid
erDiagram
    USER ||--o{ COURSE : "creates / teaches"
    USER ||--o{ ENROLLMENT : "enrolls"
    COURSE ||--o{ LESSON : "contains"
    COURSE ||--o{ ENROLLMENT : "has"
    LESSON ||--o| QUIZ : "has"
    USER ||--o{ PROGRESS : "tracks"
    LESSON ||--o{ PROGRESS : "recorded_in"

    USER {
        int id PK
        string email
        string username
        string role "admin | teacher | student"
    }
    COURSE {
        int id PK
        string title
        text description
        int teacher_id FK
        datetime created_at
    }
    LESSON {
        int id PK
        int course_id FK
        string title
        text content
        int order
    }
    ENROLLMENT {
        int id PK
        int student_id FK
        int course_id FK
        datetime enrolled_at
    }
    QUIZ {
        int id PK
        int lesson_id FK
        string title
        int max_score
    }
    PROGRESS {
        int id PK
        int student_id FK
        int lesson_id FK
        boolean is_completed
        datetime completed_at
    }