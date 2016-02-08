#Makefile lorenmanu segundo hito
#clean install test run doc

clean:
	- rm -rf *~*
	- find . -name '*.pyc' -exec rm {} \;
	- find . -name '.DS_Store' -exec rm {} \;

install:
	sudo python setup.py install

database:
	sudo python manage.py syncdb

test:
	sudo python manage.py test

run:
	sudo python manage.py runserver

doc:
	epydoc --html MiTienda/*.py
