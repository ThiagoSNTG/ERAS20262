-- Modelo PROPOSTO para SQLite. O código Python não utiliza banco de dados.
-- Apenas totaliza votos por opção; não identifica eleitores.
CREATE TABLE IF NOT EXISTS opcoes_votacao (
    id INTEGER PRIMARY KEY,
    descricao TEXT NOT NULL,
    total_votos INTEGER NOT NULL DEFAULT 0 CHECK (total_votos >= 0)
);
INSERT OR IGNORE INTO opcoes_votacao (id, descricao, total_votos)
VALUES (1, 'Opção 1', 0), (2, 'Opção 2', 0), (3, 'Opção 3', 0);
