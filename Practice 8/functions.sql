-- Function 1: search contacts by pattern (name, surname, or phone)
CREATE OR REPLACE FUNCTION search_contacts(p TEXT)
RETURNS TABLE(username VARCHAR, first_name VARCHAR, last_name VARCHAR, phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT c.username, c.first_name, c.last_name, c.phone
    FROM contacts c
    WHERE c.username   ILIKE '%' || p || '%'
       OR c.first_name ILIKE '%' || p || '%'
       OR c.last_name  ILIKE '%' || p || '%'
       OR c.phone      LIKE  '%' || p || '%';
END;
$$;

-- Function 2: paginated query using LIMIT / OFFSET
CREATE OR REPLACE FUNCTION get_contacts_paged(lim INT, off INT)
RETURNS TABLE(username VARCHAR, first_name VARCHAR, last_name VARCHAR, phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT c.username, c.first_name, c.last_name, c.phone
    FROM contacts c
    ORDER BY c.username
    LIMIT lim OFFSET off;
END;
$$;