# cd fsdl-text-recognizer-2021-labs

# pip3 install boltons wandb pytorch_lightning==1.1.4 pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 torchtext==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
# pip3 install codecarbon  

# here too pythonpath to be set export PYTHONPATH=.:$PYTHONPATH
# check with: echo $PYTHONPATH

# then refer to the following code to run the code.

#%load_ext autoreload
#%autoreload 2

#%matplotlib inline

# before running training add carbon footprint metrics to produce ESG report.

#import site
#print(site.getsitepackages())

# Import the sys module, which provides access to some variables used or maintained by the Python interpreter
import sys
# Append a new directory to the system path where Python looks for modules
# In this case, the directory is where Python 3.11 site-packages are located
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages')

# %matplotlib inline

# Import the pyplot module from matplotlib library. 
# Matplotlib is a plotting library for Python and pyplot provides a MATLAB-like interface for making plots and charts.
import matplotlib.pyplot as plt

# Import the Natural Language Toolkit (nltk). 
# NLTK is a library in Python that provides tools for working with human language data (text). 
# It provides easy-to-use interfaces to over 50 corpora and lexical resources.
import nltk
# https://www.nltk.org and https://wordnet.princeton.edu

# Import the numpy library, which provides support for large, multi-dimensional arrays and matrices, 
# along with a large collection of high-level mathematical functions to operate on these arrays.
import numpy as np

#%load_ext autoreload
#%autoreload 2

# The importlib.util.find_spec function is used to check if the 'text_recognizer' module can be found
from importlib.util import find_spec
# If the 'text_recognizer' module cannot be found, the current directory is added to the system path
if find_spec("text_recognizer") is None:
    import sys
    sys.path.append('..')

# Import the necessary classes and functions from the 'text_recognizer.data.emnist_lines' module
from text_recognizer.data.emnist_lines import EMNISTLines, construct_image_from_string, get_samples_by_char
# Import the SentenceGenerator class from the 'text_recognizer.data.sentence_generator' module
from text_recognizer.data.sentence_generator import SentenceGenerator

# Create an instance of the SentenceGenerator class
sentence_generator = SentenceGenerator()
# Generate and print four sentences with a maximum length of 16 characters
for _ in range(4):
    print(sentence_generator.generate(max_length=16))

# Import the argparse module, which is used for parsing command-line options
import argparse
# Create a Namespace object with two attributes: max_length and max_overlap
args = argparse.Namespace(max_length=16, max_overlap=0)
# Create an instance of the EMNISTLines class with the specified arguments
dataset = EMNISTLines(args)
# Prepare the data for the dataset
dataset.prepare_data()
# Set up the dataset
dataset.setup()
# Print a string representation of the dataset
print(dataset)
# Print the mapping of class indices to characters for the dataset
print('Mapping:', dataset.mapping)

# --> Example of 14,000 synthetic data generation of sentences created for model training
# EMNIST Lines Dataset
# Min overlap: 0
# Max overlap: 0
# Num classes: 83
# Dims: (1, 28, 448)
# Output dims: (16, 1)
# Train/val/test sizes: 10000, 2000, 2000
# Batch x stats: (torch.Size([128, 1, 28, 448])
# Batch y stats: (torch.Size([128, 16])

# Define a function to convert label indices to a string of characters
def convert_y_label_to_string(y, dataset=dataset):
    return ''.join([dataset.mapping[i] for i in y])  # Join the characters together to form a string

# Get the label of the first sample in the training set
y_example = dataset.data_train[0][1]
print(y_example, y_example.shape)  # Print the label and its shape
convert_y_label_to_string(y_example)  # Convert the label to a string and print it

# Set the number of samples to plot
num_samples_to_plot = 9

# Loop over the first num_samples_to_plot samples in the training set
for i in range(num_samples_to_plot):
    plt.figure(figsize=(20, 20))  # Create a new figure for each sample
    x, y = dataset.data_train[i]  # Get the input data and label of the i-th sample
    sentence = convert_y_label_to_string(y)  # Convert the label to a string
    print(sentence)  # Print the string
    plt.title(sentence)  # Set the title of the figure to the string
    plt.imshow(x.squeeze(), cmap='gray')  # Display the input data (an image) in the figure