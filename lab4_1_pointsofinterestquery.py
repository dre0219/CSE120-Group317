from multiprocessing import connection
import sqlite3

def main():
    connection = sqlite3.connect('sf_food_program_db_project_ver.sqlite')

    select = connection.cursor()
    #Create table
    #select.execute("DROP TABLE IF EXISTS businesses2")
    select.execute('''CREATE TABLE IF NOT EXISTS businesses2 (business_id integer NOT NULL, name varchar, address varchar, 
        city varchar, postal_code integer, latitude float, longitude float)''')

    #Duplicate database values to new table
    #select.execute('''INSERT INTO businesses2 (business_id, name, address, city, postal_code, latitude, longitude) 
    #    SELECT * 
    #    FROM businesses''')
    #connection.commit()

    #Insert new place (first get max business id)
    print("Insert a new place.")
    select.execute("SELECT MAX(business_id) FROM businesses2")
    maxbusiness_id = int(select.fetchone()[0]) + 1
    print(maxbusiness_id)
    
    name = str(input("Enter name of business: "))
    address = str(input("Enter address: "))
    city = str(input("Enter city: "))
    postal_code = int(input("Enter postal code: "))
    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))

    #select.execute("INSERT INTO businesses2(business_id, name, address, city, postal_code, latitude, longitude) values(?, ?, ?, ?, ?, ?, ?)", 
    #    (maxbusiness_id, name, address, city, postal_code, latitude, longitude))
    #connection.commit()

    #Query for list of points
    latitude1 = float(input("Enter latitude of top left point: "))          #assign to latitude1
    longitude1 = float(input("Enter longitude of top left point: "))        #assign to longitude1
    latitude2 = float(input("Enter latitude of bottom right point: "))      #assign to latitude2
    longitude2 = float(input("Enter longitude of bottom right point: "))    #assign to longitude2
    
    select.execute('''
        SELECT *
        FROM businesses2
        WHERE latitude < ? AND latitude > ? AND longitude > ? AND longitude < ?
    ''', (latitude1, latitude2, longitude1, longitude2))
    # latitude of rectangle is less than the top left y (latitude decreases southward from positive value in northern hemisphere), 
    # and greater than bottom right's y (going northwards increases latitude)
    # longitude of rectangle is less than the bottom right's x (longitude increases eastward from negative value in western hemisphere)
    # and greater than top left's x (longitude decreases westward in western hemisphere)

    for row in select.fetchall():
        print(str(row[1]) + ", " + str(row[2]) + ", " + str(row[3]) + ", " + str(row[4]) + ", " + str(row[5]) + ", " + str(row[6]))

    #Delete place
    namedelete = str(input("Enter the name of business to delete: "))
    select.execute("DELETE FROM businesses2 WHERE name = ?", (namedelete,))
    connection.commit()
    

if __name__ == "__main__":
    main()