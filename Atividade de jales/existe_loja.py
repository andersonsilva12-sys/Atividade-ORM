from sqlalchemy import create_engine, exists
from sqlalchemy.orm import Session
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

categoria_id = 1

with Session(engine) as session:
    consulta = session.query(
        exists().where(Produto.categoria_id == categoria_id)
    )

    possui_produtos = consulta.scalar()

    if possui_produtos:
        print(f"A categoria {categoria_id} possui produtos associados.")
    else:
        print(f"A categoria {categoria_id} não possui produtos associados.")
