CREATE TABLE characters (id INTEGER PRIMARY KEY, name TEXT, race TEXT);

INSERT INTO characters (name, race) VALUES ('frodo baggins', 'Hobbit'),('Legolas', 'ELF'),('Gimli','Dwarf');

select * FROM characters;

INSERT into characters VALUES ('4', 'Aragorn', 'half elf');

SELECT * from characters where name = Aragorn;

sqlite> SELECT * from characters where race = 'elf';
sqlite> SELECT * from characters where race = 'ELF';
-- Conditions are case sensitive!

select * from characters where race = 'ELF' or name = 'Gimli';

update characters set race = 'elf' where name = 'Legolas';

select * from characters order by Name ASC;
--Frodo was at the bottom, sorting is case sensitive. F > f

select 2+2;
-- can perform arithmetic