# need to add following steps before running the code:
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
    
import codecarbon
import argparse
import pytorch_lightning as pl
from text_recognizer.models import MLP
from text_recognizer.lit_models import BaseLitModel
from text_recognizer.data import MNIST as MNISTDataModule
from codecarbon import OfflineEmissionsTracker

# Create an argparse.Namespace object
args = argparse.Namespace()

# Initialize the data module with the args
data = MNISTDataModule(args)

# Initialize the model with the data config
model = MLP(data_config=data.config())

# Wrap the model with the PyTorch Lightning wrapper
lit_model = BaseLitModel(model=model)

# Initialize the trainer
trainer = pl.Trainer(max_epochs=3)

# Initialize the OfflineEmissionsTracker with the ISO code of Canada
tracker = OfflineEmissionsTracker(country_iso_code="CAN")

# Start tracking CO2 emissions
tracker.start()

# Fit the model
trainer.fit(lit_model, datamodule=data)

# Stop tracking CO2 emissions after training is complete
tracker.stop()

# 0.00015759014725022993 CO2 emissions in kg