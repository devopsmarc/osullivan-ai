# Ecosystem overview

## [[[ Lifecyles ]]] - Blue Box
- How to think about all of the activities in the ecosystem

## [[ <u>Per-project ecosystem</u> ]] - stack

### [ Planning & project setup ] - color box

- Decide to work on an AI Assistant
- Determine ecosystem requirements & goals
- Allocate resources
- Consider the ethical implications
- Etc.

### [ Data collection & labeling ] - color box  
- Collect training data
- Set up data collection equipment (e.g., cameras, microphone)
- Annotate with ground truth (how?)

        » stop and go back to step #1 - this is not a linear flow

    - Too hard to get data, refine the problem to make collecting data easier.
    - Easier to label a different task (e.g., hard to annotate, easier to annotate per-pixel segmentation)

### [ Training & debugging ] - color box (most peopele think this is AI)

- Implement a baseline experiment in OpenCV without AI
- Find state of the art model & reproduce
- Debug our implementation (most time will be spent here)
- Improve model architecture for your task

        » stop and go back to step #2 - this is not a linear flow

    - Collect more data (especially if model is overfitting)
    - Realize data labeling is unreliable

            » stop and go back to step #1 - this is not a linear flow

        - Realize task is too hard
        - Requirements trade off with each other, revisit which are most important (voice over in French or subtitles)

###  [ Deploying & testing ] - color box (once you think the model is good enough)

 - Pilot to share with team members
 - Write tests to prevent failed predictions and evaluate for biases
 - Roll out in production 

        » stop and go back to step #3 - this is not a linear flow

    - Doesn't work in the pilot, even though it worked in the evaluation set. 
    - keep improving accuracy of model

            » stop and go back to step #2 - this is not a linear flow

        - Fix data mismatch between training data and data seen in deployment
        - Collect more data
        - Mine hard cases

                » stop and go back to step #2 - this is not a linear flow

            - The metric chosen doesn't actually drive downstream user behavior. 
            - Revisit the metric.
            - Performance in the real world isn't great 
            - Revisit requirements (e.g., do we need to speak faster or more accurate?

## <u>Cross-project Ecosystem</u> - stack

### [ Team & Hiring ] - color box <<<>>>> [ Planning & project setup  ] - color box

- building, hiring and managing team members

### [ Infrasctructure & Tooling ] - color box <<<>>>> [ Data collection & labeling  ] - color box

### [ Infrasctructure & Tooling ] - color box <<<>>>> [ Training & debugging ] - color box

### [ Infrasctructure & Tooling ] - color box <<<>>>> [ Deploying & testing ] - color box

- setting up the infrastructure and tooling
- needs to be able to scale
- handle repetitive experiments

