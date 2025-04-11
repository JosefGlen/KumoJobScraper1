import sqlite3
import json
from datetime import datetime

def dump_sqlite_jobs():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM jobs_jobs")  # Use actual table name
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]

        fixture_data = []
        for row in rows:
            row_dict = dict(zip(columns, row))
            pk = row_dict.pop("id")  # Use 'id' as PK
            # Format the date if necessary
            if isinstance(row_dict["date"], str):
                row_dict["date"] = row_dict["date"]
            elif isinstance(row_dict["date"], datetime):
                row_dict["date"] = row_dict["date"].strftime("%Y-%m-%d")
            else:
                row_dict["date"] = str(row_dict["date"])

            fixture_data.append({
                "model": "jobs.jobs",  # Format: appname.modelname (all lowercase)
                "pk": pk,
                "fields": row_dict
            })

        with open("jobs_fixture.json", "w") as f:
            json.dump(fixture_data, f, indent=2)

        print("✅ Fixture dumped to jobs_fixture.json")

    finally:
        conn.close()

dump_sqlite_jobs()