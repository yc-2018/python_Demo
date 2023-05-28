# By：仰晨
# 文件名：qt的demo2.0
# 时 间：2023/5/28 23:17

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit
from PyQt5.QtCore import Qt


class FileDropLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        watermark_type = {'白色水印': False, '黑色水印': True}
        logos = {'小米': 'mi.png', '莱卡': 'Leica.png', "苹果": 'Apple.png', "其他": 'yc.png'}

        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if path:
                print(f"File path: {path}")
                # 水印类型（黑。or 白）
                watermark_type_value = self.parent().watermark_type.currentText()
                print(f"黑色水印吗 value: {watermark_type[watermark_type_value]}")
                # logo
                camera_logo_value = self.parent().camera_logo.currentText()
                print(f"logo value: {logos[camera_logo_value]}")
                # 相机名字
                camera_name_value = self.parent().camera_name.text()
                print(f"相机名字 value: {camera_name_value if camera_name_value else None}")
                # 地点
                Place_name_value = self.parent().Place_name.text()
                print(f"地点 value: {Place_name_value if Place_name_value else '蓝蓝的天空下'}")


class SimpleDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('生成小米款大水印')
        self.resize(800, 400)

        main_layout = QVBoxLayout()         # 垂直布局，用于按从上到下的顺序排列控件，形成一列。

        # 创建第一行的下拉框和输入框
        controls_layout = QHBoxLayout()     # 水平布局。它按从左到右的顺序排列控件，形成一行。当您将多个控件添加到 QHBoxLayout 中时，它们会在同一行内并排显示。

        # 相机水印颜色--下拉框
        self.watermark_type = QComboBox(self)
        self.watermark_type.addItems(['白色水印', '黑色水印'])
        controls_layout.addWidget(self.watermark_type)

        # 相机logo--下拉框
        self.camera_logo = QComboBox(self)
        self.camera_logo.addItems(['小米', '莱卡', "苹果", "其他"])
        controls_layout.addWidget(self.camera_logo)

        # 相机名字--输入框
        self.camera_name = QLineEdit(self)  # 设置默认值为空
        self.camera_name.setPlaceholderText('相机名字，一般默认就行，出现不是手机名字的就自行设置')  # 设置占位符文本
        controls_layout.addWidget(self.camera_name)

        main_layout.addLayout(controls_layout)

        # 创建第二行的输入框
        controls_layout2 = QHBoxLayout()
        # 地点名字--输入框
        self.Place_name = QLineEdit(self)  # 设置默认值为空
        self.Place_name.setPlaceholderText('当在照片里面读取不到位置是就会用这个来代替，默认："在宇宙一颗蔚蓝的星球上"')  # 设置占位符文本
        controls_layout2.addWidget(self.Place_name)
        main_layout.addLayout(controls_layout2)

        # 创建一个接收拖动进来的文件的控件
        self.label = FileDropLabel('将文件夹或文件拖放到此处', self)
        self.label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.label)

        self.setLayout(main_layout)     # 设置main_layout 为窗口的主布局，以便将其用于管理窗口中的控件和子布局。


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = SimpleDemo()
    demo.show()

    sys.exit(app.exec_())
