# Description: This file contains the code to run the Great Expectations tutorial.
# https://github.com/datarootsio/tutorial-great-expectations

# Create the necessary Great Expectations environment.
# cd /path/to/your/project
# python-3.7.16 
# envname (Python 3.7.16)  *  /Users/devopsmarc/anaconda3/envname/bin/python

# To activate the interactive python jupyter notebook environment, use
# conda activate "envname"
# pip install ipykernel

# Install the necessary packages to run the code.
# pip3 install -r requirements.txt
# pip3 install great_expectations==0.13.5
# pip3 install tree

# mkdir -p great_expectations/checkpoints

# here too pythonpath to be set export PYTHONPATH=.:$PYTHONPATH
# check with: echo $PYTHONPATH

# then refer to the following code to run the code.

#%load_ext autoreload
#%autoreload 2

#%matplotlib inline

# before running training add carbon footprint metrics to produce ESG report.

# import site
# print(site.getsitepackages())

# Import the sys module, which provides access to some variables used or maintained by the Python interpreter
# import sys
# sys.path.append('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages')

import great_expectations as ge
print(ge.__version__)
#print(type(context))

context = ge.data_context.DataContext()

suite = context.create_expectation_suite(
    'check_avocado_data',
    overwrite_existing=True
)

batch_kwargs = {
    'path': 'data/avocado.csv',
    'datasource': 'data_dir',
    'data_asset_name': 'avocado',
    'reader_method': 'read_csv',
    'reader_options': {
        'index_col': 0,
    }
}
batch = context.get_batch(batch_kwargs, suite)

batch.head()

# table level expectations or check
batch.expect_column_to_exist('Date')

# column level value expectations or check
batch.expect_column_values_to_not_be_null('region')

batch.expect_column_values_to_match_strftime_format('Date', "%Y-%m-%d")

batch.expect_column_values_to_be_between('AveragePrice', min_value=0.5, max_value=3.0)
# it will collect up to 20 examples of values that didn't meet the expectation 
# (this is called the _partial_ unexpected list)

batch.expect_column_values_to_be_between('AveragePrice', min_value=0.5, max_value=3.0, mostly=0.99)

batch.expect_column_distinct_values_to_be_in_set('type', ['conventional', 'organic'])

partition_object = {
    'values': ['conventional', 'organic'],
    'weights': [0.5, 0.5],
    
}
batch.expect_column_kl_divergence_to_be_less_than('type', partition_object, 0.1)

# great_expectations remembered all the expectations ran. 
# We can now retrieve the suite contents as follows:
batch.get_expectation_suite()

# saved the expectations to the suite including failed expectations
batch.save_expectation_suite(discard_failed_expectations=False)

import subprocess

command = "tree great_expectations -nI 'uncommitted'"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
output, error = process.communicate()

print(output.decode())

# the expectations are saved in a expectation store, which by default is a directory called expectations in the great_expectations directory.
# it is possible to save the expectations in a different location such as a database, cloud storage, etc.

with open('great_expectations/expectations/check_avocado_data.json', 'r') as file:
    data = file.read()

print(data)

# cat great_expectations/expectations/check_avocado_data.json is an alternative to the above code.


# Using Validation Operators to create a validation result.
# Validation results are kept in the validation store in the great_expectations/uncommitted directory - by default.
results = context.run_validation_operator('my_validation_operator', assets_to_validate=[batch])

import subprocess

command = "tree -n great_expectations/uncommitted/validations"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
output, error = process.communicate()

print(output.decode())

# This is Data Docs (testing & documentation at same time )
# see the validation results html "online" in the browser

context.open_data_docs()

# this is the Data Context, which is the central object in Great Expectations.
import subprocess

command = "tree great_expectations -nI 'uncommitted'"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
output, error = process.communicate()

print(output.decode())

with open('great_expectations/great_expectations.yml', 'r') as file:
    data = file.read()

print(data)

# cat great_expectations/great_expectations.yml is an alternative to the above code.

#  Checkpoints are used to easily rerun a validation, for example each time our data changes. 
#  Such a rerunable configuration file is called a `Checkpoint` in Great Expectations.
# As a quick reminder, for running a validation we need:
# - A *validation operator* to handle the validation results
# - A list of *batches*, each consisting of
#     - A batch of data to check
#     - expectation suites to check against

# In this case the configuration file was put together manually
# It is called `great_expectations/checkpoints/check_avocado_data.yml` and looks like this:

# Important check identation in the yaml file - especially if it fails to run the checkpoint.

data = """
validation_operator_name: my_validation_operator
batches:
  - batch_kwargs:
      path: data/avocado.csv
      datasource: data_dir
      data_asset_name: avocado
      reader_method: read_csv
      reader_options:
        index_col: 0
    expectation_suite_names:
      - check_avocado_data
"""

with open('great_expectations/checkpoints/avocado_data.yml', 'w') as file:
        file.write(data.strip())


# Running the checkpoint saved previously.
# The checkpoint is saved in the great_expectations/checkpoints directory.
# The checkpoint is run with the following command:

import subprocess

command = "great_expectations checkpoint run avocado_data"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
output, error = process.communicate()

print(output.decode())

# This run is an important step in the process of setting up Great Expectations for a project.
# Since, to summarize: a checkpoint is a _runnable check_ for your data. 
# It is the first stop for integrating Great Expectations into pipelines and workflows.

import subprocess

command = "great_expectations datasource profile data_dir -y"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
output, error = process.communicate()

print(output.decode())

############################################################################################################
# Initializing a new Great Expectations project
############################################################################################################

## Setting up your own project

# To initialize a project, run `great_expectations init` and follow the instructions. 
# This will scaffold a simple configuration for you, just like the one provided above.

# Once created a suite using `great_expectations suite new`, you can use the `great_expectations suite edit` command.
# This will open up an auto-generated notebook that you can use to set up your suite. 
# You should be able to recognise the structure of the first part of this notebook a bit ;-)