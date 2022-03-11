# -*- coding:utf-8 -*-
# @ModuleName: main
# @Description: 
# @Author: laoweimin@corp.netease.com
# @Time: 2022/3/11 10:23
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.Qt import QApplication, QPixmap, QImage, QSize, QTimer, pyqtSignal


class TestPoint(object):
	SIZE = QSize(150, 70)
	NAME = "测试"
	def __init__(self, x, y, key, parent):
		super(TestPoint, self).__init__()
		self.parent = parent
		self.button = QPushButton(self.NAME)
		self.button.setParent(parent.window)
		self.button.clicked.connect(self.onClick)
		self.button.resize(self.SIZE)
		self.x, self.y = x, y
		self.button.move(x, y)
		self.key = key

	def resize(self, xratio, yratio):
		self.button.move(self.x * xratio, self.y * yratio)
		self.button.resize(self.SIZE.width()* xratio, self.SIZE.height()* yratio)

	def onClick(self):
		self.parent.currenttime = 60
		self.parent.timer.start()
		print(self.key)


testpoints = [
	{
		"x":100,
		"y":100,
		"key":"abcde"
	},
	{
		"x":200,
		"y":200,
		"key":"dggytyt"
	}
]

class MyWindow(QWidget):
	onresize = pyqtSignal()
	def __init__(self):
		super(MyWindow, self).__init__()

	def resizeEvent(self, event):

		ret = super(MyWindow, self).resizeEvent(event)
		self.onresize.emit()
		return ret


class TestJob(object):
	def __init__(self):
		super(TestJob, self).__init__()
		self.testpoints = []
		self.timer = QTimer()
		self.timer.setInterval(1000)
		self.timer.timeout.connect(self.onTimeout)
		self.currenttime = 0

	def initUI(self):
		self.window = MyWindow()
		self.window.setWindowTitle("测试工具")
		self.label = QLabel()

		layout = QVBoxLayout()
		self.window.setLayout(layout)
		layout.addWidget(self.label)
		image = QImage()
		image.load("map.jpg")
		imgsize = image.size()
		self.imgw, self.imgh = imgsize.width(), imgsize.height()
		self.label.setScaledContents(True)
		self.label.setPixmap(QPixmap.fromImage(image))

		hlayout = QHBoxLayout()

		self.resttime = QLabel()
		self.stop = QPushButton("停止")
		self.stop.clicked.connect(self.onStop)

		hlayout.addWidget(QLabel("剩余:"))
		hlayout.addWidget(self.resttime)
		hlayout.addWidget(self.stop)
		layout.addLayout(hlayout)
		self.initTestPoints()
		self.window.onresize.connect(self.onResize)
		self.window.show()

	def onResize(self):
		nowsize = self.label.size()
		noww, nowh = nowsize.width(), nowsize.height()
		xratio = noww / self.imgw
		yratio = nowh / self.imgh
		for tp in self.testpoints:
			tp.resize(xratio, yratio)

	def onTimeout(self):
		if self.currenttime > 0:
			self.currenttime -= 1
			self.resttime.setText(str(self.currenttime))
		else:
			self.timer.stop()

	def onStop(self):
		self.timer.stop()
		self.currenttime = 0
		self.resttime.setText(str(self.currenttime))
		print("stop")

	def initTestPoints(self):
		for p in testpoints:
			self.testpoints.append(TestPoint(p["x"],p["y"],p["key"], self))


def main():
	app = QApplication([])
	tj = TestJob()
	tj.initUI()
	# tj.initTestPoints()
	app.exec_()

if __name__ == '__main__':
	main()