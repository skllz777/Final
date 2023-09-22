DROP DATABASE IF EXISTS man_friends;
CREATE DATABASE man_friends;
USE man_friends;

DROP TABLE IF EXISTS parent_class;
CREATE TABLE parent_class (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    birthday DATE
) COMMENT 'Родительский класс';

INSERT INTO `parent_class` VALUES
('1', 'Верблюд_1', '2010-05-18'),
('2', 'Осёл_1', '2011-06-19'),
('3', 'Лошадь_1', '2012-07-20'),
('4', 'Шарик', '2013-08-21'),
('5', 'Матроскин', '2014-09-22'),
('6', 'Хоми', '2020-10-23');

DROP TABLE IF EXISTS pets;
CREATE TABLE pets (
	id SERIAL,
	parent_id BIGINT UNSIGNED NOT NULL,
    learned_commands VARCHAR(120),
    FOREIGN KEY (parent_id) REFERENCES parent_class(id) ON DELETE CASCADE
) COMMENT 'Домашние животные';

INSERT INTO `pets` VALUES
('1','4', 'голос, фас, апорт'),
('2','5', 'голос, фу'),
('3','6', 'голос');

DROP TABLE IF EXISTS pack_animals;
CREATE TABLE pack_animals (
	id SERIAL,
	parent_id BIGINT UNSIGNED NOT NULL,
    capacity_kg INT,
    FOREIGN KEY (parent_id) REFERENCES parent_class(id) ON DELETE CASCADE
) COMMENT 'Вьючные животные';

INSERT INTO `pack_animals` VALUES
('4','1', '250'),
('5','2', '100'),
('6','3', '90');

DROP TABLE IF EXISTS dogs;
CREATE TABLE dogs (
	id SERIAL,
	pets_parent_id BIGINT UNSIGNED NOT NULL,
    breed VARCHAR(120),
    FOREIGN KEY (pets_parent_id) REFERENCES pets(parent_id) ON DELETE CASCADE
) COMMENT 'Собаки';

INSERT INTO `dogs` VALUES
('1','4', 'австралийская овчарка');

DROP TABLE IF EXISTS cats;
CREATE TABLE cats (
	id SERIAL,
	pets_parent_id BIGINT UNSIGNED NOT NULL,
    breed VARCHAR(120),
    FOREIGN KEY (pets_parent_id) REFERENCES pets(parent_id) ON DELETE CASCADE
) COMMENT 'Кошки';

INSERT INTO `cats` VALUES
('2','5', 'абиссинская');

DROP TABLE IF EXISTS hamsters;
CREATE TABLE hamsters (
	id SERIAL,
	pets_parent_id BIGINT UNSIGNED NOT NULL,
    breed VARCHAR(120),
    FOREIGN KEY (pets_parent_id) REFERENCES pets(parent_id) ON DELETE CASCADE
) COMMENT 'Хомяки';

INSERT INTO `hamsters` VALUES
('3','6', 'джунгарский');

DROP TABLE IF EXISTS camels;
CREATE TABLE camels (
	id SERIAL,
	pack_parent_id BIGINT UNSIGNED NOT NULL,
    breed VARCHAR(120),
    FOREIGN KEY (pack_parent_id) REFERENCES pack_animals(parent_id) ON DELETE CASCADE
) COMMENT 'Верблюды';

INSERT INTO `camels` VALUES
('1','1', 'арвана');

DROP TABLE IF EXISTS donkeys;
CREATE TABLE donkeys (
	id SERIAL,
	pack_parent_id BIGINT UNSIGNED NOT NULL,
    breed VARCHAR(120),
    FOREIGN KEY (pack_parent_id) REFERENCES pack_animals(parent_id) ON DELETE CASCADE
) COMMENT 'Ослы';

INSERT INTO `donkeys` VALUES
('1','2', 'пиренейская');

DROP TABLE IF EXISTS horses;
CREATE TABLE horses (
	id SERIAL,
	pack_parent_id BIGINT UNSIGNED NOT NULL,
    breed VARCHAR(120),
    FOREIGN KEY (pack_parent_id) REFERENCES pack_animals(parent_id) ON DELETE CASCADE
) COMMENT 'Лошади';

INSERT INTO `horses` VALUES
('1','3', 'абиссинская');

DROP PROCEDURE IF EXISTS man_friends.delete_camels;

DELIMITER $$
$$
CREATE PROCEDURE man_friends.delete_camels()
BEGIN
	DELETE FROM parent_class
	WHERE parent_class.id IN (SELECT pack_parent_id FROM camels);
END$$
DELIMITER ;

CALL  delete_camels();


DROP PROCEDURE IF EXISTS man_friends.combine_horses_and_donkeys;

DELIMITER $$
$$
CREATE PROCEDURE man_friends.combine_horses_and_donkeys()
BEGIN
	DROP TABLE IF EXISTS donkeys_and_horses;
	CREATE TABLE donkeys_and_horses (
	id SERIAL,
	pack_parent_id BIGINT UNSIGNED NOT NULL,
    breed VARCHAR(120),
    FOREIGN KEY (pack_parent_id) REFERENCES pack_animals(parent_id) ON DELETE CASCADE
) COMMENT 'Ослы и лошади';

	INSERT INTO `donkeys_and_horses`(pack_parent_id, breed) SELECT pack_parent_id, breed FROM donkeys;
	INSERT INTO `donkeys_and_horses`(pack_parent_id, breed) SELECT pack_parent_id, breed FROM horses;

	DROP TABLE donkeys;
	DROP TABLE horses;
END$$
DELIMITER ;

CALL combine_horses_and_donkeys();

DROP PROCEDURE IF EXISTS man_friends.combine_horses_and_donkeys;

DELIMITER $$
$$
CREATE PROCEDURE man_friends.create_young_animals()
BEGIN
	DROP TABLE IF EXISTS young_animals;
	CREATE TABLE young_animals (
	id SERIAL,
	parent_id BIGINT UNSIGNED NOT NULL,
	years INT UNSIGNED,
	months INT UNSIGNED,
    FOREIGN KEY (parent_id) REFERENCES parent_class(id) ON DELETE CASCADE
) COMMENT 'Молодые животные';

	INSERT INTO `young_animals`(parent_id, years, months) SELECT id,
	TIMESTAMPDIFF(YEAR, birthday, NOW()) AS pc_years,
	TIMESTAMPDIFF(MONTH, birthday, NOW()) % 12 AS pc_months
	FROM parent_class AS pc
	WHERE TIMESTAMPDIFF(YEAR, birthday, NOW()) > 1;
END$$
DELIMITER ;

CALL create_young_animals();

CREATE OR REPLACE VIEW animals_breeds AS
SELECT pets_parent_id AS parent_id, breed FROM dogs
UNION
SELECT pets_parent_id AS parent_id, breed FROM cats
UNION
SELECT pets_parent_id AS parent_id, breed FROM hamsters
UNION
SELECT pack_parent_id AS parent_id, breed FROM donkeys_and_horses;


DROP PROCEDURE IF EXISTS man_friends.union_all_tables;

DELIMITER $$
$$
CREATE PROCEDURE man_friends.union_all_tables()
BEGIN
	DROP TABLE IF EXISTS all_tables;
	CREATE TABLE all_tables AS
	SELECT pc.*, pets.learned_commands, pa.capacity_kg, ab.breed, ya.years, ya.months FROM parent_class pc
	LEFT JOIN pets
	ON pc.id = pets.parent_id
	LEFT JOIN pack_animals pa
	ON pc.id = pa.parent_id
	LEFT JOIN animals_breeds ab
	ON pc.id = ab.parent_id
	LEFT JOIN young_animals ya
	ON pc.id = ya.parent_id;

END$$
DELIMITER ;

CALL union_all_tables();

SELECT * FROM all_tables;