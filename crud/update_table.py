import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from db import get_db_connection


def update_user(user_id, new_username):
    conn = get_db_connection()

    if conn:
        try:
            cursor = conn.cursor()

            query = "UPDATE users SET name = %s WHERE id = %s;"
            cursor.execute(query, (new_username, user_id))

            conn.commit()
            cursor.close()

            print(f"User {user_id} updated to {new_username}.")

        except Exception as e:
            print(f"Error updating user: {e}")

        finally:
            conn.close()


update_user(4, "KRISHNA M ")