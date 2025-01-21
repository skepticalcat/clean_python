import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    f1_score,
)



def load_data_from_csv() -> pd.DataFrame:
    raw_data = pd.read_csv("data/mushroom_cleaned.csv")

    # class 1: will kill you, class 0: edible, we thus rename the class column to poisonous to make that clearer
    return raw_data.rename(columns={"class": "poisonous"})


def print_data_description(dataframe: pd.DataFrame):
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    print(dataframe.describe())
    print(dataframe["poisonous"].value_counts())

def extract_labels_from_dataframe(dataframe: pd.DataFrame, column_name_label: str) -> tuple:
    # X and Y are common variable names for data / labels, thats why we just stick with them here
    Y = dataframe[column_name_label]
    X = dataframe.drop(column_name_label, axis=1)
    return X, Y

def print_accuracy_and_f1_score(model, X_test, Y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_pred, Y_test)
    f1 = f1_score(y_pred, Y_test, average="weighted")

    print("Accuracy:", accuracy)
    print("F1 Score:", f1)

mushroom_data = load_data_from_csv()
print_data_description(mushroom_data)


# we can omit stratifying the data because the class distribution is quite good
X_train, X_test = train_test_split(mushroom_data, test_size=.2)

X_train, Y_train = extract_labels_from_dataframe(X_train, "poisonous")
X_test, Y_test = extract_labels_from_dataframe(X_test, "poisonous")

model = GaussianNB()
model.fit(X_train, Y_train)

print_accuracy_and_f1_score(model, X_test, Y_test)


# results of the naive bayes are not good, we also test RFC:
random_forest_clf = RandomForestClassifier(n_estimators=10)
random_forest_clf.fit(X_train, Y_train)

print_accuracy_and_f1_score(random_forest_clf, X_test, Y_test)



