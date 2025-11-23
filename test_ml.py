import pandas as pd
from ml.data import process_data


# Completed: implement the first test. Change the function name and input as needed
def test_one():
    """
    # Test that process_data returns X, y, encoder, lb with correct lengths.
    """
    # Code for test_one below:
    sample = pd.DataFrame({
        "workclass": ["Private", "Self-emp-not-inc"],
        "education": ["Bachelors", "HS-grad"],
        "marital-status": ["Never-married", "Married-civ-spouse"],
        "occupation": ["Adm-clerical", "Exec-managerial"],
        "relationship": ["Not-in-family", "Husband"],
        "race": ["White", "White"],
        "sex": ["Male", "Male"],
        "native-country": ["United-States", "United-States"],
        "salary": ["<=50K", ">50K"],
    })

    cat_features = [
        "workclass", "education", "marital-status", "occupation",
        "relationship", "race", "sex", "native-country"
    ]

    X, y, encoder, lb = process_data(
        sample, categorical_features=cat_features, label="salary", training=True
    )

    assert len(X) == 2
    assert len(y) == 2
    assert encoder is not None
    assert lb is not None


# Completed: implement the second test. Change the function name and input as needed
def test_two():
    """
    # Test that train_model returns a fitted model.
    """
    # Code for test_two below:
    import numpy as np
    from ml.model import train_model

    X = np.array([[0, 1], [1, 0]])
    y = np.array([0, 1])

    model = train_model(X, y)

    assert hasattr(model, "predict")
    preds = model.predict(X)
    assert len(preds) == 2


# Completed: implement the third test. Change the function name and input as needed
def test_three():
    """
    # Test that inference returns predictions of the expected length.
    """
    # Code for test_three below:
    import numpy as np
    from ml.model import train_model, inference

    X = np.array([[0, 1], [1, 0]])
    y = np.array([1, 0])

    model = train_model(X, y)
    preds = inference(model, X)

    assert len(preds) == 2
    assert preds.dtype in [np.int64, np.int32, np.float64, np.float32]
