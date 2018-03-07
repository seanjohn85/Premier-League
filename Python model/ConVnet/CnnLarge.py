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


class Cnn(object):
    def __init__(self):
        self.batch = 5
        self.size = 250 
    
    def model(self):
        #initialise the cnn
        self.classifier = Sequential()
        
        #Convolution layer
        
        #32 feature dectors with dimentions 3*3
        self.classifier.add(Conv2D(32, (3, 3), input_shape=(self.size, self.size, 3)))   
        self.classifier.add(Activation('relu'))   
        
        #pooling layer
        
        #used to reduce the size of the feature map- reducing num of nodes and complexity 
        self.classifier.add(MaxPooling2D(pool_size=(2, 2)))
        
        #add an extra con layer
        
        self.classifier.add(Conv2D(32, (3, 3)))   
        self.classifier.add(Activation('relu')) 
        self.classifier.add(Dropout(0.25))
        self.classifier.add(MaxPooling2D(pool_size=(2, 2)))
        
        #add an extra con layer
        
        self.classifier.add(Conv2D(64, (3, 3)))   
        self.classifier.add(Activation('relu')) 
        classifier.add(Dropout(0.2))
        self.classifier.add(MaxPooling2D(pool_size=(2, 2)))
        
        #add an extra con layer
        
        self.classifier.add(Conv2D(64, (3, 3)))   
        self.classifier.add(Activation('relu')) 
        self.classifier.add(Dropout(0.25))
        self.classifier.add(MaxPooling2D(pool_size=(2, 2)))
        
        #add an extra con layer
        
        self.classifier.add(Conv2D(128, (3, 3)))   
        self.classifier.add(Activation('relu')) 
        self.classifier.add(Dropout(0.2))
        self.classifier.add(MaxPooling2D(pool_size=(2, 2)))
        
        #flatten layer
        
        #puts all the feature maps in one single vector
        self.classifier.add(Flatten())
        
        
        # full connection of layers
        
        #128 nodes
        self.classifier.add(Dense(units = 5000, activation = "relu"))
        self.classifier.add(Dropout(0.2))
         #only 2 (sigmoid) other wise sofmax is needed 
        self.classifier.add(Dense(units = 20, activation = "softmax"))
    
    def train(self):
        #set optimiser
        import keras
        optimizer = keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-8)
        #compiling the CNN
        
        #without binary outcome crossentropy is needed
        self.classifier.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
        
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
                target_size=(self.size, self.size),
                batch_size=self.batch,
                class_mode='categorical')
        
        validation_generator = test_datagen.flow_from_directory(
                'dataset/test_set',
                target_size=(self.size, self.size),
                batch_size=self.batch,
                class_mode='categorical')
        
        
        history = self.classifier.fit_generator(train_generator,
                steps_per_epoch=3845, epochs=100, validation_steps=3845/100, validation_data = validation_generator)
        self.graphs(history)
        

                
    

    def graphs(self, his):
        import matplotlib.pyplot as plt
    
        plt.plot(his.history['acc'])  
    
        plt.plot(his.history['val_acc']) 
        plt.title('trn. accuracy')  
        plt.ylabel('accuracy')  
        plt.xlabel('epoch')  
        plt.legend(['acc',  'val_acc',], loc='lower right')  
        
        plt.show()
        plt.savefig('acc.png')
        
        
        plt.plot(his.history['loss'])  
        
        plt.plot(his.history['val_loss']) 
        plt.title('trn. loss')  
        plt.ylabel('loss')  
        plt.xlabel('epoch')  
        plt.legend(['loss',  'val_loss',], loc='lower right')  
        
        plt.show()
        plt.savefig('loss.png')
        
    #save the model
    def savefiles(self, h5name, coremlname):
        #keras file format
        import h5py
        classifier.save(h5name + ".h5")
        
        #export model to coreml
        
        import coremltools
        
        output_labels = ["Arsenal", "Bournemouth", "Brighton", "Burnley", "Chelsea", "Crystal Palace", "Everton",
                         "Huddersfield", "Leicester", "Liverpool",  "Man City", "Man Utd", 
                         "Newcastle", "Southampton", "Spurs", "Stoke", "Swansea",  
                         "Watford", "West Brom", "West Ham"]
        
        scale = 1/255.
        
        coreml_gen = coremltools.converters.keras.convert(h5name+".h5",
                                                          input_names = 'image',
                                                          image_input_names='image',
                                                          class_labels =output_labels,
                                                          image_scale= scale)
        coreml_gen.author = "John Kenny"
        coreml_gen.license = 'MIT'
        coreml_gen.input_description['image'] = 'Image of a football crest'
        coreml_gen.output_description['output1'] = "Predicted team"
        coreml_gen.save(coremlname + ".mlmodel")
                
   

#run the cnn     

cnn = Cnn()
cnn.model()
cnn.train()
cnn.savefiles("test", "test")















