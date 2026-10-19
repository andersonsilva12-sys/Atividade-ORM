
from sqlalchemy import create_engine
from sqlalchemy.schema import CreateTable
from modelos_escola import Base

engine = create_engine("sqlite:///escola.db", echo=True)

for tabela in Base.metadata.sorted_tables:
    print(f"\nDDL da tabela {tabela.name}:")
    print(CreateTable(tabela).compile(engine))

Base.metadata.create_all(engine)

print("\nBanco da Escola criado com sucesso!")
