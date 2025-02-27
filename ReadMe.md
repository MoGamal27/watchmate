# Django Watchlist API

This project is a Django REST Framework (DRF) based API for managing a watchlist of movies/shows, user reviews, and streaming platforms. It includes features like user authentication, token-based authorization, filtering, pagination, and more.

---

## Features

1. **User Authentication**:
   - User registration with email and password.
   - Token-based authentication for secure API access.
   - Logout functionality to invalidate tokens.

2. **Watchlist Management**:
   - Add, update, delete, and retrieve movies/shows.
   - Associate movies/shows with streaming platforms.

3. **Review Management**:
   - Add, update, delete, and retrieve reviews for movies/shows.
   - Restrict review updates/deletions to the review author.

4. **Stream Platform Management**:
   - Add, update, delete, and retrieve streaming platforms.

5. **Advanced Features**:
   - Filtering, searching, and ordering of movies/shows.
   - Pagination for large datasets.
   - Throttling to limit API requests.

## Api Documentation

### 1. User Authentication
- **Register a User:**
  - **POST** `/account/register/`
  - **Request Body:**
    ```json
    {
      "username": "new-user",
      "email": "new-user@example.com",
      "password": "password123",
      "password2": "password123"
    }
    ```

- **Login:**
  - **POST** `/account/login/`
  - **Request Body:**
    ```json
    {
      "username": "your-username",
      "password": "your-password"
    }
    ```

- **Logout:**
  - **POST** `/account/logout/`
  - **Headers:**
    ```
    Authorization: Token your-auth-token
    ```

### 2. Watchlist Management
- **Get All Movies/Shows:**
  - **GET** `/watch/list/`

- **Get Movie/Show Detail:**
  - **GET** `/watch/<int:pk>/`

- **Create a Movie/Show:**
  - **POST** `/watch/list/`
  - **Request Body:**
    ```json
    {
      "title": "Inception",
      "storyline": "A mind-bending movie",
      "platform": 1,
      "active": true
    }
    ```

### 3. Review Management
- **Create a Review:**
  - **POST** `/watch/<int:pk>/review-create/`
  - **Request Body:**
    ```json
    {
      "rating": 5,
      "description": "Great movie!"
    }
    ```

- **Get Reviews for a Movie/Show:**
  - **GET** `/watch/<int:pk>/reviews/`

- **Get Review Detail:**
  - **GET** `/review/<int:pk>/`

- **Get Reviews by User:**
  - **GET** `/reviews/?username=<username>`

### 4. Stream Platform Management
- **Get All Stream Platforms:**
  - **GET** `/stream/`

- **Get Stream Platform Detail:**
  - **GET** `/stream/<int:pk>/`



