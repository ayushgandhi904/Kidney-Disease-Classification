# Kidney-Disease-Classification
Classifies Kidney Tumor based on object Detection 

# Kidney-Disease-Classification-MLflow-DVC


## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline 
7. Update the main.py
8. Update the dvc.yaml
9. Run app.py

# How to run?
### STEPS:

Clone the repository

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -p venv python=3.8 -y
```

```bash
conda activate venv/
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/ayushgandhi904/Kidney-Disease-Classification.mlflow \
MLFLOW_TRACKING_USERNAME=ayushgandhi904 \
MLFLOW_TRACKING_PASSWORD=your_token  \
python script.py


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)



