SET search_path TO transactions_exercise;

DROP TABLE IF EXISTS bill_to_return;


-- por si queremos devolver mas de 1 factura
DROP TABLE IF EXISTS bill_to_return;
CREATE TEMP TABLE bill_to_return (
    bill_return_ID INTEGER
);

INSERT INTO bill_to_return
VALUES (1);

DO $$

DECLARE 
    variable_product_ID INTEGER;
    variable_quantity INTEGER;
    variable_status VARCHAR(30);
    variable_bill_ID INTEGER;
    variable_original_status VARCHAR(30);

    item RECORD;
    item_products RECORD;

BEGIN
    variable_status := 'Retornada';

    FOR item IN
        SELECT bill_return_ID
        FROM bill_to_return
    LOOP

        RAISE NOTICE 'Bill ID to return: %',
            item.bill_return_ID;

        SELECT ID, status
        INTO variable_bill_ID, variable_original_status
        FROM bills
        WHERE ID = item.bill_return_ID;

        IF variable_bill_ID IS NULL THEN
            RAISE EXCEPTION 'Factura no existe. Abortando transacción.';
        END IF;

        IF variable_original_status = 'Retornada' THEN
            RAISE EXCEPTION 'Factura Retornada. Abortando transacción.';
        END IF;

        UPDATE bills 
        SET status = variable_status
        WHERE ID = variable_bill_ID;

        FOR item_products IN
            SELECT product_id, quantity
            FROM products_per_bill
            WHERE bill_id = variable_bill_ID
        LOOP

            UPDATE products
            SET stock_available = stock_available + item_products.quantity
            WHERE ID = item_products.product_id;

        END LOOP;

    END LOOP;

END $$;
