# x-ray image classification

Dataset is downloaded from: https://nihcc.app.box.com/v/ChestXray-NIHCC

This project is for the prediction of chest infection by visualisation of the chest x-ray images on the basis of 15 different classifications which are given by the NIH Clinical Center.

It uses keras for the CNN and as a backend tensorflow for creating the x-ray prediction model. 
Django is used for creating the web interface of this predicting model and deployment on the web.

Output comes by the processing of image with the ".h5" file of the model in 15 different classifications if infection is present in image.

Steps for running this project:
1. clone the repository by command <git clone https://github.com/redcrix/x-ray.git>
2. use command < cd x-ray >
3. run install.py by command < python install.py > it will install all the libraries which are required to run this project.
4. After the whole libraries install now its time to start the webapp.
5. Use command < python manage.py runserver > for starting the webapp.
6. It will open with register page and registration is required to use this webapp.
7. After that login with the credentials which you entered at the time of registration.
8. Upload image and after uploading image it will show the results.

Note:
If their is an problem in running the install.py file then use the manual commands which are writen below.

pip install tensorflow

pip install keras

pip install django

pip install h5py

pip install numpy


It is not necessary to create virtual environment for running this webapp.



>>>>>>>>>>for mac and linux use python3 and pip3 in place of python and pip.
