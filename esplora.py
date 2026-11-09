from app.models import Utente
from pydantic import ValidationError

utenti_validi = [
    {
        "id": 1,
        "nome": "Mario Rossi",
        "email": "mario@example.com",
        "eta": 25,
        "ruolo": "admin",
        "tags": ["python", "backend"]
    },
    {
        "id": 2,
        "nome": "Anna Bianchi",
        "email": "anna@example.com",
        "eta": 30,
        "ruolo": "user",
        "tags": ["react", "frontend"]
    },
    {
        "id": 3,
        "nome": "Luca Verdi",
        "email": "luca@example.com",
        "eta": None,
        "ruolo": "user",
        "tags": []
    },
    {
        "id": 4,
        "nome": "Sara Neri",
        "email": "sara@example.com",
        "eta": 19,
        "ruolo": "admin",
        "tags": ["fastapi"]
    },
    {
        "id": 5,
        "nome": "Paolo Blu",
        "email": "paolo@example.com",
        "eta": 45,
        "ruolo": "user"
    }
]


utenti_non_validi = [
    {
        "id": "abc",
        "nome": "Mario Rossi",
        "email": "mario@example.com",
        "eta": 25,
        "ruolo": "admin"
    },
    {
        "id": 2,
        "nome": "Anna Bianchi",
        "email": "annaexample.com",
        "eta": 30,
        "ruolo": "user"
    },
    {
        "id": 3,
        "nome": "Luca Verdi",
        "email": "luca@example.com",
        "eta": 200,
        "ruolo": "user"
    },
    {
        "id": 4,
        "nome": "Sara Neri",
        "email": "sara@example.com",
        "eta": 19,
        "ruolo": "boss"
    },
    {
        "id": 5,
        "nome": "",
        "email": "paolo@example.com",
        "eta": 45,
        "ruolo": "user"
    }
]



def testa_utenti(nome_lista, utenti):
    print(f"-----{nome_lista:_<40}-----")
    for i, dati in enumerate(utenti, start=1):
        try: 
            utente = Utente.model_validate(dati)
            print(f"\nUtente {i} valido:")
            print(utente)
        except ValidationError as e:
            for err in e.errors():
                print(err['loc'], err['type'], err['msg'])


testa_utenti("Utenti validi", utenti_validi)
testa_utenti("Utenti non validi", utenti_non_validi)
