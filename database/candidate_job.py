from connectDb import get_connection

def get_candidate_job(candidate_id: str, job_id: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = f"select * from  candidate_job where candidate_id='{candidate_id}' and job_id='{job_id}';"
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            return {"success":result}

    except Exception as e:
        return {"success": False, "error": str(e)}

    finally:
        conn.close()


def create_candidate_job(candidate_id: str, job_id: str, resume_path: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO candidate_job (candidate_id, job_id, resume_path)
                VALUES (%s, %s, %s);
            """
            cursor.execute(sql, (candidate_id, job_id, resume_path))
            conn.commit()
            return {"success": True, "message": "Record created successfully"}

    except Exception as e:
        return {"success": False, "error": str(e)}

    finally:
        conn.close()

def update_candidate_video_path(candidate_id:str,job_id:str,video_path:str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            query = """
                UPDATE candidate_job 
                SET interview_video_paths = 
                    CASE 
                        WHEN interview_video_paths IS NULL OR interview_video_paths = '' 
                        THEN %s
                        ELSE CONCAT(interview_video_paths, ',', %s)
                    END
                WHERE candidate_id = %s AND job_id = %s;
                """



            print(query)
            cursor.execute(query, (video_path, video_path, candidate_id, job_id))
            print('query runned')
            conn.commit()

            return {"success": True, "message": "Record updated successfully"}
    
    except Exception as e:
        print(e)
        return {"success": False, "error": str(e)}

    finally:
        conn.close()

def execte_query(sql):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            if "select" in sql:
                    result=cursor.fetchall()
                    return {"success": result, "message": "Candidate Job Table Query Executed" } 
            else:
                conn.commit()
                return  {"success": True, "message": "Candidate Job Table Query Executed" }
                

    
    except Exception as e:
        return {"success": False, "error": str(e)}

    finally:
        conn.close()
            


def update_candidate_job(candidate_id: str, job_id: str,
                         ats_score: float = None,
                         softskill: float = None,
                         amptitude_score: float = None,
                         result:int=None,
                         probablities:str=None

                         ):
    
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            
            fields = []
            values = []

            if ats_score is not None:
                fields.append("ats_score = %s")
                values.append(ats_score)

            if softskill is not None:
                fields.append("softskill = %s")
                values.append(softskill)

            if amptitude_score is not None:
                fields.append("amptitude_score = %s")
                values.append(amptitude_score)

            if result is not None:
                fields.append("result = %s")
                values.append(result)

            if probablities is not None:
                fields.append("probablities = %s")
                values.append(probablities)

            if not fields:
                return {"success": False, "message": "No fields to update"}

            sql = f"""
                UPDATE candidate_job
                SET {', '.join(fields)}
                WHERE candidate_id = %s AND job_id = %s;
            """

            values.extend([candidate_id, job_id])

            cursor.execute(sql, tuple(values))
            conn.commit()

            return {"success": True, "message": "Record updated successfully"}

    except Exception as e:
        return {"success": False, "error": str(e)}

    finally:
        conn.close()