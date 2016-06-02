insert into eyescolor (person_id, color) values (6, "Brown");
insert into eyescolor (person_id, color) values (7, "Green");
CREATE TABLE TVShow (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name char(128) NOT NULL
);
CREATE TABLE TVShowPerson (
    tvshow_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    FOREIGN KEY(person_id) REFERENCES Person(id),
    FOREIGN KEY(tvshow_id) REFERENCES tvshow(id)
);
insert into tvshow (name) values ("Homeland");
insert into tvshow (name) values ("The big bang theory");
insert into tvshow (name) values ("Game of Thrones");
insert into tvshow (name) values ("Breaking bad");
insert into tvshowperson (person_id, tvshow_id) values (4, 2);
insert into tvshowperson (person_id, tvshow_id) values (3, 3);
insert into tvshowperson (person_id, tvshow_id) values (2, 4);
insert into tvshowperson (person_id, tvshow_id) values (3, 5);
insert into tvshowperson (person_id, tvshow_id) values (3, 6);
insert into tvshowperson (person_id, tvshow_id) values (3, 7);
select * from person;
select * from eyescolor;
select * from tvshow;
select * from tvshowperson;
