# Helmet-Detection
Sudisa Project for detecting the workers not wearing the helmet.

The File Structure is as such:
  First the Data File contains 3 sub-folders namely: train, test and valid.
  All the above mentioned folders contain 2 sub-folder each namely images and labels.
  The dataset contains a total of 791 images from a CCTV feed. 
  The model was trained upon 400 images, validated on 195 images and also tested on 196 images.
  The Google Collaboratory file named "Object Detection.ipynb" is the file used to train the model.
  The content file contains all the runs data including the validation result, weights etc.
  Next for inferencing we have taken the weights into "models" folder.
  The video used for inferncing is placed inside Videos folder.
  predict.py was initially used for inferencing. Issues currently related to this file are:
    Manually shifting to next frame.
    Procesing time is huges for skiping to the next frame
    Currently not detecting all the people wearing helmets and detecting none without helmet.
  demo.py file solves the issue of manually skipping the frame and also more efficiently processing the video.
