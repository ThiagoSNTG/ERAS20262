-- Modelo PROPOSTO para SQLite. O código Python não utiliza banco de dados.
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nota_final REAL NOT NULL
);
-- Uma chave ID evita depender do nome como identificador do aluno.
-- No Java original, nomes repetidos são guardados na lista,
-- mas apenas a nota mais recente é mantida no mapa de notas.
