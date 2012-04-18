pyCave Explorer
===============

.. split here

Authors
-------

- Jennifer Dziuba
- TJ Miller
- Ralph Bean (threebean)
- David Gay (oddshocks)

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
	- mirrors ?

- grid generator

	- create genrator that randomly populates grid
	- create solver to check if grid is valid

		- re-create grid if invalid

- create stat tracking interface

	- incorporate with Journal

--------------------

Teach fourth grade electricity and magnetism
http://schools.nyc.gov/Documents/STEM/Science/K8ScienceSS.pdf

--------------------

Some concepts:

- battery is placeable, but then anchored in place
- player gets certain number of lights per level
- infinite lengths of wire
- lights are placeable, but then anchored in place
- there are mirrors in the grid that will direct light in certain directions

Lighting Strategies:

- the player can quickly light an area in series, using one wire.

	- provides average lighting
	- requires less "commands"
	- can short out the battery

- the player can take more time to light the area in parallel.

	- provides better lighting
	- requires more "commands"
	- will not short out the battery
