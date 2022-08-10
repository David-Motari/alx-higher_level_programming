-- lists all cities contained in the database hbtn_0d_usa.
SELECT c.id c_id, c.name c_name, s.name s_name
FROM cities c
LEFT JOIN states s
ON s.id = c.state_id 
ORDER BY c_id;
