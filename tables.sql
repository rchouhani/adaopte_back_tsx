-- Création des tables dans le bon ordre

CREATE TABLE pets_statuses (
    id serial primary key,
    status_title varchar(255) NOT NULL
);

CREATE TABLE admins (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at DATE DEFAULT NOW() NOT NULL,
    updated_at DATE
);

CREATE TABLE availabilities (
    id SERIAL PRIMARY KEY,
    frequency VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    birthdate DATE NULL,
    password VARCHAR(255) NOT NULL,
    e_mail VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NULL,
    city VARCHAR(255) NOT NULL,
    zipcode VARCHAR(20) NOT NULL,
    motivation TEXT NOT NULL,
    volunteer BOOLEAN DEFAULT FALSE NOT NULL,
    adoptant BOOLEAN DEFAULT FALSE NOT NULL,
    availability_id BIGINT NOT NULL,
    created_at DATE DEFAULT NOW() NOT NULL,
    updated_at DATE,
    FOREIGN KEY (availability_id) REFERENCES availabilities(id)
);

CREATE TABLE donations (
    id SERIAL PRIMARY KEY,
    amount_euros BIGINT NOT NULL,
    user_id BIGINT NOT NULL,
    created_at DATE DEFAULT NOW() NOT NULL,
    updated_at DATE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE pets(
    id Serial Primary Key,
    pet_name varchar(255) NOT NULL,
    status_id bigint,
    birthyear bigint,
    breed varchar(255) NOT NULL,
    pet_type varchar(255) NOT NULL,
    city varchar(255) NOT NULL,
    zipcode varchar(255) NOT NULL,
    pet_description text NOT NULL,
    image_url varchar(255) NOT NULL,
    created_at DATE DEFAULT now() NOT NULL,
    updated_at DATE,
    FOREIGN KEY (status_id) REFERENCES pets_statuses(id)
);

CREATE TABLE petting_dates (
    id serial primary key,
    user_id bigint,
    pet_id bigint,
    appointment date,
    duration_minutes bigint,
    created_at DATE DEFAULT now() NOT NULL,
    updated_at DATE,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (pet_id) REFERENCES pets(id)
);

CREATE TABLE adoptions (
    id serial primary key,
    user_id bigint,
    pet_id bigint,
    adoption_date DATE DEFAULT now(),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (pet_id) REFERENCES pets(id)
);


-- SEEDING des tables 

INSERT INTO pets_statuses (status_title) VALUES
    ('available'),
    ('adopted'),
    ('dead');

INSERT INTO admins (username, password) VALUES
    ('admin', 'rofated');

INSERT INTO availabilities (frequency) VALUES
    ('Une fois par semaine'),
    ('Une fois par mois'),
    ('Une fois par trimestre'),
    ('Une fois par semestre'),
    ('Une fois par an');

INSERT INTO users (firstname, lastname, password, e_mail, city, zipcode, motivation, volunteer, adoptant, availability_id) VALUES
    ('Ada', 'Lovelace', 'adalovelace', 'ada@lovelace.com', 'Paris', 75010, 'J''ai un ami animal', true, false, 4),
    ('Add', 'Option', 'addoption', 'add@option.com', 'Paris', 75010, 'J''ai été adoptée un jour', false, true, 4);

INSERT INTO donations (amount_euros, user_id) VALUES
    (2, 1);

INSERT INTO pets (pet_name, status_id, birthyear, breed, pet_type, city, zipcode, pet_description, image_url) VALUES
    ('Charlie', 1, 2020, 'Pug', 'Chien', 'Lille', '59000', 'Charlie est un petit chien calme et affectueux qui adore les balades tranquilles et les caresses sur le canapé.', '/images/charlesdeluvio-K4mSJ7kc0As-unsplash.jpg'),
    ('Mia', 1, 2023, 'Chat noir et blanc', 'Chat', 'Strasbourg', '67000', 'Mia est une boule de tendresse curieuse et joueuse, toujours prête à ronronner près de vous.', '/images/manja-vitolic-gKXKBY-C-Dk-unsplash.jpg');

INSERT INTO petting_dates (user_id, pet_id, appointment, duration_minutes) VALUES
    (1, 1, now(), 60);

INSERT INTO adoptions (pet_id, user_id, adoption_date) VALUES 
    (2, 2, now());

-- SEEDING VIA PYTHON DJANGO : 

-- Création d'une ligne dans "Users" :
{
"birthdate": "1990-08-22",
"firstname": "Add",
"lastname": "Option",
"password": "addoption",
"email": "add@option.com",
"phone": "0607080901",
"city": "Paris",
"zipcode": "75010",
"motivation": "J'ai été adoptée un jour", 
"volunteer": "False",
"adoptant": "True",
"availability_id": "4"
}

-- Création d'une ligne dans "Pets" :
{
"pet_name": "Charlie",
"status_id": "1",
"birthyear": "2020-01-01",
"breed": "Pug",
"pet_type": "Chien",
"city": "Lille",
"zipcode": "59000",
"pet_description": "Charlie est un petit chien calme et affectueux qui adore les balades tranquilles et les caresses sur le canapé.",
"image_url": "/images/charlesdeluvio-K4mSJ7kc0As-unsplash.jpg"
}

{
"pet_name": "Mia",
"status_id": "1",
"birthyear": "2023-01-01",
"breed": "Chat noir et blanc",
"pet_type": "Chat",
"city": "Strasbourg",
"zipcode": "67000",
"pet_description": "Mia est une boule de tendresse curieuse et joueuse, toujours prête à ronronner près de vous.",
"image_url": "/images/manja-vitolic-gKXKBY-C-Dk-unsplash.jpg"
}

-- Création d'une ligne dans "Petting_dates" :
{
"user_id": "1",
"pet_id": "1",
"appointment": "2025-07-13T16:00",
"duration_minutes": "60"
}

-- Création d'une ligne dans "Adoptions" :
{
"user_id": "2",
"pet_id": "2",
"adoptions_date": "2025-07-05"
}