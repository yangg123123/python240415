# DemoForm2.py
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# 웹서버에 요청
import requests
import os
# 크롤링
from bs4 import BeautifulSoup
import web2_yang
import yang_db1


# 디자인한 파일 로딩
getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
os.path.join(base_path, relative_path)
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
        result = yang_db1.dbRead()
        self.label.setText(str(result))
        # self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        result = yang_db1.dbRead()
        f = open("db_write_test.txt", "wt", encoding="utf-8")
        f.write(str(result))
        f.close()
        self.label.setText("파일 생성 완료")
        

# 직접 모듈을 실행했는지 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()