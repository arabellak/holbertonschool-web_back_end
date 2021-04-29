-- Creates a table users

CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    PRIMARY KEY (id)
)
