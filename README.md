# The `skippy` python package

Skip the boilerplate of scikit-learn machine learning examples.

## Installation
```bash
pip install skippy
```

# Usage
Simplify code to a single function call per step:
```python
from sklearn.metrics import confusion_matrix, accuracy_score
import skippy as skp

data = skp.get_data('digits')
x_train, x_test, y_train, y_test = skp.split_data(data)

model = skp.get_model(model_type='ensemble',
                      model_name='RandomForestClassifier')

fit = model.fit(x_train, y_train)
skp.pickle_model(filename='digits_rf.pickle', model=fit)
predictions = fit.predict(x_test)

confmat = confusion_matrix(y_true=y_test, y_pred=predictions)
accuracy = accuracy_score(y_true=y_test, y_pred=predictions)

skp.confusion_matrix_plot(cm=confmat,
                          acc=accuracy,
                          filename='digits_rf.png')
```

Or run a whole pipeline with one function:

```python
import skippy as skp

skp.classification(dataset='digits',
                   model_type='ensemble',
                   model_name='RandomForestClassifier',
                   pickle_name='digits_rf.pickle',
                   plot_name='digits_rf.png')
```

For inspiration, look at the example pipelines in the
[pipelines folder](https://github.com/marskar/skippy/tree/master/pipelines)
of the
[skippy repo](https://github.com/marskar/skippy).
