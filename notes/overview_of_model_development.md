# Overview of model development

## 1.1 Deployment of machine learning models
- Process of making models available in production environments, where they can provide predictions to other software systems
- Potentiall the most challenging stage of the machine learning life cycle

### Why is model deployment challenging?
- Challenges of traditional software
    - Reliability
    - Reuseability
    - Maintainability
    - FLexibility
- Additional challenges specific to Machine Learning
    - Reproducibility 
- Needs the co-ordination of various teams: data science, IT, business professionals
- Discrepency between programming language used to build a model and the production system language

### Why is model deployment important?
- To use a machine learning model, it needs to be deployed into production so that predictions can be supplied to other systems

## 1.2 Deployment of machine learning pipelines
### Data format and quality
- Missing values, text data, variable distributions, outliers, variable scales, images
- Pipeline
    - data → feature engineering → feature selection → mode building → selection

## 1.3 Research and production environments
- Environment: The setting or state of a computer where software or other products are developed or put in operation

### Research environment
- Contains the tools, programs and software suitable for data analysis and the development of machine learning models
- Here, we develop the ML models and identify their value

### Production environment
- The production enviroment is a real-time setting with running programs and hardware setups that allow the organization's daily operations
- It is the place where ML models are available for business use
- Allows organisations to show clients a "live" service

**The tools, software and hardware used in research and production environments are not the same, as they serve different purposes**

## 1.4 Building reproducible machine learning pipelines
- Machine learning pipeline
    - Series of steps that need to occur from the moment we receive the data to the moment we produce a prediction
- We create an entire piepline in the research environment, which needs to be output to the production envrionment
- Pipelines in production must be reproducible
    - Live model must reproduce exactly the model created in the research environment

## Why reproducibility matters?
- Financial costs
- Lost time
- Lost reputation

- Without the ability to replicate prior results, it is difficult to determine if a new model is truly better than the previous one

## 1.5 Challenges to reproducibility
- Reproducibility is the ability to duplicate a machine learnnning model exactly, such that given the same raw data as inout, both models return the same output
- ML pipeline overview:
    - Gathering data sources → data anlysis → data pre-processing → variable selection → machine learning model building → model deployment
    - All steps should be reproducible! (except maybe data analysis)
- Data
    - The most difficult challenge to reproducibility
    - Save a snapshot of the training data to load into production
        - Potential conflict with GDPR
    - Design data sources with accurate timestamps

### Reproducibility during feature creation
- Feature creation should be tracked under version control 
- Many features depend on the data used for training → ensure data is reproducible
- If using processes with randomisation, always set a seed!

### Reproducibility during model training 
- Challenges
    - ML models rely on randomness for training
    - ML model implementations work with arrays agnostic to feature names

- Solutions
    - Record the order of features
    - Record applied features transformations
    - Record hyperparameters
    - For models that require randomness, always set a seed
    - If the final model is a stack of models, record the structure of the ensemble

### Reproducibility during model deployment
- Challenges
    - Feature is not available in the live environment
    - Different programming languages
    - Different software
    - Live populations don't match those used for training
- Solutions
    - Software versions should match exactly (Python packages)
    - Use a container and track software specifications
    - Research, develop and deploy utilising the same language, r.g., python
    - Prior to building the model, understand how the model will be integrated with other systems

### Streamlining model deployment with open-source
- Challenges
    - A lot of code
        - Time consuming
        - Different versions across teams
    - Repetitive
        - Multiple copies of same code
        - Different versions of same code
        - Difficult to keep track ot latest version
    - Learn and store parameters
        - Multiple intermediate files with parameters
        - Config or params file
    - Reproduciblity
        - Re-write code for production
        - Include tests
        - Reproduciblity

### Team performance
- Decreased performance
- Frustration
- Lack of reproducibility
- Increased deployment times

### Open source
- Increase performance
- Prevent frustration
- Maximise reproducibility
- Minimise deployment times
- Less coding
- Version tracking for reproducibility
- Classes and functions include tests - no need to record for production

    ![Image](images/ml_pipelines.png)


