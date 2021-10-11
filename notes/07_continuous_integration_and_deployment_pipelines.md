# Continuous integration and deployment pipelines

## 8.2 Introduction to CI / CD
- Continuous integration and continuous deployment
    - Continuous integration
        - Build → Test → Merge
    - Continuous Delivery
        - Automatically release to repository
    - Continuous Deployment
        - Automatically deploy to production
- Why does this matter?
    - The system is always in a releasable state
    - Faster, regular release cycles
         - Many small changes reduces the chances of breaking something
    - Building and testing is automated
        - Reduces changes of human error
    - Delivery and deployments are automated (at least to some extent)
    - Visibility across the company (and audit log)
- Circle CI
    - Hosted platform
    - Easy GitHub integration
    - One free project
    - Many great features
    - Trusted by many top companies
- Alternatives to Circle CLI
    - Jenkins
    - Travis CI
    - Bamboo
    - Gitlab CI
    - Team City

## 8.4 Understanding CI / CD Automation 1
- Environment variables need to be added in CircleCI
    - HEROKU_API_KEY
    - HEROKU_APP_NAME
    - PIP_EXTRA_INDEX_URL
- Heroku environmental variables
    - PIP_EXTRA_INDEX_URL

## 8.5 CI / CD Config
- config.yml
    - workflows section near bottom
        - Defines the sequence in which jobs will be run
        - Run tests for API
        - Deploy API to Heroku
- Jobs are defined in jobs block of the config.yml file
- Need to add environmental variables to CircleCI:
    - HEROKU_APP_NAME
    - HEROKU_API_KEY

## 8.6 CI / CD Automation 2
- In some cases we might want to publish a private package to a private index server
    - Sensitive intellectual property
- Gemfury
    - Managed file server
    - Free trial
- Location of private package added to requirements.txt
    - --extra-index-url=${PIP_EXTRA_INDEX_URL}
- CircleCI additional environmental variables
    - PIP_EXTRA_INDEX_URL
    - KAGGLE_KEY
    - KAGGLE_USERNAME
    - GEMFURY_PUSH_URL → Same as PIP_EXTRA_INDEX_URL (but could have different access levels)
- Heroku additional environmental variables
    - PIP_EXTRA_INDEX_URL
- Best practice NOT TO STORE DATA IN REPO
- Conceptual understanding is important
    - Try not to focus too much on specific technologies

## 8.7 Using a Private Index Server
- Workflow
    1. Make some kind of change to model package
    2. Bump the version
    3. Open a pull request
    4. Tests will run
    5. Merge pull request and create a tag
    6. Tag triggers a publish job



    ![Image](images/image.png)