from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from modelos_loja import Produto, Categoria

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

with Session(engine) as session:

    consulta_produtos = (
        session.query(Produto.nome, Categoria.nome)
        .join(Categoria, Produto.categoria_id == Categoria.id)
        .all()
    )

    print("\n--- Produtos e suas categorias ---")

    for nome_produto, nome_categoria in consulta_produtos:
        print(f"Produto: {nome_produto} | Categoria: {nome_categoria}")

    consulta_categorias = (
        session.query(Categoria)
        .outerjoin(Produto, Categoria.id == Produto.categoria_id)
        .filter(Produto.id == None)
        .all()
    )

    print("\n--- Categorias sem produtos ---")

    for categoria in consulta_categorias:
        print(f"Categoria órfã: {categoria.nome}")
