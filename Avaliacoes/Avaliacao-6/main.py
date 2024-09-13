import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

# Create the database connection
def get_db_connection():
    conn = sqlite3.connect('dbalunos.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create the Aluno model
class Aluno(BaseModel):
    aluno_nome: str
    endereco: str

# Create the database tables
def create_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS TB_ALUNO (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        aluno_nome TEXT(50) NOT NULL,
                        endereco TEXT(100) NOT NULL)''')
    conn.commit()
    conn.close()

@app.on_event("startup")
async def startup_event():
    create_db()

if __name__ == '__main__':
    create_db()

# Endpoint criar_aluno
@app.post('/alunos/')
async def criar_aluno(aluno: Aluno):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO TB_ALUNO (aluno_nome, endereco) VALUES (?, ?)", (aluno.aluno_nome, aluno.endereco))
        conn.commit()
        conn.close()
        return {"message": "Aluno criado com sucesso"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint listar_alunos
@app.get('/alunos/')
async def listar_alunos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TB_ALUNO")
    alunos = cursor.fetchall()
    conn.close()
    return [{'id': aluno['id'], 'aluno_nome': aluno['aluno_nome'], 'endereco': aluno['endereco']} for aluno in alunos]

# Endpoint listar_um_aluno
@app.get('/alunos/{aluno_id}')
async def listar_um_aluno(aluno_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TB_ALUNO WHERE id=?", (aluno_id,))
    aluno = cursor.fetchone()
    conn.close()
    if aluno:
        return {'id': aluno['id'], 'aluno_nome': aluno['aluno_nome'], 'endereco': aluno['endereco']}
    else:
        raise HTTPException(status_code=404, detail='Aluno não encontrado')

# Endpoint atualizar_aluno
@app.put('/alunos/{aluno_id}')
async def atualizar_aluno(aluno_id: int, aluno: Aluno):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE TB_ALUNO SET aluno_nome=?, endereco=? WHERE id=?", (aluno.aluno_nome, aluno.endereco, aluno_id))
    conn.commit()
    conn.close()
    return {"message": "Aluno atualizado com sucesso"}

# Endpoint excluir_aluno
@app.delete('/alunos/{aluno_id}')
async def excluir_aluno(aluno_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TB_ALUNO WHERE id=?", (aluno_id,))
    conn.commit()
    conn.close()
    return {"message": "Aluno excluído com sucesso"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
