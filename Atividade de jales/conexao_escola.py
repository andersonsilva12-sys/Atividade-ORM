from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///:memory:", echo=True)

with engine.connect() as conexao:
    resultado = conexao.execute(text("SELECT sqlite_version()"))
    print("Versão do SQLite:", resultado.scalar())