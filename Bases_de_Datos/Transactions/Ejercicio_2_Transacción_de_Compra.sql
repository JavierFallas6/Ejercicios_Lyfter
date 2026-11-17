SET search_path TO transactions_exercise;

CREATE TEMP TABLE purchase_products (
    product_name VARCHAR(30),
    variable_quantity INTEGER
);

INSERT INTO purchase_products
VALUES
    ('Monitor', 4),
    ('Keyboard', 2),
    ('Mouse', 3);

DO $$


DECLARE 
	variable_available_stock INTEGER;
	variable_user VARCHAR(50);
	variable_user_ID INTEGER;
	variable_product_ID INTEGER;
	variable_status VARCHAR(30);
	variable_bill_ID INTEGER;
	item RECORD;

BEGIN

	variable_user := 'Ana';
	variable_status := 'En Proceso';

    FOR item IN
        SELECT product_name, variable_quantity
        FROM purchase_products
    LOOP

        RAISE NOTICE 'Producto: %, Cantidad: %',
            item.product_name, item.variable_quantity;
			
	--(stock_available - variable_quantity, lo puse pensando en si la cantidad se le resta al stock y quedamos debiendo)
    SELECT stock_available - item.variable_quantity, ID
    INTO variable_available_stock, variable_product_ID
    FROM products
    WHERE product_name = item.product_name;

    IF variable_available_stock IS NULL OR variable_available_stock < 0 THEN
      RAISE EXCEPTION 'Stock insuficiente. Abortando transacción.';
    END IF;

    SELECT user_name, ID
    INTO variable_user, variable_user_ID
    FROM users
    WHERE user_name = variable_user;
	
    IF variable_user IS NULL THEN
      RAISE EXCEPTION 'User no encontrado. Abortando transacción.';
    END IF;

	INSERT INTO bills (user_id,status)
	VALUES (variable_user_ID,variable_status)
	RETURNING ID INTO variable_bill_ID;

	INSERT INTO products_per_bill (bill_id,product_id,quantity)
	VALUES (variable_bill_ID,variable_product_ID,item.variable_quantity);
	
	UPDATE products
	SET stock_available = variable_available_stock
	WHERE product_name = item.product_name;
	
    END LOOP;
END $$;