# db1.py
import sqlite3

# 일단 메모리에서 임시 저장
# con = sqlite3.connect(":memory:")
# 파일로 저장(커밋까지 완료)
con = sqlite3.connect("c:\\work\\sample.db")

# 커서 객체
cur = con.cursor()

# 테이블(자료구조) 생성
cur.execute("create table if not exists PhoneBook(Name text, PhoneNum text);")

# 1건 입력
cur.execute("insert into PhoneBook values('홍길동', '010-222');")

# 외부에서 입력 파라메터 처리
name = "전우치"
phoneNum = "010-333"
cur.execute("insert into PhoneBook values(?, ?);",(name, phoneNum))

# 다중행 입력
datalist = (("김길동","010-123"),("박문수","010-567"))
cur.executemany("insert into PhoneBook values(?, ?);",datalist)


print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

# 작업 정상 완료
con.commit()
