import pickle
with open('RF.pkl', 'rb') as model_file:
    mp = pickle.load(model_file)
mp.decision_path(X_test)