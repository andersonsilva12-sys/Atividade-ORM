from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

with Session(engine) as session:

    consulta = session.query(Produto).filter(
        Produto.em_estoque.is_(True)
    )

    consulta = consulta.add_columns(
        (Produto.preco * 0.85).label("preco_promocional")
    )

    resultados = consulta.all()

    print("\n--- Promoção de Black Friday: 15% de desconto ---")

    for produto, preco_promocional in resultados:
        print(f"Produto: {produto.nome}")
        print(f"Preço original: R$ {produto.preco:.2f}")
        print(f"Preço promocional: R$ {preco_promocional:.2f}")
        print("-" * 40)
