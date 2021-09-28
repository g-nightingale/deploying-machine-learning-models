# Research environment - developing a machine learning model

## 2.4 Research environment - process overview
- Need to deploy the entire machine learning pipeline, and not the machine learning model
- Build in-house software if a python library is not available to do the thing we want to do

## 2.5 Machine learning model pipeline: overview
- Gathering data sources
- Data analysis
- Data pre-processing
- Variable selection
- Machine learning model building
- Model monitoring  

- Need to deploy at least the following steps of the pipeline:
    - Data pre-processing
    - Variable selection
    - Machine learning model building

## 2.6 Feature engineering - Variable characteristics
- Missing values
    - Random or systematic
- Categorical variables
    - High cardinality
    - Rare labels
    - Strings
- Variable distribution
    - Gaussian or not
- Outliers
    - Linear regression and Adaboost are sensitive to outliers
- Feature scale
    - Linear regression/logistic regression, SVMs, neural nets and distance based algorithms are sensitive to feature scale

## 2.7 Feature engineering techniques
- Transform variables
- Extract features
- Create new features

## 2.8 Feature selection
- Finding best subset of features from all features in dataset
- Simpler models are easier to interpret
- Shorter training and scoring times
- Enhanced generalisation, less risk of overfitting
- Less time to train/score
- Easier to implement by software developers
- Data redundancy

### Reducing features for model deployment
- Smaller json messages sent to the model
- Less code for unit testing features
- Less information to log
- Less feature engineering code

### Variable redundancy
- Constant variables
- Quasi-constant variables
- Duplication
- Correlation
 
 ### Feature selection methods
 - Filter methods
 - Wrapper methods
  - Embedded methods
    - Lasso regression
    - Feature importance from tree-based algorithms
- Features selected in training before implementing in the pipeline

## 2.9 Training a machine learning model
- Data → prediction
    - Linear models
    - Tree models
    - Neural networks
- Performance
    - ROC-AUC
        - For each probability value:
            - How many times the model made a good assessment vs how many times the model made a bad assessment
    - Accuracy
    - MSE, RMSE, etc
- Model stacking - meta ensembling

## 3.0 - 4.2 Note book activities

## 4.3 Python open source for machine learning
- Scikit-Learn
    - Estimators
        - A class with fit() and predict() methods
    - Transformers
        - A class with fit() and transform() methods
            - Scalers
            - Feature selectors
            - Encoders
            - Imputers
            - Discretizers
            - Transfomers
    - Pipeline
        - A class that allows to run transformers and estimators in sequence
        - Most steps are transformers
        - Last step can be an estimator

            ![Image](images/pipeline.png)

- Open-source libraries for feature engineering
    - Scikit-Learn
    - Category Encoders
    - Feature-engine
    - Featuretools
    - Imbalanced-learn

- Open-source libraries for feature selection
    - Scikit-Learn
    - Feature-engine
    - MLXtend

## 4.4 Open-source libraries for feature engineering
- Scikit-Learn runs on top of Numpy, so it is very fast
- Feature engine 
- Category Encoders
    - For encoding categorical variables

- model_pipe = Pipeline([('trans1', transformer1()), ('trans2', transformer2()),, ('trans3', transformer3()), ('gbm', gradient_boosting()),])
- mode_pipe.fit(x_train, y_train)
- mode_pipe.predictr(x_train)

- Save entire pipeline in one Pickle

## 4.7 Intro to OOP
- Procedural programming seems straightforward, but it has its shortcomings
- Object oriented programming (OOP)
    - Objects store data and can also store instructions or procedures to modify that data or do other things
    - Data → attributes
    - Code → methods
- Have both parameters and functions

## 4.8 OOP - inheritance
- Inheritance in the process by which one class takes on the atttributes and methods of another
- Parent class → child class
    - class MeanImputer(TransformerMixin)
    - Child class automatically inherits methods of parent class → for example fit_transform() from TransformerMixin
- Sckit-Learn has base classes that we can leverage:
    - BaseEstimator
    - TransformerMixin
    - Etc

## 5.2 Should feature selection be part of the pipeline?
- Suitable
    - Model build and refreshed on the same data
    - Model build and refreshed on smaller datasets
- Not suitable
    - If model built using datasets with a high feature space → large amount of feature engineering code required
    - If model constantly enriched with new data sources









 


