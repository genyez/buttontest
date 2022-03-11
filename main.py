# -*- coding:utf-8 -*-
# @ModuleName: main
# @Description: 
# @Author: laoweimin@corp.netease.com
# @Time: 2022/3/11 10:23
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.Qt import QApplication, QPixmap, QImage, QSize


class TestPoint(object):
	SIZE = QSize(150, 70)
	NAME = "测试"
	def __init__(self, x, y, key, parent):
		super(TestPoint, self).__init__()
		self.button = QPushButton(self.NAME)
		self.button.setParent(parent)
		self.button.clicked.connect(self.onClick)
		self.button.resize(self.SIZE)
		self.button.move(x, y)
		self.key = key

	def onClick(self):
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

		self.initTestPoints()

		self.window.show()

	def initTestPoints(self):
		for p in testpoints:
			self.testpoints.append(TestPoint(p["x"],p["y"],p["key"], self.window))


def main():
	app = QApplication([])
	tj = TestJob()
	tj.initUI()
	# tj.initTestPoints()
	app.exec_()

if __name__ == '__main__':
	main()