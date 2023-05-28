# By：仰晨
# 文件名：qt的demo
# 时 间：2023/5/28 21:58

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt


class FileDropLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if path:
                print(f"File path: {path}")


class SimpleDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('生成小米款大水印')
        self.resize(800, 400)  # 设置窗口大小

        # 创建一个 QVBoxLayout
        layout = QVBoxLayout()

        # 创建一个接收拖动进来的文件的控件
        self.label = FileDropLabel('将文件夹或文件拖放到此处', self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = SimpleDemo()
    demo.show()

    sys.exit(app.exec_())
