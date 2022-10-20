CREATE TABLE IF NOT EXISTS accounts (
	id INTEGER PRIMARY KEY,
   	name TEXT NOT NULL,
	surname TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS transaction_types (
	id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS transactions (
	id INTEGER PRIMARY KEY,
   	account_id INTEGER NOT NULL,
	date TEXT DEFAULT 0,
    transaction_type_id INTEGER NOT NULL,
    amount REAL NOT NULL,
	FOREIGN KEY (account_id) REFERENCES accounts (id),
    FOREIGN KEY (transaction_type_id) REFERENCES transaction_types (id)
);


INSERT INTO accounts (name, surname, email)
VALUES('Manuel', 'Corales', 'mcoralesdev@gmail.com');

INSERT INTO transaction_types (id, name)
VALUES (1, 'Debit'), (2, 'Credit');

INSERT INTO transactions (id, account_id, date, transaction_type_id, amount)
VALUES
    (1, 1, '01/04/2022', 2, 31),
    (2, 1, '01/04/2022', 1, 4),
    (3, 1, '01/04/2022', 1, 623),
    (4, 1, '01/04/2022', 2, 1);