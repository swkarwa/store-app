# Stores REST API

A RESTful API built with Flask for managing stores, items, and tags with JWT authentication.

## Features

- **Store Management** - Create, read, update, delete stores
- **Item Management** - CRUD operations for items within stores
- **Tag System** - Organize items with tags, link/unlink tags to items
- **User Authentication** - Register, login with JWT tokens
- **API Documentation** - Interactive Swagger UI

## Tech Stack

- Flask & Flask-Smorest
- SQLAlchemy & Flask-SQLAlchemy
- Flask-JWT-Extended (Authentication)
- Flask-Migrate (Database migrations)
- Passlib (Password hashing)
- SQLite (Default database)

## Setup

### 1. Clone and navigate to project

```bash
cd store-app
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```bash
# Generate a secure secret key
echo "JWT_SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(32))')" > .env
```

Or manually create `.env`:

```
JWT_SECRET_KEY=your-super-secret-key-here
```

> ⚠️ **Important**: Never commit `.env` to version control. It contains secrets.

### 5. (Optional) Configure database

By default, SQLite is used. To use a different database, add to `.env`:

```
DB_URL=postgresql://user:password@localhost/dbname
```

## Running the Application

### Development mode

```bash
flask run
```

The API will be available at `http://localhost:5000`

### Alternative: Run directly

```bash
python app.py
```

## Database Migrations

Initialize migrations (first time only):

```bash
flask db init
```

Create a migration after model changes:

```bash
flask db migrate -m "Description of changes"
```

Apply migrations:

```bash
flask db upgrade
```

## API Documentation (Swagger)

Once the app is running, access the interactive API documentation at:

**📖 Swagger UI: [http://localhost:5000/api/swagger](http://localhost:5000/api/swagger)**

The Swagger interface allows you to:
- Browse all available endpoints
- View request/response schemas
- Test API calls directly from the browser
