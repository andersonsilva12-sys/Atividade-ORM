from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from modelos_escola import Aluno

engine = create_engine("sqlite:///escola.db", echo=True)

with Session(engine) as session:

    total_alunos = session.query(Aluno).count()

    print(f"\nTotal de alunos matriculados: {total_alunos}")

    alunos_ordenados = (
        session.query(Aluno)
        .order_by(Aluno.nome.asc())
        .all()
    )

    print("\nAlunos em ordem alfabética:")

    for aluno in alunos_ordenados:
        print(f"{aluno.nome} - Matrícula: {aluno.matricula}")

    pagina_atual = 3
    tamanho_pagina = 10

    alunos_paginados = (
        session.query(Aluno)
        .order_by(Aluno.nome.asc())
        .offset((pagina_atual - 1) * tamanho_pagina)
        .limit(tamanho_pagina)
        .all()
    )

    print(f"\nAlunos da página {pagina_atual}:")

    for aluno in alunos_paginados:
        print(f"{aluno.nome} - Matrícula: {aluno.matricula}")
