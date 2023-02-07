import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle


# Reading data

df = pd.read_csv('data.csv')
# print(df.head())
# print(df.tail())

# print(df.info())

# print(df['diffBreath'].value_counts())
# print(df.describe())

# Train test Spliting
def data_split(data, ratio):
    np.random.seed(42)

    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

# print(len(df))
# shuffled = np.random.permutation(len(df))
# print(shuffled)
# test_set_size = int(len(df) * 0.2)
# print(test_set_size)
# test_indices = shuffled[:test_set_size]
# print(test_indices)
# train_indices = shuffled[test_set_size:]
# print(train_indices)

if __name__=="__main__":
    train, test = data_split(df, 0.2)

    print(train)
    print(test)

    X_train = train[['fever', 'bodypain', 'Age', 'runnyNose', 'diffBreath']].to_numpy()
    print(X_train)

    X_test = test[['fever', 'bodypain', 'Age', 'runnyNose', 'diffBreath']].to_numpy()
    print(X_test)

    Y_train = train[['infectionProb']].to_numpy().reshape(13, )
    print(Y_train)

    Y_test = test[['infectionProb']].to_numpy().reshape(3, )

    # print(Y_train)
    # print(Y_test)

    clf = LogisticRegression()
    # print(clf)
    # print(clf.fit)
    print(clf.fit(X_train, Y_train))

    with open('model.pkl', 'wb') as file:
        pickle.dump(clf, file)

    # Code for inference
    # infProb = clf.predict_proba([[90, 0, 18, 0, 0]])[0][1]
    # print(infProb)
    # print(int(infProb*100))
    