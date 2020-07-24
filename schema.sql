CREATE TABLE kayttajat (
    id SERIAL PRIMARY KEY, 
    nimi TEXT, 
    salasana TEXT, 
    email TEXT
);

CREATE TABLE tapahtumat (
    id SERIAL PRIMARY KEY, 
    nimi TEXT, 
    kayttaja INTEGER REFERENCES kayttajat
);

CREATE TABLE osaprojektit (
    id SERIAL PRIMARY KEY, 
    nimi TEXT, 
    budjettisumma INTEGER, 
    tapahtuma INTEGER REFERENCES tapahtumat
);

CREATE TABLE kulukategoriat (
    id SERIAL PRIMARY KEY, 
    nimi TEXT
);

CREATE TABLE maksut (
    id SERIAL PRIMARY KEY, 
    kayttaja INTEGER REFERENCES kayttajat, 
    osaprojekti INTEGER REFERENCES osaprojektit NOT NULL, 
    kulukategoria INTEGER REFERENCES kulukategoriat, 
    saaja TEXT, 
    summa INTEGER, 
    pvm DATE
);

