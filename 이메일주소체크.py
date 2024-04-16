import re

def check_email(email):
    # 이메일 주소를 확인하기 위한 정규식 패턴
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # 입력된 이메일 주소가 정규식 패턴과 일치하는지 확인
    if re.match(pattern, email):
        print(f"{email}: 유효한 이메일 주소입니다.")
    else:
        print(f"{email}: 유효하지 않은 이메일 주소입니다.")

# 이메일 주소 샘플 리스트
sample_emails = [
    "example@example.com",
    "test.email@example.com",
    "user.name@example.com",
    "username123@example.com",
    "user.name123@example.co.uk",
    "user123@example.co.jp",
    "user_name@example-domain.com",
    "user123@subdomain.example.com",
    "user+tag@example.com",
    "user.name@123.com"
]

# 각 샘플 이메일 주소에 대해 체크 함수 호출
for email in sample_emails:
    check_email(email)
