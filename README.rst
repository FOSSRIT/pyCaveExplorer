pyCave Explorer
===============

.. split here

Authors
-------

- Jennifer Dziuba
- TJ Miller
- Ralph Bean (threebean)

created for use on the OLPC

Development instructions for Linux
----------------------------------

threebean found that on Fedora 17, he had to do the following stuff to get
pygame to stand up correctly in a virtualenv::

  $ sudo yum -y install pygame pygame-devel
  $ mkvirtualenv --system-site-packages pyCaveExplorer
  (pyCaveExplorer) $ python setup.py develop

Then I could run the game by typing::

  (pyCaveExplorer) $ explore-the-cave


TO DO :
-------

- learn pygame

- make grid

	- decide resolution
	- tag for current square
	- tag for goal square
	- tags for lit squares
	- tags for unlit squares
	- tags for blocked squares
	- lightbulb object
	- battery object
	- treasure object
	- way to track which squares are electrically connected

- grid generator

	- create genrator that randomly populates grid
	- create solver to check if grid is valid

		- re-create grid if invalid

- create stat tracking interface

	- incorporate with Journal

--------------------

Teach fourth grade electricity and magnetism
http://schools.nyc.gov/Documents/STEM/Science/K8ScienceSS.pdf
