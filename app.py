import connection_info as c
import psycopg2


for x in range(0, 10000):
    port = "0000"
    if x < 10:
        port = "000%s" % str(x)
    elif x < 100:
        port = "00%s" % str(x)
    elif x < 1000:
        port = "0%s" % str(x)
    else:
        port = x

    print("Looking for connection to %s at %s:%s" % (c.db_name, c.host, port), end="\r")

    try:
        conn = psycopg2.connect(
            user=c.user,
            password=c.password,
            host=c.host,
            port=port,
            database=c.db_name
        )
        print("")
        print("Connection to %s found at %s:%s" % (c.db_name, c.host, port))
        conn.close()
        break

    except:
        continue