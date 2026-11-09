# Registrazione Ordini

Progetto Python per la gestione di utenti e ordini, sviluppato progressivamente per esercitarmi con Python, Pydantic, FastAPI e database.

## Obiettivi del progetto

- Creare modelli di dati con Pydantic.
- Validare e gestire i dati degli utenti.
- Gestire ruoli e informazioni personali.
- Sviluppare un sistema di registrazione e gestione ordini.
- Integrare successivamente FastAPI e un database.

## Tecnologie

- Python 3.13
- Pydantic
- EmailStr
- uv (gestione ambiente e dipendenze)
- pytest (test)

## Struttura del progetto

```text
registrazione-ordini/
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── settings.py
├── tests/
├── esplora.py
├── main.py
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```

## Funzionalità

### Step 1 – Modelli e validazione con Pydantic

- [x] Creazione del modello `Ruolo` tramite Enum.
- [x] Creazione del modello `Indirizzo`.
- [x] Creazione del modello `Utente`.
- [x] Validazione dei campi con `Field`.
- [x] Validazione delle email con `EmailStr`.
- [x] Gestione di campi opzionali con `None`.
- [x] Utilizzo di `default_factory` per le liste.
- [x] Preparazione di 5 utenti validi e 5 non validi.
- [x] Test manuale della validazione tramite `esplora.py`.
- [x] Gestione delle eccezioni `ValidationError`.

### Step successivi

- [ ] Organizzazione delle impostazioni in `settings.py`.
- [ ] Creazione dei modelli per gli ordini.
- [ ] Definizione delle relazioni tra utenti e ordini.
- [ ] Implementazione delle funzionalità CRUD.
- [ ] Creazione degli endpoint con FastAPI.
- [ ] Integrazione di un database SQLite.
- [ ] Test automatici con pytest.

## Installazione

Clonare il repository e spostarsi nella cartella del progetto.

Installare le dipendenze:

```bash
uv sync
```

Avviare il progetto:

```bash
uv run main.py
```

Eseguire lo script di esplorazione:

```bash
uv run esplora.py
```

## Test

Eseguire i test automatici con:

```bash
uv run pytest -v
```

## Diario di sviluppo

| Data | Modifica |
|---|---|
| 09/11/2026 | Inizializzazione progetto e primi modelli Pydantic |

---

**Stato del progetto:** In sviluppo 🚧