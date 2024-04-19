# db1.py
import sqlite3

def dbRead():
    # 읽기
    f = open("yang_select_sql.sql", "rt", encoding="utf-8")
    query = f.read()
    f.close()

    # 일단 메모리에서 임시 저장
    # con = sqlite3.connect(":memory:")
    # 파일로 저장(커밋까지 완료)
    con = sqlite3.connect("c:\\work\\sample.db")

    # 커서 객체
    cur = con.cursor()

    print("---fetchall()---")
    cur.execute(query)
     # 작업 정상 완료
    con.commit()

    return cur.fetchall()

   
