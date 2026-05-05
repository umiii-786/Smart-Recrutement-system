from connectDb import get_connection

def create_candidate(id:str,name: str, internship:int,
            certification:int,
            projects:int,
            hsc:int,
            ssc:int,
            cgpa:float):
    conn = get_connection()
    print('candidate wala run hoya')
    try:
        with conn.cursor() as cursor:
            print('cursor run hoya')
            sql = "INSERT INTO candidate (id,name,internship,certification,projects,hsc,ssc,cgpa) VALUES " \
            "(%s,%s,%s,%s,%s,%s,%s,%s);"

            cursor.execute(sql, (id,name,internship,certification,
                                    projects,hsc,ssc,cgpa
                                 ))
            print('cursor executed ')
        print('create kr rha hn ')
        conn.commit()
        print('candidate created successfully')
        return {"success":True}
    
    except Exception as e:
        print(e)
        return {'success':False,'error':e}
    finally:
        conn.close()


def get_candidate(id:str):
    conn=get_connection()
    try:
        with conn.cursor() as cursor:
            sql=f"SELECT * FROM candidate where id='{id}';"
            cursor.execute(sql)
            result = cursor.fetchall()
            return {"success":result}
    except Exception as e:
        return {"success": False,'error':e}
    finally:
        conn.close()
