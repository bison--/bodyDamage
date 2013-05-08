#!/usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui
from bodyDamage import *

# tools:
# qt4-designer
# pyqt4-dev-tools
# pyuic4 -x bodyDamage.ui -o bodyDamage.py

# TODO: auto connect signals!
# http://www.eurion.net/python-snippets/snippet/Connecting%20signals%20and%20slots.html
# QtCore.QMetaObject.connectSlotsByName(MainWindow)



class signalHandler(object):
	def __init__(self, ui):
		self._ui = ui
		self.connect()
		
		self.connectedBodyParts = { 'Lbody':('Rleg','Lleg'), 'Rleg':('Rfeet',), 'Lleg':('Lfeet',), 'Rarm':('Rhand',), 'Larm':('Lhand',) }
		
	def connect(self):
		# conenct here
		print 'connect'
		for itm in dir(self._ui):
			#print itm
			if 'nut' in itm:
				QtCore.QObject.connect(self._ui.__dict__[itm], QtCore.SIGNAL("valueChanged(int)"), self.recalc)
			elif 'chk' in itm:
				QtCore.QObject.connect(self._ui.__dict__[itm], QtCore.SIGNAL("stateChanged(int)"), self.recalc)

	def recalc(self):
		lostSubBodyPart = False
		totalHp = 0
		restHp = 0
		dead = False
		damageResult = []
		additionalMessages = []
		
		for itm in dir(self._ui):
			if itm.startswith('nut'):
				#print dir(self._ui.__dict__[itm])
				#print self._ui.__dict__[itm].value()
				tmpValue = self._ui.__dict__[itm].value()
				
				totalHp += 100
				restHp += tmpValue
				
				if tmpValue < 100 and tmpValue > 0:
					damageResult.append(itm.replace("nut", "") + ": {0:d} %".format(tmpValue) )
				elif tmpValue == 0:
					damageResult.append("You lost: " + itm.replace("nut", ""))
					itmShort = itm.replace('nut', '')
					if itmShort in self.connectedBodyParts:
						for subPart in self.connectedBodyParts[itmShort]:
							if self._ui.__dict__['nut' + subPart].value() > 0:
								self._ui.__dict__['nut' + subPart].setValue(0)
								lostSubBodyPart = True
				
				if itm == 'nutHead' and tmpValue == 0:
					additionalMessages.append("DONT LOSE YOUR HEAD!")
					dead = True
				elif itm == 'nutUbody' and tmpValue == 0:
					additionalMessages.append("seems like your heard stopped beating...")
					dead = True
				
			elif itm.startswith('chk'):
				#print self._ui.__dict__[itm].checkState()
				totalHp += 50
				if self._ui.__dict__[itm].checkState() == 0:
					restHp += 50
				else:
					additionalMessages.append("NO MORE ADVENTURES 4 YOU")

		if lostSubBodyPart:
			self.recalc()
		else:
			self._ui.__dict__['pgbHP'].setMaximum(totalHp)
		
			if dead or restHp <= 0:
				additionalMessages.append("DEAD")
				self._ui.__dict__['pgbHP'].setValue(0)
			else:
				self._ui.__dict__['pgbHP'].setValue(restHp)
				additionalMessages.append("{0}/{1} hp".format(restHp, totalHp))
		
			finalText = ""
			if damageResult:
				finalText += "\n".join(damageResult)
		
			if finalText != "" and additionalMessages:
				finalText += "\n"
			
			if additionalMessages:
				finalText += "\n".join(additionalMessages)

			self._ui.__dict__['txtReport'].setPlainText(finalText)
		
		
	def on_nutRhand_valueChanged(self, val):
		print 'right hand', val
	
	def on_nutRhand_valueChanged(self):
		print 'right hand'
	

app = QtGui.QApplication(sys.argv)
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

sh = signalHandler(ui)

MainWindow.show()
sys.exit(app.exec_())


