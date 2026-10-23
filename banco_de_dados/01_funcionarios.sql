-- Modelo PROPOSTO para SQLite. O código Python não utiliza banco de dados.
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario NUMERIC NOT NULL CHECK (salario >= 0)
);
-- Até 100 registros: regra aplicada no código, não no SQL.
