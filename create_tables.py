import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_existing_tables(cur, conn):
    """
    Drops all existing tables listed in the `drop_table_queries`.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_new_tables(cur, conn):
    """
    Creates necessary tables as defined in `create_table_queries`.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Connects to the Redshift cluster, drops existing tables,
    creates new ones, and closes the connection.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn_params = config['CLUSTER']
    conn = psycopg2.connect(
        host=conn_params['HOST'],
        dbname=conn_params['DB_NAME'],
        user=conn_params['DB_USER'],
        password=conn_params['DB_PASSWORD'],
        port=conn_params['DB_PORT']
    )
    cur = conn.cursor()

    drop_existing_tables(cur, conn)
    create_new_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
