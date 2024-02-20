# need to add following steps before running the code:
# cd fsdl-text-recognizer-2021-labs
# pip3 install boltons wandb pytorch_lightning==1.1.4 pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 torchtext==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
# then refer to the following code to run the code.

#%load_ext autoreload
#%autoreload 2

#%matplotlib inline

# before running training add carbon footprint metrics to produce ESG report.

#import site
#print(site.getsitepackages())

import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages')

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# The importlib.util module provides functions to support the import mechanism.
from importlib.util import find_spec # Check if the "text_recognizer" module can be found
if find_spec("text_recognizer") is None:
    # If not, add the parent directory to the system path
    import sys
    sys.path.append('..')

# Now we can import the EMNIST class from the "text_recognizer.data.emnist" module
# Import the EMNIST class from the text_recognizer.data.emnist module
from text_recognizer.data.emnist import EMNIST

# Create an instance of the EMNIST class
data = EMNIST()

# Call the prepare_data method to download the data and prepare it for use
data.prepare_data()

# Call the setup method to create the data loaders
data.setup()

# Print a string representation of the EMNIST instance, which includes information about the dataset
print(data)

# Get the first batch of images (x) and labels (y) from the test data loader
x, y = next(iter(data.test_dataloader()))

# Print the shape, data type, minimum value, mean value, standard deviation, and maximum value of the images
print(x.shape, x.dtype, x.min(), x.mean(), x.std(), x.max())

# Print the shape, data type, minimum value, and maximum value of the labels
print(y.shape, y.dtype, y.min(), y.max())

# Create a new figure with a size of 9x9 inches
fig = plt.figure(figsize=(9, 9))
for i in range(9): # Loop over the range of 9 to create 9 subplots
    # Add a subplot to the figure in a 3x3 grid at position i+1
    ax = fig.add_subplot(3, 3, i + 1)
    # Generate a random index within the range of the test data length
    rand_i = np.random.randint(len(data.data_test))
    # Use the random index to select a random image and its corresponding label from the test data
    image, label = data.data_test[rand_i]
    # Display the image in the subplot, reshaping it to 28x28 and using a grayscale color map
    ax.imshow(image.reshape(28, 28), cmap='gray')
    # Set the title of the subplot to the character that corresponds to the label
    ax.set_title(data.mapping[label])
    
# --> add carbon footprint metrics to produce ESG report

import codecarbon
import pytorch_lightning as pl
from text_recognizer.models import CNN
from text_recognizer.lit_models import BaseLitModel
from codecarbon import OfflineEmissionsTracker

model = CNN(data_config=data.config())

lit_model = BaseLitModel(model=model)

# Initialize the trainer
trainer = pl.Trainer(max_epochs=8)

# Initialize the OfflineEmissionsTracker with the ISO code of Canada
tracker = OfflineEmissionsTracker(country_iso_code="CAN")

# Start tracking CO2 emissions
tracker.start()

trainer.fit(lit_model, datamodule=data)

# Stop tracking CO2 emissions after training is complete
tracker.stop()

# 15.375331498498674 grams of CO2 emitted
    
# Get the first batch of images (x) and labels (y) from the test data loader
x, y = next(iter(data.test_dataloader()))

# Pass the images through the model to get the logits
# The logits are the raw output values from the model, before applying the softmax function
logits = model(x)  # (B, C)
print(logits.shape)  # Print the shape of the logits tensor

# Get the predicted labels by finding the index of the maximum logit for each image
# The argmax function returns the index of the maximum value along a specified axis (here, -1 indicates the last axis)
preds = logits.argmax(-1)

# Print the true labels and the predicted labels
print(y, preds)

# Create a new figure with a size of 9x9 inches
fig = plt.figure(figsize=(9, 9)) # Loop over the range of 9 to create 9 subplots
for i in range(9): # Add a subplot to the figure in a 3x3 grid at position i+1
    ax = fig.add_subplot(3, 3, i + 1)
    # Generate a random index within the range of the test data length
    rand_i = np.random.randint(len(data.data_test))
    # Use the random index to select a random image and its corresponding label from the test data
    image, label = data.data_test[rand_i]

    image_for_model = image.unsqueeze(0)  # (1, 1, 28, 28)
    logits = model(image_for_model)  # (1, C)
    # Get the index of the maximum value in the logits tensor
    # This is the predicted class index, because the class with the highest score (logit) is the model's prediction
    pred_ind = logits.argmax(-1)  # (1, )

    # Convert the predicted class index into the corresponding class label
    # data.mapping is a list or dictionary that maps class indices to class labels
    pred_label = data.mapping[pred_ind]

    # Reshape the image tensor into a 28x28 grid and display it in the subplot `ax` in grayscale
    ax.imshow(image.reshape(28, 28), cmap='gray')

    # Set the title of the subplot to a string that includes the actual label (`data.mapping[label]`) and the predicted label (`pred_label`) of the image
    ax.set_title(f'Correct: {data.mapping[label]}, Pred: {pred_label}')   
    