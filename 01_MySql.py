import pymysql


def main():
    conn = pymysql.connect(host='192.168.1.13', port=3306,
                           user='root', password='123456',
                           db='school', charset='utf8')

    print(conn)


if __name__ == '__main__':
    main()
