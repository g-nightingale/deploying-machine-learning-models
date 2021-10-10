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

    ![Image](images/image.png)