Instructions :- 

Phase 1:-(installation)(For better understanding refer to http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

1. Choose a location where you want your application to live and create a new folder there to contain it.

2.  Now from terminal cd in this folder.

3.	Install pip :- sudo easy_install pip (on mac).

4.	Install virtual environment :- pip install virtualenv.	

5.  For older versions of Python that have been expanded with virtualenv, the command that creates a virtual environment is:
	virtualenv flask (i have done this)

6. Now install :
	flask/bin/pip install flask
	flask/bin/pip install flask-login
	flask/bin/pip install flask-openid
	flask/bin/pip install flask-mail
	flask/bin/pip install flask-sqlalchemy
	flask/bin/pip install sqlalchemy-migrate
	flask/bin/pip install flask-whooshalchemy
	flask/bin/pip install flask-wtf
	flask/bin/pip install flask-babel
	flask/bin/pip install guess_language
	flask/bin/pip install flipflop
	flask/bin/pip install coverage

	You now have a flask sub-folder inside your Project Folder.

7.  Now in this folder you create all sub folders
	mkdir app
	mkdir app/static
	mkdir app/templates
	mkdir tmp


8. run ./db_create.py ( if permission not set , set it by using chmod)
9. run ./db_migrate.py ( if permission not set , set it by using chmod)

Phase 2 (Running) :- 
	1. Run this project by typing : ./run.py ( if permission not set , set it by using chmod)
	2. For searching in app just type the url as : http://localhost:5000/ ( and give appropriate location and speciality) 
	2. For getting in admin page u need to type : http://localhost:5000/adminIndex 
	3. Now if u want to insert some doctor data then place the copy of image in static folder in app and in insert page just type the
	   name of the image.