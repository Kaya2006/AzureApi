import os, pyodbc
from fastapi import FastAPI, Request
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

def get_conn():
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASS')};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str)

@app.post("/items")
async def opslaan(request: Request):
    data = await request.json()
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (metric_naam, bron, waarde) VALUES (?, ?, ?)", 
                   (data['metric_naam'], data['bron'], data['waarde']))
    conn.commit()
    return {"status": "success"}

@app.get("/health")
def health(): return {"status": "ok"}