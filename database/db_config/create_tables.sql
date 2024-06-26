-- @block create tables
-- @conn local_mysql
--#--new--#
-- @label Set up products table
CREATE TABLE IF NOT EXISTS products(
    ID          INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(255) NOT NULL,
    category    VARCHAR(255) NOT NULL,
    price       FLOAT NOT NULL,
    count       INT NOT NULL
);
--#--new--#
-- @label Set up Set up transactions table
CREATE TABLE IF NOT EXISTS transactions(
    ID          INT PRIMARY KEY AUTO_INCREMENT,
    type        VARCHAR(255) NOT NULL,
    product_id  INT NOT NULL,
    CONSTRAINT  FK_PRODUCT
    FOREIGN KEY(product_id)
    REFERENCES products(id)
);