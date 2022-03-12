from asyncio.windows_events import NULL
from multiprocessing import connection
import sqlite3

def main():
    connection = sqlite3.connect('sf_food_program_db_project_ver.sqlite')

    select = connection.cursor()
    #Create table
    #select.execute("DROP TABLE IF EXISTS businesses2")
    select.execute("DROP TABLE IF EXISTS areas")
    select.execute("DROP TABLE IF EXISTS composites")
    select.execute('''CREATE TABLE IF NOT EXISTS composites (composite_id integer PRIMARY KEY, composite_name string, user_id integer)''')
    select.execute('''CREATE TABLE IF NOT EXISTS areas (area_id integer NOT NULL, latitude1 float, longitude1 float,
            latitude2 float, longitude2 float, composite_id integer, FOREIGN KEY(composite_id) REFERENCES composites(composite_id))
            ''')

    select.execute("SELECT MAX(composite_id) FROM composites")
    maxcomposite_id = 0
    fetch = select.fetchone()
    if fetch[0] is not None:
        maxcomposite_id = fetch[0] + 1
    print(maxcomposite_id)

    select.execute("SELECT MAX(area_id) FROM areas")
    maxarea_id = 0
    fetch = select.fetchone()
    if fetch[0] is not None:
        maxarea_id = fetch[0] + 1
    print(maxarea_id)

    #Insert an area
    area_name = str(input("Enter the name of the composite area: "))

    select.execute("INSERT INTO composites(composite_id, composite_name, user_id) VALUES (?,?,?)", (maxcomposite_id, area_name, 0))
    connection.commit()

    val = int(input("Add area for this composite, or press 0 to stop: "))
    while val != 0:
        latitude1 = float(input("Enter latitude of top left point: "))          #assign to latitude1
        longitude1 = float(input("Enter longitude of top left point: "))        #assign to longitude1
        latitude2 = float(input("Enter latitude of bottom right point: "))      #assign to latitude2
        longitude2 = float(input("Enter longitude of bottom right point: "))    #assign to longitude2
        select.execute('''INSERT INTO areas(area_id, latitude1, longitude1, latitude2, longitude2, composite_id) VALUES(?,?,?,?,?,?)
                        ''', (maxarea_id, latitude1, longitude1, latitude2, longitude2, maxcomposite_id))
        connection.commit()
        maxarea_id += 1
        val = int(input("Press 0 to stop, press any other key to continue: "))

    #Delete area
    iddelete = int(input("Enter the id of area to delete: "))
    select.execute("DELETE FROM areas WHERE area_id = ?", (iddelete,))
    connection.commit()
    

if __name__ == "__main__":
    main()