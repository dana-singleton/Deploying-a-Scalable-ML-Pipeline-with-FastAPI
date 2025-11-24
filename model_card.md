# Model Card

## Model Details
This project trains a basic machine learning model to predict whether someone makes more than $50K a year using the Census Income dataset.
The model and encoder are trained in `train_model.py` and saved in the `model/` folder.
For predictions, the FastAPI app in `main.py` loads the saved model and processes incoming data.

## Intended Use
This model is only meant for learning and practice as part of the Udacity ML DevOps Nanodegree.
It’s here to show how to:
- preprocess data
- train and test a model
- compute slice metrics
- run unit tests and CI
- deploy a simple ML API

It should **not** be used for any real-world decisions.

## Training Data
The training data comes from the modified Adult Census Income dataset that Udacity provides.
It includes things like age, race, education level, occupation, hours worked, etc.
Categorical features are one-hot encoded using the encoder saved in `model/encoder.pkl`.

## Evaluation Data
The model is evaluated on a held-out test split from the same dataset.
The same preprocessing (encoder + label binarizer) is applied during testing.
Slice-based metrics for one categorical feature are also created and saved in `slice_output.txt`.

## Metrics
Here are the main metrics from my model:

- **Precision:** 0.7419
- **Recall:** 0.6384
- **F1 Score:** 0.6863

These come from running `train_model.py`.

## Ethical Considerations
Because the dataset includes sensitive features like race and sex, the model can reflect bias that exists in the data.
Some slices may have better or worse performance.
This is why the model is for practice only and shouldn’t be used for anything important.

## Caveats and Recommendations
This is not a production model.
- It hasn’t been checked for fairness, drift, or stability.
- If the data changes, the model should be retrained by running `train_model.py` again.
- Any real deployment would need more testing and monitoring.
