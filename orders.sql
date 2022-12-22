CREATE TABLE IF NOT EXISTS orders(
               order_id VARCHAR(16) NOT NULL,
               customer_name VARCHAR(25),
               drink VARCHAR(15),
               size VARCHAR(10),
               extras VARCHAR(150),
               price REAL,
               PRIMARY KEY(order_id)
)