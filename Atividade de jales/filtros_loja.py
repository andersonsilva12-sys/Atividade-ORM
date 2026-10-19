from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

with Session(engine) as session:

    produtos_estoque = session.query(Produto).filter_by(
        em_estoque=True
    ).all()

    print("\n--- Produtos em estoque ---")
    if produtos_estoque:
        for produto in produtos_estoque:
            print(produto)
    else:
        print("Nenhum produto em estoque.")

    produtos_gamer = session.query(Produto).filter(
        Produto.preco > 100,
        Produto.nome.ilike("%Gamer%")
    ).all()

    print("\n--- Produtos Gamer acima de R$ 100,00 ---")
    if produtos_gamer:
        for produto in produtos_gamer:
            print(produto)
    else:
        print("Nenhum produto Gamer acima de R$ 100,00.")
