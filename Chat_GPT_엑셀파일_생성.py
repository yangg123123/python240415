import random
from openpyxl import Workbook

# 엑셀 파일 경로
file_path = r'c:\work\products.xlsx'

# 제품 정보 생성 함수
def generate_product_data():
    product_id = random.randint(1000, 9999)
    product_name = f'제품_{product_id}'
    quantity = random.randint(1, 100)
    price = round(random.uniform(10.0, 100.0), 2)
    return product_id, product_name, quantity, price

# 엑셀 파일 생성
workbook = Workbook()
sheet = workbook.active

# 헤더 추가
sheet.append(['제품ID', '제품명', '수량', '가격'])

# 데이터 생성 및 입력
for _ in range(100):
    product_data = generate_product_data()
    sheet.append(product_data)

# 엑셀 파일 저장
workbook.save(filename=file_path)
