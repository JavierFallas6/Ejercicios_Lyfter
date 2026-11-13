SET search_path TO transactions_exercise;
DO $$


DECLARE 
	variable_available_stock INTEGER;
	variable_user VARCHAR(50);
	variable_user_ID INTEGER;
	variable_product_name VARCHAR(30);
	variable_product_ID INTEGER;
	variable_quantity INTEGER;
	variable_status VARCHAR(30);
	variable_bill_ID INTEGER;

BEGIN

	variable_user := 'Ana';
	variable_product_name := 'Monitor';
	variable_quantity := 4;
	variable_status := 'En Proceso';
	variable_bill_ID := 3; -- Queria ponerlo como autoincrementar pero se me hizo un colocho para guardarlo entonces lo pase a ser manual
	
	--(stock_available - variable_quantity, lo puse pensando en si la cantidad se le resta al stock y quedamos debiendo)
    SELECT stock_available - variable_quantity, ID
    INTO variable_available_stock, variable_product_ID
    FROM products
    WHERE product_name = variable_product_name;

    IF variable_available_stock IS NULL OR variable_available_stock < 1 THEN
      RAISE EXCEPTION 'Stock insuficiente. Abortando transacción.';
    END IF;

    SELECT user_name, ID
    INTO variable_user, variable_user_ID
    FROM users
    WHERE user_name = variable_user;
	
    IF variable_user IS NULL THEN
      RAISE EXCEPTION 'User no encontrado. Abortando transacción.';
    END IF;

	INSERT INTO bills (ID,user_id,status)
	VALUES (variable_bill_ID,variable_user_ID,variable_status);

	INSERT INTO products_per_bill (bill_id,product_id,quantity)
	VALUES (variable_bill_ID,variable_product_ID,variable_quantity);
	
	UPDATE products
	SET stock_available = variable_available_stock
	WHERE product_name = variable_product_name;
	

END $$;