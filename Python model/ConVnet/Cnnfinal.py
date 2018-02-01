# -*- coding: utf-8 -*-
"""
Spyder Editor

By John Kenny
Convolutional Neural Nework Training model

"""

#import coremltools

#import keras
#import tensorflow


#Building the CNN

#importing Keras libs and packages





from keras.preprocessing.image import ImageDataGenerator   
from keras.models import Sequential   
from keras.layers import Conv2D, MaxPooling2D   
from keras.layers import Activation, Dropout, Flatten, Dense   
from keras import backend as K  




batch = 5
size = 250 

#initialise the cnn
classifier = Sequential()

#Convolution layer

#32 feature dectors with dimentions 3*3
classifier.add(Conv2D(32, (3, 3), input_shape=(250, 250, 3)))   
classifier.add(Activation('relu'))   


#pooling layer

#used to reduce the size of the feature map- reducing num of nodes and complexity 
classifier.add(MaxPooling2D(pool_size=(2, 2)))

#add an extra con layer

classifier.add(Conv2D(32, (3, 3)))   
classifier.add(Activation('relu')) 
classifier.add(MaxPooling2D(pool_size=(2, 2)))

#add an extra con layer

classifier.add(Conv2D(32, (3, 3)))   
classifier.add(Activation('relu')) 
classifier.add(MaxPooling2D(pool_size=(2, 2)))

#add an extra con layer

classifier.add(Conv2D(32, (3, 3)))   
classifier.add(Activation('relu')) 
classifier.add(MaxPooling2D(pool_size=(2, 2)))

#add an extra con layer

classifier.add(Conv2D(32, (3, 3)))   
classifier.add(Activation('relu')) 
classifier.add(MaxPooling2D(pool_size=(2, 2)))




#flatten layer

#puts all the feature maps in one single vector
classifier.add(Flatten())


# full connection of layers

#128 nodes
classifier.add(Dense(units = 5000, activation = "relu"))
 #only 2 (sigmoid) other wise sofmax is needed 
classifier.add(Dense(units = 20, activation = "softmax"))

from keras.optimizers import Optimizer


optimizer = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-8)

#compiling the CNN

#without binary outcome crossentropy is needed
classifier.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# adding images to cnn

#image preprocessing
from keras.preprocessing.image import ImageDataGenerator


#image augmentation 

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(size, size),
        batch_size=5,
        class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(size, size),
        batch_size=5,
        class_mode='categorical')


classifier.fit_generator(train_generator,
        steps_per_epoch=4000, epochs=30, validation_steps=20, validation_data = validation_generator)



#save the model

import h5py

classifier.save("CNNmodel2.h5")

from Ipython.display import SVG
from keras.utils.vis_utils import model_to_dot
SVG(model_to_dot(classifier).create(prog="dot", format ="svg"))

#plot graph using model

from keras.utils import plot_model

plot_model(classifier, "graph.png")

#export model to coreml

import coremltools

output_labels = ["Arsenal", "Bournemouth", "Brighton", "Burnley", "Chelsea", "Crystal Palace", "Everton",
                 "Huddersfield", "Leicester", "Liverpool",  "Man City", "Man Utd", 
                 "Newcastle", "Southampton", "Spurs", "Stoke", "Swansea",  
                 "Watford", "West Brom", "West Ham"]

scale = 1/255.

coreml_gen = coremltools.converters.keras.convert("CNNmodel2.h5",
                                                  input_names = 'image',
                                                  image_input_names='image',
                                                  class_labels =output_labels,
                                                  image_scale= scale)
coreml_gen.author = "John Kenny"
coreml_gen.license = 'MIT'
coreml_gen.input_description['image'] = 'Image of a football crest'
coreml_gen.output_description['output1'] = "Predicted team"
coreml_gen.save("crestIdeniferCNN2.mlmodel")











