contact_info={
    "Alice": {
        "Phone":"049654321",
        "email":"alice@gmail.com",
        "address": "Rruga kryesore Prishtine",
        "birthday": "18/04/1996"

    },
    "Bob": {
        "Phone": "049654321",
        "email": "bob@gmail.com",
        "address": "Rruga kryesore Prishtine",
        "birthday": "18/04/1996"

    },
    "Eve": {
        "Phone": "049654321",
        "email": "eve@gmail.com",
        "address": "Rruga kryesore Prishtine",
        "birthday": "18/04/1996"

    },
    "Jane": {
        "Phone": "049654321",
        "email": "jane@gmail.com",
        "address": "Rruga kryesore Prishtine",
        "birthday": "18/04/1996"

    },
    "John": {
        "Phone": "049654321",
        "email": "john@gmail.com",
        "address": "Rruga kryesore Prishtine",
        "birthday": "18/04/1996"

    },
}
print(contact_info["Bob"])
print(contact_info["Jane"])

contact_info["Jane"]["Phone"]="049111111"

print(contact_info["Jane"]["Phone"])

