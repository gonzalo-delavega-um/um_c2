from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    print("Hijo recibiendo: "+conn.recv())
    conn.send("hola mundo")
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print (parent_conn.recv())   # prints "[42, None, 'hello']"
    parent_conn.send("enviando desde el padre...")
    print (parent_conn.recv())
    p.join()
