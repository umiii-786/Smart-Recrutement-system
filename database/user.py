from connectDb import get_connection

def create_user(id:str, email: str,
                password:str,role:str,
                assosiated_with:str):
    conn = get_connection()
    print('user wala run hoya')
    try:
        with conn.cursor() as cursor:
            print('cursor run hoya')
            sql = "INSERT INTO user (id, email,password,role,assosiated_with) VALUES (%s,%s,%s,%s, %s);"

            cursor.execute(sql, (id,email,password,role,assosiated_with))
            print('cursor executed ')
        print('create kr rha hn ')
        conn.commit()
        print('user created successfully')
        return {"success":True}
    
    except Exception as e:
        print(e)
        return {'success':False,'error':e}
    finally:
        conn.close()

def get_user(email: str, password: str = None):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            if password:
                sql = "SELECT * FROM user WHERE email=%s AND password=%s;"
                cursor.execute(sql, (email, password))
            else:
                sql = "SELECT * FROM user WHERE email=%s;"
                cursor.execute(sql, (email,))

            result = cursor.fetchall()
            return {"success": result}

    except Exception as e:
        return {"success": False, "error": str(e)}

    finally:
        conn.close()
