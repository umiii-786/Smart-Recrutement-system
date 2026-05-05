# ✅ CREATE COMPANY
from connectDb import get_connection
def create_company(id,company_name, industry, size, logo_url):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO company 
                (id,company_name, industry, size, logo_url)
                VALUES (%s,%s, %s, %s, %s)
            """
            cursor.execute(sql, (
                id,
                company_name,
                industry,
                size,
                logo_url
            ))
        conn.commit()
        return {"success": True, "message": "Company created"}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        conn.close()



def get_company(id:str):
    conn=get_connection()
    try:
        with conn.cursor() as cursor:
            sql=f"SELECT * FROM company where id='{id}';"
            cursor.execute(sql)
            result = cursor.fetchall()
            return {"success":result}
    except Exception as e:
        return {"success": False,'error':e}
    finally:
        conn.close()



# ✅ UPDATE COMPANY (EDIT INFO)
def update_company(company_id, company_name=None, email=None,
                   industry=None, headcount=None, logo_url=None):
    
    conn = get_connection()
    try:
        with conn.cursor() as cursor:

            fields = []
            values = []

            if company_name:
                fields.append("company_name=%s")
                values.append(company_name)

            if email:
                fields.append("email=%s")
                values.append(email)

            if industry:
                fields.append("industry=%s")
                values.append(industry)

            if headcount:
                fields.append("headcount=%s")
                values.append(headcount)

            if logo_url:
                fields.append("logo_url=%s")
                values.append(logo_url)

            if not fields:
                return {"success": False, "message": "No data to update"}

            sql = f"""
                UPDATE companies 
                SET {', '.join(fields)} 
                WHERE id=%s
            """

            values.append(company_id)

            cursor.execute(sql, tuple(values))

        conn.commit()
        return {"success": True, "message": "Company updated"}

    except Exception as e:
        return {"success": False, "error": str(e)}

    finally:
        conn.close()