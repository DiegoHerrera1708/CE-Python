from __future__ import annotations

import os
import sqlite3

from typing import List, Optional
from models import RecursoDigital

def _connect(db_path: str) -> sqlite3.Connection:
    os.makedirs(os.path.dirname(db_path), exist_ok= True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    
    return conn

def init_db(db_path: str) -> None:
    schema = """
    CREATE TABLE IF NOT EXISTS recursos (
        id          INTEGER PRIMARY KEY, 
        tipo        TEXT NOT NULL,
        titulo      TEXT NOT NULL,
        autor       TEXT,
        anio        INTEGER,

        -- LibroDigital
        isbn        TEXT,
        num_pagina  INTEGER,
        formato     TEXT,

        -- VideoCurso
        duracion    INTEGER,
        nivel       TEXT,

        -- Podcast
        episodios  INTEGER,
        url         TEXT
    );

    CREATE INDEX IF NOT EXISTS idx_recursos_tipo ON recursos(tipo);
    CREATE INDEX IF NOT EXISTS idx_recursos_titulo ON recursos(titulo);

    INSERT INTO recursos (id, tipo, titulo, duracion, nivel) VALUES (1, 'Videocurso', 'Prueba', 120, 'Avanzado')
    """

    with _connect(db_path) as conn:
        conn.executescript(schema)

def cargar_recursos(db_path: str)->  List[RecursoDigital]:
    init_db(db_path)

    with _connect(db_path) as conn:
        rows = conn.execute("SELECT * FROM recursos ORDER BY id ASC").fetchall()
    
    recursos: List[RecursoDigital] = []
    for row in rows:
        data = dict(row)