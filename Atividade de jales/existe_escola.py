from sqlalchemy import create_engine, select, exists
from sqlalchemy.orm import Session
from modelos_escola import Aluno

engine = create_engine("sqlite:///escola.db", echo=True)

turma_id = 5

with Session(engine) as session:
    consulta = select(
        exists().where(Aluno.turma_id == turma_id)
    )

    possui_alunos = session.execute(consulta).scalar()

    if possui_alunos:
        print(f"Sim, existem alunos matriculados na turma {turma_id}.")
    else:
        print(f"Não existem alunos matriculados na turma {turma_id}.")
