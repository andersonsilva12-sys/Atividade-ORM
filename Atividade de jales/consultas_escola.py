from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from modelos_escola import Aluno

engine = create_engine("sqlite:///escola.db", echo=True)

with Session(engine) as session:

    aluno = session.get(Aluno, 1)

    if aluno:
        print("\nAluno encontrado:")
        print(f"Matrícula: {aluno.matricula}")
        print(f"Nome: {aluno.nome}")
    else:
        print("\nAluno com ID 1 não encontrado.")

    alunos = session.query(Aluno).all()

    print("\nTodos os alunos cadastrados:")
    if alunos:
        for aluno in alunos:
            print(aluno)
    else:
        print("Nenhum aluno cadastrado.")

    resultado_rows = session.execute(select(Aluno)).all()

    print("\nResultado de execute(select(Aluno)).all():")
    for linha in resultado_rows:
        print(linha)
        print("Tipo:", type(linha))

    resultado_alunos = session.execute(select(Aluno)).scalars().all()

    print("\nResultado de execute(select(Aluno)).scalars().all():")
    for aluno in resultado_alunos:
        print(aluno)
        print("Tipo:", type(aluno))
