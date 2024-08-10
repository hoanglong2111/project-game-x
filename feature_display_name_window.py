import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class TextDisplayApp (QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Text Display Application")
        self.setGeometry(100, 100, 400, 200)
        
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        
        self.text_edit = QLineEdit("")
        self.display_button = QPushButton("Hiển thị")
        self.result_label = QLabel("aa")
        
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.display_button)
        layout.addWidget(self.result_label)
        
        centralWidget.setLayout(layout)
        
        self.display_button.clicked.connect(self.display_text)
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
    
