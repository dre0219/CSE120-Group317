import sqlite3

class DBClass():
    def __init__(self):
        self.coordinates = []
        self.coordinate_array=[]
        
        self.area_id = self.access_most_recent_area()[0]
        self.composite_id = self.access_most_recent_composite()[0]
        print(str(self.area_id) + " " + str(self.composite_id))
               
    def get_db_connect(self):
        """ Attempts to create a connection to the database

        Returns:
            sqlite3 connection: returns the sqlite connection or none if error
        """
        connection = None
        try:
            connection = sqlite3.connect("sf_food_program_db_project_ver.sqlite")
        except sqlite3.error as e:
            print(e)
        return connection
    
    
    def dict_factory(self, cursor, row):
        """ Converts row_factory function to output dictionaries instead of tuples

        Args:
            cursor (_type_):s Database Cursor
            row (_type_): Row of database

        Returns:
            dict: returns a dictionary of values with column names as keys
        """
        return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))
    
    
    def composite_logic(self):
        """ Logic function that uses the shape_querying function to find POI in composite areas

        Returns:
            list: list of data to be displayed on datatable
        """
        data_to_send = []
        for i in self.coordinate_array:
            datas = self.shape_querying(i)
            for j in range(len(datas)):
                if datas[j] not in data_to_send:
                    data_to_send.append(datas[j])
        return data_to_send
    
    
    def save_area_to_db(self, data2):
        print("saving to db")
        connection = self.get_db_connect()
        cursor = connection.cursor()
        cursor.execute('''pragma foreign_keys = ON''')
        connection.commit()
        latitude1 = data2['testcoordNE[lat]']    #assign to latitude1
        longitude1 = data2['testcoordNE[lng]']   #assign to longitude1
        latitude2 = data2['testcoordSW[lat]']    #assign to latitude2
        longitude2 = data2['testcoordSW[lng]']   #assign to longitude2
        composite_id = 1
        self.area_id += 1
        cursor.execute('''INSERT INTO areas(area_id, latitude1, longitude1, latitude2, longitude2, composite_id) VALUES(?,?,?,?,?,?)
                        ''', (self.area_id, latitude1, longitude1, latitude2, longitude2, composite_id))
        connection.commit()
        coordinates = {"lat1": latitude1, "long1": longitude1, "lat2": latitude2, "long2":longitude2}
        self.coordinate_array.append(coordinates)
        return ""
    
    
    def access_most_recent_composite(self):
        print("most recent composite")
        connection = self.get_db_connect()
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM composites WHERE composite_id = (SELECT MAX(composite_id) FROM composites)''')
        composites = cursor.fetchone()
        if composites == None:
            print("No searches yet")
            return 0
        print(composites)
        return composites    
    
    
    def access_most_recent_area(self):
        print("most recent composite")
        connection = self.get_db_connect()
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM areas WHERE area_id = (SELECT MAX(area_id) FROM areas)''')
        area = cursor.fetchone()
        # area = dict(area_id = row[0], lat1 = row[1], long1 = row[2], lat2 = row[3], long2 = row[4], composite_id = row[5]) 
        print(area)
        if area == None:
            print("No areas yet")
            return 0
        print("Accessed most recent area")
        return area
    
    
    def load_areas_from_composite(self, composite_id):
        connection = self.get_db_connect()
        cursor = connection.cursor()
        cursor.execute('''pragma foreign_keys = ON''')
        connection.commit()
        cursor.execute('''SELECT * FROM areas WHERE composite_id = ?''', (composite_id,))
        output_data = cursor.fetchall()
        return output_data


    def delete_area_from_db(self, id):
        connection = self.get_db_connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM areas WHERE area_id = ?", (id,))
        connection.commit()
    
    
    def delete_composites_from_db(self, id):
        connection = self.get_db_connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM areas WHERE composite_id = ?", (id,))
        connection.commit()
        cursor.execute("DELETE FROM composites WHERE composite_id = ?", (id,))
        connection.commit()

        
    def save_composite_to_db(self, composite_id, name):
        print("saving to db")
        connection = self.get_db_connect()
        cursor = connection.cursor()
        cursor.execute('''pragma foreign_keys = ON''')
        connection.commit()
        cursor.execute('''INSERT INTO composites(composite_id, composite_name, user_id) VALUES(?,?,?)
                        ''', (composite_id, name, 0))
        self.composite_id += 1
        connection.commit()
        return ""    


    def shape_querying(self, latestcoords):
        connection = self.get_db_connect()
        connection.row_factory = self.dict_factory
        cursor = connection.cursor()

        cursor.execute('''
        SELECT *
        FROM businesses
        WHERE latitude < ? AND latitude > ? AND longitude > ? AND longitude < ?
        ''', (latestcoords["lat1"],latestcoords["lat2"], latestcoords["long2"], latestcoords["long1"]))

        # # latitude of rectangle is less than the top left y (latitude decreases southward from positive value in northern hemisphere), 
        # # and greater than bottom right's y (going northwards increases latitude)
        # # longitude of rectangle is less than the bottom right's x (longitude increases eastward from negative value in western hemisphere)
        # # and greater than top left's x (longitude decreases westward in western hemisphere)

        
        output_data = cursor.fetchall()


        print(">>>>>> Shape Querying Functions")
        return output_data