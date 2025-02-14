import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    f1_score,
)
# get the data
raw_data = pd.read_csv("data/mushroom_cleaned.csv")

# class 1: will kill you, class 0: edible
# lets make that a bit clearer in the dataframe
mushroom_data = raw_data.rename(columns={"class": "poisonous"})



# checking what kind of data we're seeing in the dataframe
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
print(mushroom_data.describe())
# whats the class distribution?
print(mushroom_data["poisonous"].value_counts())


# extract the class from the df and make it a numpy array
#np_mush = mushroom_data.to_numpy()
# x_train = np_mush[,:5]
# y_train = np_mush[,:6]

# split the data
# we can omit stratifying the data because the class distribution is quite good
X_train, X_test = train_test_split(mushroom_data, test_size=.2)
# now we need to extract the labels obviously, haha. Need also to make sure not to leave the labels in the training data
Y_train = X_train["poisonous"]
X_train.drop("poisonous", axis=1, inplace=True)
Y_test = X_test["poisonous"]
X_test.drop("poisonous", axis=1, inplace=True)

# build a Gaussian Classifier
model = GaussianNB()

# model training
model.fit(X_train, Y_train)

# calculate acc and f1 score:
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_pred, Y_test)
f1 = f1_score(y_pred, Y_test, average="weighted")

print("Accuracy:", accuracy)
print("F1 Score:", f1)

### waaaay to bad, lets try something else
random_forest_clf = RandomForestClassifier(n_estimators=10)
random_forest_clf.fit(X_train, Y_train)

y_pred = random_forest_clf.predict(X_test)
accuracy = accuracy_score(y_pred, Y_test)
f1 = f1_score(y_pred, Y_test, average="weighted")

print("Accuracy:", accuracy)
print("F1 Score:", f1)



