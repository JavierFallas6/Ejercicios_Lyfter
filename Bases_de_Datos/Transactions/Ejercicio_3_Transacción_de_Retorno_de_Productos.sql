SET search_path TO transactions_exercise;
DO $$


DECLARE 

	variable_product_ID INTEGER;
	variable_quantity INTEGER;
	variable_status VARCHAR(30);
	variable_bill_ID INTEGER;

BEGIN
	variable_status := 'Retornada';
	variable_bill_ID := 3;
	

    SELECT ID 
    INTO variable_bill_ID
    FROM bills
    WHERE ID = variable_bill_ID;

    IF variable_bill_ID IS NULL THEN
      RAISE EXCEPTION 'Factura no existe. Abortando transacción.';
    END IF;
	
    SELECT product_id, quantity 
    INTO variable_product_ID, variable_quantity
    FROM products_per_bill
    WHERE bill_id = variable_bill_ID;
	
	UPDATE bills 
	SET status = variable_status
    WHERE ID = variable_bill_ID;

	UPDATE products
	SET stock_available = stock_available + variable_quantity
	WHERE ID = variable_product_ID;
	
END $$;