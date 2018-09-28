from split_data import split_data
from sklearn.metrics import confusion_matrix, accuracy_score
from matplotlib import pyplot as plt
import pickle

def load_model():
    with open('model.pickle', 'rb') as f:
        return pickle.load(f)

x_train, x_test, y_train, y_test = split_data()

predicted = model.predict(x_test)

# evaluate the model
cm = confusion_matrix(y_test, predicted)
a = accuracy_score(y_test, predicted)


fig, ax = plt.subplots()
colorbar = ax.matshow(cm)
fig.colorbar(colorbar)
fig.suptitle("Confusion Matrix")
fig.subtitle("Accuracy = ")
fig.savefig('cm.png')

# In addition to saving the plot, you can show it
plt.show()
