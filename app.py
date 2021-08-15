import sqlite3
import time
from plyer import notification

if __name__=="__main__":
    conn = sqlite3.connect('ca.db')
    cur = conn.execute('''SELECT * FROM Titles''')
    rows=cur.fetchall()
    
    j=0
    while True:
        
        notification.notify(
            title="Time to Read Some news!",
            message=rows[j][0],
            app_icon="icon.ico",
            timeout=20
        )
        time.sleep(10*60)

        j+=1
