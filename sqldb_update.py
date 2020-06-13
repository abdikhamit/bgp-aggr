import sqlite3

def SQL_CONNECT():
    try:
        con = sqlite3.connect('BGP_ASN.db')
        create_table_query = '''CREATE TABLE IF NOT EXISTS BGP_ASN (
                                Company_Name TEXT,
                                ASN_Name text,
                                AGR_Subnet text UNIQUE);'''

        cursor = con.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(create_table_query)
        con.commit()
        print("BGP_ASN table created")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)

def SQL_UPDATE(entities):
    con = sqlite3.connect('BGP_ASN.db')
    cursor = con.cursor()
    cursor.execute("INSERT OR REPLACE INTO BGP_ASN(Company_Name, ASN_Name,AGR_Subnet)VALUES(?, ?, ?)", entities)
    con.commit()
