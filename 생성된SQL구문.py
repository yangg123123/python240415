import sqlite3
import random
import string

class ProductDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                                product_id INTEGER PRIMARY KEY,
                                product_name TEXT NOT NULL,
                                price REAL NOT NULL
                                )''')
        self.conn.commit()

    def insert_product(self, product_name, price):
        self.cursor.execute('''INSERT INTO products (product_name, price)
                                VALUES (?, ?)''', (product_name, price))
        self.conn.commit()

    def update_product(self, product_id, product_name, price):
        self.cursor.execute('''UPDATE products
                                SET product_name = ?, price = ?
                                WHERE product_id = ?''', (product_name, price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''DELETE FROM products WHERE product_id = ?''', (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        self.cursor.execute('''SELECT * FROM products WHERE product_id = ?''', (product_id,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.conn.close()

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_sample_data(db, num_samples):
    for _ in range(num_samples):
        product_name = generate_random_string(10)
        price = random.uniform(10, 1000)
        db.insert_product(product_name, price)

# 데이터베이스 생성
db = ProductDatabase('products.db')

# 샘플 데이터 생성
generate_sample_data(db, 100)

# 특정 제품 조회 예시
product_id = 1
product = db.select_product(product_id)
print("Selected Product:", product)

# 데이터베이스 연결 종료
db.close_connection()
