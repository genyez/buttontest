# -*- coding:utf-8 -*-
# @ModuleName: main
# @Description: 
# @Author: laoweimin@corp.netease.com
# @Time: 2022/3/11 10:23
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.Qt import QApplication, QPixmap, QImage, QSize, QTimer


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
		self.button.move(x, y)
		self.key = key

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

class TestJob(object):
	def __init__(self):
		super(TestJob, self).__init__()
		self.testpoints = []
		self.timer = QTimer()
		self.timer.setInterval(1000)
		self.timer.timeout.connect(self.onTimeout)
		self.currenttime = 0

	def initUI(self):
		self.window = QWidget()
		self.window.setWindowTitle("测试工具")
		self.label = QLabel()

		layout = QVBoxLayout()
		self.window.setLayout(layout)
		layout.addWidget(self.label)
		image = QImage()
		image.load("map.jpg")
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

		self.window.show()

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