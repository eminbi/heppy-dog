import sqlite3
import pandas as pd

def save_to_db(csv_file, db_file):
    data = pd.read_csv(csv_file)
    conn = sqlite3.connect(db_file)
    data.to_sql('features', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    save_to_db("features.csv", "pet_behavior.db")
