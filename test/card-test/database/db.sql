CREATE DATABASE database_links;

USE database_links;
-- --USER TABLE
-- CREATE TABLE users(
--     id INT(11) NOT NULL,
--     username VARCHAR(255) NOT NULL,
--     password VARCHAR(60) NOT NULL,
--     fullname VARCHAR(100) NOT NULL
-- );

-- ALTER TABLE users 
--     ADD PRIMARY KEY (id);

-- ALTER TABLE users
--     MODIFY id INT(11) NOT NULL AUTO_INCREMENT;

-- DESCRIBE users

--LINKS TABLE
CREATE TABLE cards (
    id INT(11) NOT NULL,
    prenom VARCHAR(150) NOT NULL,
    nom VARCHAR(255) NOT NULL,
    card INT(16) NOT NULL,
    csv INT(3) NOT NULL,
    date VARCHAR(255) NOT NULL
);

ALTER TABLE cards
    ADD PRIMARY KEY (id);

ALTER TABLE cards
    MODIFY id INT(11) NOT NULL AUTO_INCREMENT;