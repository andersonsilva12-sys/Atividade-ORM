from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

with Session(engine) as session:

    id_produto = 1
    produto = session.get(Produto, id_produto)

    if produto:
        print("\nProduto encontrado pelo ID:")
        print(produto)
    else:
        print(f"\nProduto com ID {id_produto} não encontrado.")

    primeiro_produto = session.query(Produto).first()

    if primeiro_produto:
        print("\nPrimeiro produto encontrado:")
        print(primeiro_produto)
    else:
        print("\nNenhum produto cadastrado.")

    consulta = select(Produto)
    produtos = session.execute(consulta).scalars().all()

    print("\nLista de produtos:")
    for produto in produtos:
        print(produto)
