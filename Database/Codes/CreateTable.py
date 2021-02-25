import sqlite3
print(sqlite3.version)
print(sqlite3.sqlite_version)

conn = sqlite3.connect("shop.db", isolation_level=None)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS product \
    (name VARCHAR(20), thumbnail VARCHAR(100), price VARCHAR(20), discountPrice VARCHAR(20), number INT PRIMARY KEY)")

c.execute("CREATE TABLE IF NOT EXISTS store \
    (_id INT AUTO_INCREMENT, name CHAR(20) NOT NULL)")


# c.execute("INSERT INTO product\
#     VALUES('램스킨 더 파우치 백','https://cdn.jentestore.io/resource/products/151092/151092_1.jpg', '3,953,000', '2,753,000', 151092)")
# c.execute("INSERT INTO product\
#     VALUES('램스킨 더 체인 카세트백','https://cdn.jentestore.io/resource/products/150709/150709_1.jpg', '3,953,000', '2,753,000', 150709)")
