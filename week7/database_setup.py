import dblib

gradebook_db = dblib.GradeBookDatabase()
gradebook_db.create_table()
gradebook_db.fill_data() #this method populates the table with some initial data
