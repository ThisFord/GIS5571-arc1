# -*- coding: utf-8 -*-
"""

Original file is located at
    https://colab.research.google.com/drive/1GO7B1-nnrdVu82Lt9_BT3-2vNOrh6IWB
"""

!pip install tensorflow_addons

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
import tensorflow_datasets as tfds
import tensorflow_hub as hub
import tensorflow_addons as tfa

# Loading a dataset, for this example we will be using the eurosat data from TensorFlow datasets as a starting point
dataset = tfds.load('eurosat', with_info = True)

# We are going to train at 70%
train_ds = tfds.load('eurosat', split='train[:70%]')
#test_ds = tfds.load('eurosat', split='train[60%:80%]')
valid_ds = tfds.load('eurosat', split='train[30%:]')

# Here we are initializing our class names, number of classes, and the examples that we will have
class_names = dataset[1].features['label'].names
num_classes = len(class_names)
num_examples = dataset[1].splits['train'].num_examples

# Preparing to train the model
def trainprep(ds, cache=True, batch_size=64, shuffle_buffer_size=1000):

  # Cache is a method that saves the preprocessed dataset into a local cache
  # Only preprocesses it for the very first time in the 1st epoch
  if cache:
    if isinstance(cache, str):
      ds = ds.cache(cache)
    else:
      ds = ds.cache()

  # Maps the dataset so that each sample is a tuple of an image
  ds = ds.map(lambda d: (d["image"], tf.one_hot(d["label"], num_classes)))

  # Shuffles the dataset so the samples are random
  ds = ds.shuffle(buffer_size=shuffle_buffer_size)

  # Every time we iterate through, it'll repeatedly generate samples
  ds = ds.repeat()

  # Batch our DS into 64 or 32 samples per training step
  ds = ds.batch(batch_size)
  
  # `prefetch` lets the dataset fetch batches in the background while the model
  # is training.
  ds = ds.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
  return ds

batch_size = 64

train_ds = trainprep(train_ds, batch_size=batch_size)
valid_ds = trainprep(valid_ds, batch_size=batch_size)

batch = next(iter(train_ds))

def show_batch(batch):
  plt.figure(figsize=(16, 16))

  for n in range(min(32, batch_size)):
      ax = plt.subplot(batch_size//8, 8, n + 1)
      plt.imshow(batch[0][n])
      plt.title(class_names[tf.argmax(batch[1][n].numpy())])
      plt.axis('off')
      plt.savefig("sample-images.png")


show_batch(batch)