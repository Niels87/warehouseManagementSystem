DROP PROCEDURE IF EXISTS search_by_name;
--#--new--#
CREATE PROCEDURE search_by_name (IN search_name VARCHAR(255), OUT result VARCHAR(255))
Begin
	SELECT * FROM products WHERE products.name LIKE search_name;
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
CREATE PROCEDURE update_item (IN item_id INT, IN field_to_update VARCHAR(255), IN new_val VARCHAR(255))
Begin
	SET @update_query = CONCAT("UPDATE products SET ", field_to_update, "='", new_val, "' WHERE ID = ", item_id );
	PREPARE query FROM @update_query;
	EXECUTE query;
	DEALLOCATE PREPARE query;
END
