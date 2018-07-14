import sqlite3 as sq


class database_operations:
    def connection(dbname):
        conn = sq.connect(dbname)
        cur=conn.cursor()
        return conn,cur
    
    def insert(conn,cur,tit,auth,year,isbn):
    
        cur.execute("""CREATE TABLE if not exists book(id integer PRIMARY KEY ,
                                                      title text,author text,
                                                      year real,isbn real );""")
        cur.execute("INSERT INTO book(title,author,year,isbn) VALUES(?,?,?,?);",(tit,auth,year,isbn))
        conn.commit()
        print('Insert done')
            
    def update(conn,cur,check,tit,auth,year,isbn):
        cur.execute("UPDATE book set title =? ,author =? ,year= ?,isbn = ? WHERE id =?",(tit,auth,year,isbn,int(check)))
        conn.commit()
    
    def delete(conn,cur,check):
        #check= input("Delete id:")
        cur.execute("DELETE from book WHERE id =?",(int(check),))
        conn.commit()
         
    def search(conn,cur,check):
        #check=input("id")
        cur.execute("SELECT * FROM book WHERE id=?",(check,))
        r=cur.fetchall()
        return r
    def view(conn,cur):
        cur.execute("SELECT * FROM book")
        v=cur.fetchall()
        return v
        
        