import pymysql


# "select * from booklist_book where id=%s", [1, ]
def search(sql, *arg):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='bookstore',
                           charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, *arg)

    results = cursor.fetchall()
    # print(results)
    cursor.close()
    conn.close()
    return results


def getone(sql, *arg):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='bookstore',
                           charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, *arg)

    results = cursor.fetchone()
    # print(results)
    cursor.close()
    conn.close()
    return results


def update(sql, *arg):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', database='bookstore',
                           charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, *arg)
    last_row_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return last_row_id

# print(search('desc booklist_book_writer')
# update('update booklist_book set title=%s where id=1',['book666'])
# update('insert into booklist_book(title, writer, press, date) values(%s,%s,%s,%s)',['book999','w555','p5555','2012-03-02'])
