from datetime import date
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import Session
from modelos_escola import Aluno, Turma

engine = create_engine("sqlite:///escola.db", echo=True)

with Session(engine) as session:

    turma = session.query(Turma).filter_by(
        nome_turma="3º Ano A"
    ).first()

    print("\n--- Busca pela turma ---")
    if turma:
        print(turma)
    else:
        print("Turma '3º Ano A' não encontrada.")

    alunos_filtrados = session.query(Aluno).filter(
        or_(
            Aluno.data_nascimento > date(2005, 12, 31),
            Aluno.email.endswith("@escola.com")
        )
    ).all()

    print("\n--- Alunos nascidos após 2005 ou com e-mail @escola.com ---")
    if alunos_filtrados:
        for aluno in alunos_filtrados:
            print(aluno)
    else:
        print("Nenhum aluno corresponde aos critérios.")
