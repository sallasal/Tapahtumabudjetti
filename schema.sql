CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    name TEXT UNIQUE NOT NULL, 
    password TEXT NOT NULL, 
    email TEXT
);

CREATE TABLE projects (
    id SERIAL PRIMARY KEY, 
    name TEXT,
    userid INTEGER REFERENCES users
);

CREATE TABLE subprojects (
    id SERIAL PRIMARY KEY, 
    name TEXT, 
    total INTEGER, 
    project INTEGER REFERENCES projects
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY, 
    name TEXT
    project_id INTEGER REFERENCES projects
);

CREATE TABLE payments (
    id SERIAL PRIMARY KEY, 
    userid INTEGER REFERENCES users, 
    subproject INTEGER REFERENCES subprojects NOT NULL, 
    recipient TEXT, 
    total INTEGER, 
    date DATE
);

CREATE TABLE paymentcategory (
    id SERIAL PRIMARY KEY, 
    payment_id INTEGER, 
    category_id INTEGER
);
