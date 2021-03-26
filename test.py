import psycopg2

def main():
    
    #creating a connection and cursor to the database
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=postgres port=5432")
    cur = conn.cursor()

    #test songplays
    select_stmt= "SELECT * FROM songplays LIMIT 5"
    cur.execute(select_stmt)
    result=cur.fetchall()
    for i in result:
        print(i)

    #test users
    select_stmt= "SELECT * FROM users LIMIT 5"
    cur.execute(select_stmt)
    result=cur.fetchall()
    for i in result:
        print(i)

    #test time
    select_stmt= "SELECT * FROM time LIMIT 5"
    cur.execute(select_stmt)
    result=cur.fetchall()
    for i in result:
        print(i)

    #test songs
    select_stmt= "SELECT * FROM songs LIMIT 5"
    cur.execute(select_stmt)
    result=cur.fetchall()
    for i in result:
        print(i)

    #test artists
    select_stmt= "SELECT * FROM artists LIMIT 5"
    cur.execute(select_stmt)
    result=cur.fetchall()
    for i in result:
        print(i)

    #closing the connection
    conn.close()


if __name__ == "__main__":
    main()