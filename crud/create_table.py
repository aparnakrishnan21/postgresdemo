import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection


def create_user_table():
    conn = get_db_connection()

    if conn is not None:
        try:
            cursor = conn.cursor()

            create_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL
            );
            '''

            cursor.execute(create_table_query)
            conn.commit()

            print("Table 'users' created successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            cursor.close()
            conn.close()

create_user_table()