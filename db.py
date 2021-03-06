import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.OperationalError as e:
        print(e)
 
    return None
    
def create_run(conn, run):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO Run(number)
              VALUES(?) '''
    cur = conn.cursor()
    print(run)
    cur.execute(sql, run)
    return cur.lastrowid


def create_scan(conn, scan):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
 
    sql = ''' INSERT INTO Scan(image,number,run)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, scan)
    return cur.lastrowid
