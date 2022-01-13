import pymysql


def main():
    conn = pymysql.connect(host='192.168.1.13', port=3306,
                           user='root', password='123456',
                           db='school', charset='utf8')
    try:
        with conn.cursor() as cursor:
            result = cursor.execute('insert tb_college values( 5, "水利学院","www.baidu.com" );')
            print(result)
        conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    main()
