# Automatic-ML-Profiling-Training-Model

## How to start with the webapp
```
# clone the repo
git clone <repo link>

# move inside the clone folder
cd <folder-name>
```
## Initial setup for virtual env
```
# create the virtual env (prerequisite conda )
conda craete --name ml-webapp python==3.10 -y

# activate the conda environment
conda actiavte ml-webapp
```

## Install the dependencies
```
pip install requirements.txt
```

## Start the localhost server
```
streamlit run app.py
```

## Screens of the webapp
### Here user will upload the dataset in csv (currently only csv)
![upload screen](/docs/images/upload1.png)

### After uploading csvv dataset, it will show the info. To save the data for training click on "save data" button.
![upload screen](/docs/images/upload2.png)

### From the right side select profiling radio button to get the profiling of the dataset .
![profiling1](/docs/images/profiling1.png)
.
.
.
![profiling2](/docs/images/profiling2.png)
.
.
.
![profiling3](/docs/images/profiling3.png)

### Select the column from the dropdown menu and Click on the train button, to train the model.
![train model](/docs/images/MLtrain.png)

### Click on the Download button to Download the train model and you can use that model anywhere just by loading it.
![download model](/docs/images/ModelDownload.png)