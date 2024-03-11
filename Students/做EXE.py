from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
import sys

# 一、应用程序对象，只能有一个
# 1、该类管理GUI应用程序控制流和主要设置，专门用于QWidget所需的一些功能
# 2、不使用命令行或提示符程序（cmd），则为空列表 []
# 3、如果使用命令行或提示符程序(cmd)，则为sys.argv
app = QApplication(sys.argv)
# 二、从窗口类型中可以创建三种窗口对象
# 1、QWidget
# 2、QMainWindow
# 3、QDialog
window = QWidget()
# 三、QWidget显示窗口
window.show()
# 四、执行程序
sys.exit(app.exec())