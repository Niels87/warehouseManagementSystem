DROP PROCEDURE IF EXISTS search_by_name;
--#--new--#
CREATE PROCEDURE search_by_name (IN search_name VARCHAR(255))
Begin
	SELECT * FROM products WHERE products.name = search_name;
END
--#--new--#
DROP PROCEDURE IF EXISTS add_item;
--#--new--#
CREATE PROCEDURE add_item (IN item_name VARCHAR(255), item_category VARCHAR(255), item_price FLOAT, item_count INT)
Begin
	INSERT INTO products ( name, category, price, count )
	VALUES (item_name, item_category, item_price, item_count);
END
--#--new--#
DROP PROCEDURE IF EXISTS remove_item;
--#--new--#
CREATE PROCEDURE remove_item (IN item_id INT)
Begin
	DELETE FROM products WHERE ID = item_id; 
END
--#--new--#
DROP PROCEDURE IF EXISTS update_item;
--#--new--#
CREATE PROCEDURE update_item (IN item_id INT, update_field VARCHAR(255), new_val VARCHAR(255))
Begin
	UPDATE products SET update_field = new_val WHERE ID = item_id;
END
