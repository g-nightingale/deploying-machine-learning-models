# Serving and deploying the model via REST API

## 7.2 Understanding the architecture of the API
- API is a contract between an information provider and an information user
- REST API is a type of contract
    - A set of rules that both parties adhere to
- How can our API be consumed?
    - Web browsers
    - Mobile devices
    - IOT connected devices
    - Other applications
- Modern frontend approaches would use JS frameworks like ReactJS, Vue and AngularJS
- Ajax

## 7.3 Introduction to FastAPI
- Web development framework
    - Tools to handle & automate standard tasks when building web applications
        - Session management
        - Templating
        - Database access
        - Much more!
    - Flask and Django are the most popular
    - FastAPI is rapidly gaining popularity
- Features of FastAPI
    - It's fast - leverages Python async capabilities
        - Very fast performance compared with NodeJS or GoLang
    - Validation with type hints and Pydantic
    - Automatic documentation
    - Dependency injection
    - Much more!
- Future of web development in Python
- Really good documentation

## 7.5 Using Schemas in our API
- Fast API can convert inputs to the correct type according to a schema
    - Input passed as string but should be an integer according to schema

## 7.6 Logging
- Critical to understanding what's happening on our server
- Can't rely on print statements
    - Need to persist any information that we capture
- Use Python logging library
- Specify logging level
- Loguru simplifies configuration for logging

## 7.7 The Uvicorn Web Server
- Production → need dedicated web server
- Uvicorn is an implementation of the Asynchronous Server Gateway Interface (ASGI)
    - Spiritual successor to WSGI
    - Uses asynchronous applications → much faster