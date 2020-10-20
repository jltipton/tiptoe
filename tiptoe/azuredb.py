import psycopg2
import azure.functions as func



class AzureDBConn:
    cursor = ""
    conn = ""

    def __enter__(self, azure_config):
        host = azure_config['host']
        dbname = azure_config['dbname']
        user = azure_config['user']
        password = azure_config['password']
        sslmode = "require"

        # Construct connection string
        conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
            host, user, dbname, password, sslmode
        )
        self.conn = psycopg2.connect(conn_string)
        print("Connection established")

        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
