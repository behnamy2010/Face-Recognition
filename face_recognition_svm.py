# -*- coding: utf-8 -*-
"""Face_Recognition_SVM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nq_MgIb3M4OfPRNbikLE8acI2xb-4OdZ
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from sklearn.datasets import fetch_lfw_people

faces = fetch_lfw_people(min_faces_per_person=50)
print(faces.target_names)
print(faces.images.shape)

from sklearn.svm import SVC

#Using randomized PCA
from sklearn.decomposition import PCA as RandomizedPCA
from sklearn.pipeline import make_pipeline

#preprocessing and classifier in the same package
pca = RandomizedPCA(n_components=150, whiten=True, random_state=42)
svc = SVC()
model = make_pipeline(pca, svc)

from sklearn.model_selection import train_test_split

Xtrain, Xtest, ytrain, ytest = train_test_split(faces.data, faces.target,test_size=0.20, random_state=42)

from sklearn.model_selection import GridSearchCV

param_grid = {'svc__C': [1, 5, 10,50], 'svc__gamma': [0.0001, 0.0005, 0.001, 0.005]}

grid = GridSearchCV(model, param_grid)

grid.fit(Xtrain, ytrain) 

print(grid.best_params_)

model = grid.best_estimator_
yfit = model.predict(Xtest)

from sklearn.metrics import classification_report

print(classification_report(ytest, yfit, target_names=faces.target_names))