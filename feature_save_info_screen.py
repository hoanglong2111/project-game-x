import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout

class TextDisplayApp (QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Text Display Application")
        self.setGeometry(100, 100, 400, 200)
        
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.label1 = QLabel("Họ và Tên")
        self.label2 = QLabel("Số điện thoại")
        self.text_edit1 = QLineEdit("")
        self.text_edit2 = QLineEdit("")
        
        self.display_button1 = QPushButton("Lưu thông tin")
        self.display_button2 = QPushButton("Xóa thông tin")
      
        self.result_label = QLabel("")
        
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.text_edit1)
        layout.addWidget(self.label2)
        layout.addWidget(self.text_edit2)
        layout.addWidget(self.display_button1)
        layout.addWidget(self.display_button2)
      
        layout.addWidget(self.result_label)
 
        
        centralWidget.setLayout(layout)

        
        self.display_button1.clicked.connect(self.display_text)
        self.display_button2.clicked.connect(self.display_text)
    def display_text(self):
        entered_text = self.text_edit.text()
        self.result_label.setText(f"Tên của bạn là:{entered_text}")
def main():
    app = QApplication(sys.argv) 
    window = TextDisplayApp()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
    
