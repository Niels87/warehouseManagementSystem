-- @block create product table
-- @conn local_mysql

-- @label Set up DATABASE
CREATE DATABASE IF NOT EXISTS warehouseDB;

-- @label Set up products table
CREATE TABLE IF NOT EXISTS products(
    id          INT AUTO_INCREMENT NOT NULL,
    prod_name   VARCHAR(255) NOT NULL,
    category    VARCHAR(255) NOT NULL,
    price       FLOAT NOT NULL,
    count       INT NOT NULL,
    PRIMARY KEY(id)
);

-- @label Set up Set up transactions table
CREATE TABLE IF NOT EXISTS transactions(
    id          INT PRIMARY KEY AUTO_INCREMENT,
    type        VARCHAR(255) NOT NULL,
    product_id  INT NOT NULL,
    CONSTRAINT  FK_PRODUCT
    FOREIGN KEY(product_id)
    REFERENCES products(id)
);