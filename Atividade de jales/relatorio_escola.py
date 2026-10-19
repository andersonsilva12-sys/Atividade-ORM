from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from modelos_escola import Aluno

engine = create_engine("sqlite:///escola.db", echo=True)

with Session(engine) as session:

    relatorio = (
        session.query(
            Aluno.turma_id,
            func.count(Aluno.id).label("total_alunos")
        )
        .group_by(Aluno.turma_id)
        .having(func.count(Aluno.id) > 30)
        .all()
    )

    print("\n--- Relatório de Capacidade das Turmas ---")

    for turma_id, total_alunos in relatorio:
        print(f"Turma ID: {turma_id}")
        print(f"Total de alunos: {total_alunos}")
        print("-" * 35)
