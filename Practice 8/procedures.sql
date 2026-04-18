-- Procedure 1: upsert a single contact (insert or update phone if username exists)
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_username VARCHAR, p_first VARCHAR, p_last VARCHAR, p_phone VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE username = p_username) THEN
        UPDATE contacts
        SET phone      = p_phone,
            first_name = COALESCE(NULLIF(p_first, ''), first_name),
            last_name  = COALESCE(NULLIF(p_last,  ''), last_name)
        WHERE username = p_username;
    ELSE
        INSERT INTO contacts(username, first_name, last_name, phone)
        VALUES (p_username, p_first, p_last, p_phone);
    END IF;
END;
$$;

-- Procedure 2: bulk insert from array, validate phone with IF, return invalid rows
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    p_data TEXT[][],           -- array of [username, first, last, phone]
    OUT invalid_rows TEXT
)
LANGUAGE plpgsql AS $$
DECLARE
    row TEXT[];
    result TEXT := '';
BEGIN
    FOREACH row SLICE 1 IN ARRAY p_data LOOP
        IF row[4] !~ '^\+?[0-9\s\-\(\)]{7,20}$' THEN
            result := result || 'INVALID PHONE: ' || row[1] || ' -> ' || row[4] || E'\n';
        ELSIF row[1] IS NULL OR row[1] = '' THEN
            result := result || 'MISSING USERNAME: ' || row[4] || E'\n';
        ELSE
            CALL upsert_contact(row[1], row[2], row[3], row[4]);
        END IF;
    END LOOP;
    invalid_rows := COALESCE(NULLIF(result, ''), 'none');
END;
$$;

-- Procedure 3: delete by username OR phone (or both)
CREATE OR REPLACE PROCEDURE delete_contact(
    p_username VARCHAR DEFAULT NULL,
    p_phone    VARCHAR DEFAULT NULL
)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_username IS NOT NULL AND p_phone IS NOT NULL THEN
        DELETE FROM contacts WHERE username = p_username AND phone = p_phone;
    ELSIF p_username IS NOT NULL THEN
        DELETE FROM contacts WHERE username = p_username;
    ELSIF p_phone IS NOT NULL THEN
        DELETE FROM contacts WHERE phone = p_phone;
    ELSE
        RAISE EXCEPTION 'Provide at least one of: username, phone';
    END IF;
END;
$$;