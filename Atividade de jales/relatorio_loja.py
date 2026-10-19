from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

with Session(engine) as session:

    relatorio = (
        session.query(
            Produto.categoria_id,
            func.avg(Produto.preco).label("preco_medio"),
            func.count(Produto.id).label("total_produtos")
        )
        .group_by(Produto.categoria_id)
        .having(func.avg(Produto.preco) > 250)
        .all()
    )

    print("\n--- Relatório de Produtos por Categoria ---")

    for categoria_id, preco_medio, total_produtos in relatorio:
        print(f"Categoria ID: {categoria_id}")
        print(f"Preço médio: R$ {preco_medio:.2f}")
        print(f"Total de produtos: {total_produtos}")
        print("-" * 35)
