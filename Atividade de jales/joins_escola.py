from sqlalchemy import create_engine, or_
from sqlalchemy.orm import Session
from modelos_escola import Aluno, Turma

engine = create_engine("sqlite:///escola.db", echo=True)

with Session(engine) as session:

    consulta_alunos = (
        session.query(Aluno, Turma.nome_turma)
        .outerjoin(Turma, Aluno.turma_id == Turma.id)
        .all()
    )

    print("\n--- Alunos e suas turmas ---")

    for aluno, nome_turma in consulta_alunos:
        turma = nome_turma if nome_turma is not None else "Sem turma"
        print(f"Aluno: {aluno.nome} | Turma: {turma}")

    alunos_sem_turma = (
        session.query(Aluno)
        .outerjoin(Turma, Aluno.turma_id == Turma.id)
        .filter(
            or_(
                Aluno.turma_id.is_(None),
                Turma.id.is_(None)
            )
        )
        .all()
    )

    print("\n--- Alunos sem turma vinculada ---")

    for aluno in alunos_sem_turma:
        print(f"Aluno: {aluno.nome} | Matrícula: {aluno.matricula}")
