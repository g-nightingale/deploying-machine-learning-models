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
     - Responsible for incoming requests and outgoing responses at a low level
     - Dedicated web servers can handle much higher loads
     - A server implements a "server gateway interface"
- Uvicorn is an implementation of the Asynchronous Server Gateway Interface (ASGI)
    - Spiritual successor to WSGI (Web Server Gateway Interface → introduced in PEP 333)
    - Uses asynchronous applications → much faster
- When running a web application in production, it's really important to have a web server

## 7.8 Introducing Heroku and Platform as a Service (PaaS)
- "A cloud-based service that provides a platform allowing customers to develop, run, and manage applications without the complexity of building and maintaining the infrastructure typically associated with developing and launching an app"
- Understanding the range of possibilities

    ![Image](images/paas.png)

- On-Premises
    - Server racks in buildings → control everything
    - Useful when there are extremely high security and performance requirements
    - Maintaining legacy systems
- Infrastructure as a Service
    - Running in the cloud using a provider such as AWS, GCP, Azure
    - Don't have to worry about taking care of the actual hardware
- Platform as a Service
    - Also runs in the cloud
    - Don't have to worry about configuring OS, Middleware, Runtime etc
    - Simplifies the process
- Software as a Service
    - Completely managed, no control over
- PaaS Pros and Cons
    | Pros                                   | Cons                                            |
    | ---------------------------------------| ----------------------------------------------- |
    | Simple to setup, maintain and deploy   | Hard / impossible to scale to a very large size |
    | Easy to scale to moderate size         | Tends to be more expensive than IaaS            |
    | Allows developers to focus on apps     | Vulnerable to PaaS downtime                     |
    | Easy creation of dev/test environments | Limitations on configuration                    |

- Why use Heroku in this course?
    - Very easy to use
    - Can use Heroku Dyno for free
    - Nice 3rd party add on options
    - Works with Docker
    - Great documentation
    - Supports multiple languages

## 7.9 Deploying our Application to Heroku
- Git subtree push
    - Push a specific subdirectory
- Command line → heroku logs --tail
    - Get the last logs
- Heroku free tier is not suitable for a serious production application 

## 8.0 Understanding the Heroku specific project files
- Procfile
    - Heroku requirement
    - Specifies commands to run our app
    - Heroku dynamically assigns a port, therefore we don't need to specify a port
- runtime.txt
    - Specify what version of Python we are going to use
- requirements.txt
    - By default, Heroku looks for a requirements.txt file
    - It won't install our test_requirements.txt
