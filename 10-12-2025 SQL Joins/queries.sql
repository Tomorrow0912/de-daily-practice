CREATE TABLE weapons (
    id INTEGER PRIMARY KEY,
    character_id INTEGER,
    weapon TEXT
);

INSERT INTO weapons (character_id, weapon)
VALUES (1, 'Sword'),
       (2, 'Bow'),
       (3, 'Axe');

select * FROM weapons;

SELECT characters.id, characters.name, weapons.weapon_name
FROM characters
INNER JOIN weapons ON characters.id = weapons.character_id;

