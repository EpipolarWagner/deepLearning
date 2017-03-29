# These are all the modules we'll be using later. Make sure you can import them
# before proceeding further.
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import tarfile
from IPython.display import display, Image
from scipy import ndimage
from sklearn.linear_model import LogisticRegression
from six.moves.urllib.request import urlretrieve
from six.moves import cPickle as pickle

# Config the matplotlib backend as plotting inline in IPython
#%matplotlib inline
print(2+2)

data_root = '.'

pickle_file = os.path.join(data_root, 'notMNIST.pickle')
with open(pickle_file,'rb') as opn:
    letter_class=pickle.load(opn)

# Prepare training data
samples, width, height = letter_class['train_dataset'].shape
X_train = np.reshape(letter_class['train_dataset'],(samples,width*height))
y_train = letter_class['train_labels']

# Prepare testing data
samples, width, height = letter_class['test_dataset'].shape
X_test = np.reshape(letter_class['test_dataset'],(samples,width*height))
y_test = letter_class['test_labels']
# Import
from sklearn.linear_model import LogisticRegression

# Instantiate
#lg = LogisticRegression(multi_class='multinomial', solver='lbfgs', random_state=42, verbose=1, max_iter=1000, n_jobs=-1)
lg=LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver='liblinear', max_iter=100, multi_class='ovr', verbose=0, warm_start=False, n_jobs=1)
# Fit
lg.fit(X_train, y_train)

y_pred = lg.predict(X_test)

# Score
from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred))
