SELECT * FROM businesses2

INSERT INTO businesses2 (name, address, city, postal_code, latitude, longitude)
SELECT name, address, city, postal_code, latitude, longitude
FROM businesses

DELETE FROM areas WHERE latitude1 LIKE 37.7711516627233 AND longitude1 LIKE -122.469616958809 AND
latitude2 LIKE 37.754323933666 AND longitude2 LIKE -122.501460144234 AND composite_id = 2;

DELETE FROM areas;

DELETE FROM composites;