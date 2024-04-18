# DemoForm2.py
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# 웹서버에 요청
import requests
# 크롤링
from bs4 import BeautifulSoup
import web2_yang

# 디자인한 파일 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 윈도우 클래서 정의
class DemoForm(QMainWindow, form_class):
    # 초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def firstClick(self):
        web2_yang.test()
        self.label.setText("당근마켓 크롤링 완료")

    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭")
        

# 직접 모듈을 실행했는지 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()