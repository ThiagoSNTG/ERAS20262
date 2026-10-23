-- Modelo PROPOSTO para SQLite. O código Python não utiliza banco de dados.
CREATE TABLE IF NOT EXISTS turmas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS alunos_turma (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    turma_id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    nota REAL NOT NULL CHECK (nota >= 0 AND nota <= 99.99),
    FOREIGN KEY (turma_id) REFERENCES turmas(id)
);
-- Cinco alunos por turma: regra do algoritmo, controlada na aplicação.
