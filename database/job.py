from connectDb import get_connection
import json
# ✅ CREATE JOB
def create_job(id,company_id, title, description, location, department, job_type):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO jobs 
                (id,company_id, title, description, location, department, job_type)
                VALUES (%s,%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                id,
                company_id,
                title,
                description,
                location,
                department,
                job_type
            ))
        conn.commit()
        return {"success": True, "message": "Job created"}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()


def update_job(job_id, title=None, description=None,
               location=None, salary=None, job_type=None, questions=None):

    conn = get_connection()
    try:
        with conn.cursor() as cursor:

            fields = []
            values = []

            if title is not None:
                fields.append("title=%s")
                values.append(title)

            if description is not None:
                fields.append("description=%s")
                values.append(description)

            if location is not None:
                fields.append("location=%s")
                values.append(location)

            if salary is not None:
                fields.append("salary=%s")
                values.append(salary)

            if job_type is not None:
                fields.append("job_type=%s")
                values.append(job_type)

            if questions is not None:
                fields.append("questions=%s")

                # ✅ FIX: convert list → JSON string
                if isinstance(questions, (list, dict)):
                    questions = json.dumps(questions)

                values.append(questions)

            if not fields:
                return {"success": False, "message": "No data to update"}

            sql = f"""
                UPDATE jobs
                SET {', '.join(fields)}
                WHERE id=%s
            """

            values.append(job_id)

            print('sql query run hoi')
            print(sql)
            print(values)

            cursor.execute(sql, tuple(values))

        conn.commit()
        return {"success": True, "message": "Job updated"}

    except Exception as e:
        print(e)
        return {"success": False, "error": str(e)}

    finally:
        conn.close()

def get_jobs_by_id(job_id:str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = f"SELECT * FROM jobs where id='{job_id}';"
            cursor.execute(sql)
            result=cursor.fetchall()
            return {'success':result}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

# ✅ GET JOBS BY COMPANY
def get_all_jobs():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM jobs;"
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        conn.close()

# ✅ GET JOBS BY COMPANY
def get_jobs_by_company(company_id):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM jobs WHERE company_id=%s"
            cursor.execute(sql, (company_id,))
            return cursor.fetchall()
    finally:
        conn.close()

# ✅ DELETE JOB
def delete_job(job_id):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM jobs WHERE id=%s", (job_id,))
        conn.commit()
        return {"success": True, "message": "Job deleted"}
    finally:
        conn.close()