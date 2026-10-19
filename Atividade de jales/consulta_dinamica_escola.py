from sqlalchemy import create_engine, case
from sqlalchemy.orm import Session
from modelos_escola import Aluno

engine = create_engine("sqlite:///escola.db", echo=True)

turma_id = 1

with Session(engine) as session:

    consulta = session.query(Aluno).filter(
        Aluno.turma_id == turma_id
    )

    status_idade = case(
        (Aluno.data_nascimento < "2008-01-01", "Nascido antes de 2008"),
        else_="Nascido em 2008 ou depois"
    ).label("status_idade")

    consulta = consulta.add_columns(status_idade)

    resultados = consulta.all()

    print(f"\n--- Alunos da turma {turma_id} ---")

    for aluno, status in resultados:
        print(f"Nome: {aluno.nome}")
        print(f"Matrícula: {aluno.matricula}")
        print(f"Data de nascimento: {aluno.data_nascimento}")
        print(f"Classificação: {status}")
        print("-" * 40)
