SET search_path TO transactions_exercise;


DO $$


DECLARE 

	variable_product_ID INTEGER;
	variable_quantity INTEGER;
	variable_status VARCHAR(30);
	variable_bill_ID INTEGER;
	variable_original_status VARCHAR(30);	
	item RECORD;
	
BEGIN
	variable_status := 'Retornada';
	
    FOR item IN
        SELECT ID
        FROM bills
    LOOP

        RAISE NOTICE 'Bill ID: %',
            item.ID;
		
    SELECT ID, status
    INTO variable_bill_ID,variable_original_status
    FROM bills
    WHERE ID = item.ID;

    IF variable_bill_ID IS NULL THEN
      RAISE EXCEPTION 'Factura no existe. Abortando transacción.';
    END IF;
    IF variable_original_status = 'Retornada' THEN
      RAISE EXCEPTION 'Factura Retornada. Abortando transacción.';
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
	
    END LOOP;	
END $$;