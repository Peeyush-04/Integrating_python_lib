def is_classifier(x):
    '''x = estimator
    Check if the estimator is a classifier.

    Parameters
    ----------
    estimator : object
        The estimator object to check.

    Returns
    -------
    is_cls : bool
        True if the estimator is a classifier, False otherwise.
    '''
    if hasattr(x, "predict_proba"):
        return True
    else:
        return False
    
def is_regressor(x):
    '''x = estimator
    Check if the estimator is a regressor.

    Parameters
    ----------
    estimator : object
        The estimator object to check.

    Returns
    -------
    is_reg : bool
        True if the estimator is a regressor, False otherwise.
        '''
    if hasattr(x, "predict"):
        if not hasattr(x, "predict_proba"):
            return True
    return False