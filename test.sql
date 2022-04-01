SELECT * FROM businesses2

INSERT INTO businesses2 (name, address, city, postal_code, latitude, longitude)
SELECT name, address, city, postal_code, latitude, longitude
FROM businesses