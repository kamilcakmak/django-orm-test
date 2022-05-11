#Installation

#Prerequisites

#1 Install Python
Install python-3.7.2 and python-pip. Follow the steps from the below reference document based on your Operating System. Reference: https://docs.python-guide.org/starting/installation/

#2 Setup virtual environment
Install virtual environment
sudo pip install virtualenv

Make a directory
mkdir envs

Create virtual environment
virtualenv ./envs/

Activate virtual environment
source envs/bin/activate

for windows;
Install virtual environment
pip3 install virtualenvwrapper-win

Make a directory
mkdir envs

Create virtual environment
mkvirtualenv myvenv

Activate virtual environment
workon myvenv


#3 Clone git repository
git clone "https://github.com/kamilcakmak/django-orm-test.git"

#4 Install requirements
cd simple-django-project/
pip install -r requirements.txt

#5 Run the Server
python manage.py runserver

Try opening http://127.0.0.1:8000 in the browser.

#6 URLs
 Question 1
http://127.0.0.1:8000/q1/

![q1](https://user-images.githubusercontent.com/71510521/167818334-8e43707a-42bf-44ee-ab30-e6307a488602.PNG)

 Question 2
http://127.0.0.1:8000/q1/

![q2](https://user-images.githubusercontent.com/71510521/167818569-840ffb94-dfc9-4ba5-b66c-71d6ed03c6c6.PNG)

entity-relationship diagram
![operation1](https://user-images.githubusercontent.com/71510521/167818662-c6e7322e-a409-4cd0-a42a-757596c6139a.png)

 admin page
http://127.0.0.1:8000/admin/

user:evrk
password : 123





