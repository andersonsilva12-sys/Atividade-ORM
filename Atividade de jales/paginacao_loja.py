from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from modelos_loja import Produto

engine = create_engine("sqlite:///loja_virtual.db", echo=True)

with Session(engine) as session:

    total_produtos = session.query(Produto).count()

    print(f"\nTotal de produtos cadastrados: {total_produtos}")

    categorias = (
        session.query(Produto.categoria_id)
        .distinct()
        .all()
    )

    print("\nCategorias distintas presentes nos produtos:")

    for categoria in categorias:
        print(f"Categoria ID: {categoria[0]}")

    tamanho_pagina = 5
    pagina_atual = 2

    produtos = (
        session.query(Produto)
        .order_by(Produto.preco.desc())
        .limit(tamanho_pagina)
        .offset((pagina_atual - 1) * tamanho_pagina)
        .all()
    )

    print("\nProdutos da segunda página, do mais caro ao mais barato:")

    for produto in produtos:
        print(f"Nome: {produto.nome} | Preço: R$ {produto.preco:.2f}")
