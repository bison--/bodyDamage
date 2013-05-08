# bodyDamage #


fell down the stairs, wrote a program to calculate the damage I took ^^

## Story ##

I fell down the stairs and would tweet about it, with a damage report.  
Then I remembered my bad math skills and I am too lazy to calculate em.  
So I wrote a program for me to do it ^^

## Installation ##

you need PyQt4

### Linux ###
just run the start.py

### Windows ###
on 64bit download  
  + [python-2.7.4.amd64.msi] [1]
  + [PyQt4-4.10.1-gpl-Py2.7-Qt4.8.4-x64.exe] [2]

on 32bit download  
  + [python-2.7.4.msi] [3]
  + [PyQt4-4.10.1-gpl-Py2.7-Qt4.8.4-x32.exe] [4]

install both with the DEFAULT settings and everything would be fine ;)

### Dev ###
under Linux you you have to install:  

    sudo apt-get install qt4-designer pyqt4-dev-tools

now you can edit the **bodyDamage.ui** with the qt4-designer and convert it to Python code with:  

    pyuic4 -x bodyDamage.ui -o bodyDamage.py


  [1]: http://www.python.org/ftp/python/2.7.4/python-2.7.4.amd64.msi        "64bit"
  [2]: http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.10.1/PyQt4-4.10.1-gpl-Py2.7-Qt4.8.4-x64.exe    "64bit"

  [3]: http://www.python.org/ftp/python/2.7.4/python-2.7.4.msi        "32bit"
  [4]: http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.10.1/PyQt4-4.10.1-gpl-Py2.7-Qt4.8.4-x32.exe        "32bit"
