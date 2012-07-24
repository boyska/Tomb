For testers
===========

If you are an impatient, and do not want to install everything the tidy way, this is for you.
From the "tombqt" directory (the same that contains this file), run:

TOMBDIR=../../ TOMBLIBDIR=../../pytomb python2 create.py

to create a tomb, or

TOMBDIR=../../ TOMBLIBDIR=../../pytomb python2 open.py

to open one.

For packagers/tidy people
==========================

You first must install tomb using the usual configure && make && sudo make install
Then you have to install pytomb using python setup.py install
Then you have to install tombqt using python setup.py install

