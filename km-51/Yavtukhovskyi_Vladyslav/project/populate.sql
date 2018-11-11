

insert into "Userss"(LOGIN, PASSWORD, USER_NAME, DATE_OF_BIRTH) values ('expo', '123456', 'Ya Ya Ya', TO_DATE('03.12.2004'));

insert into "Userss"(LOGIN, PASSWORD, USER_NAME, DATE_OF_BIRTH) values ('expo12', '1234561', 'Ya1 Ya Ya', TO_DATE('03.12.2003'));

insert into "Userss"(LOGIN, PASSWORD, USER_NAME, DATE_OF_BIRTH) values ('expo22', '1234562', 'Ya Ya2 Ya', TO_DATE('03.12.2005'));

insert into "Userss"(LOGIN, PASSWORD, USER_NAME, DATE_OF_BIRTH) values ('expo33', '1234563', 'Ya Ya Ya3', TO_DATE('03.12.2007'));

insert into syndromes values ('leg is broken');

insert into syndromes values ('arm is broken');

insert into syndromes values ('Achu');

insert into syndromes values ('Not planned');

insert into weakness values ('broken leg');
insert into weakness values ('broken arm');

insert into weakness values('broken arm and achu');
insert into weakness values ('good day sir');
insert into medicine values ('new arm');
insert into medicine values ('new leg');
insert into medicine values ('nothing shall help');
insert into medicine values ('pika');

insert into weakness_has_syndrom values ('leg is broken', 'broken leg' );
insert into weakness_has_syndrom values ( 'arm is broken', 'broken arm');
insert into weakness_has_syndrom values ( 'arm is broken', 'broken arm and achu');
insert into weakness_has_syndrom values ('Achu','broken arm and achu');

insert into medicine_is_for_weakness values ( 'broken arm', 'new arm');
insert into medicine_is_for_weakness values ('broken leg', 'new leg');
insert into medicine_is_for_weakness values ('good day sir','pika');
insert into medicine_is_for_weakness values ('broken arm and achu', 'pika');

insert into healing_histories(id, num_of_record, login, name_of_medicine, name_of_weakness, name_of_syndrom) values (1, 1,
'expo12', 'pika', 'broken arm and achu', 'Achu');

insert into healing_histories(id, num_of_record, login, name_of_medicine, name_of_weakness, name_of_syndrom) values (2, 2,
'expo22', 'new arm', 'broken arm and achu', 'arm is broken');

insert into healing_histories(id, num_of_record, login, name_of_medicine, name_of_weakness, name_of_syndrom) values (3, 2,
'expo22', 'pika', 'broken arm and achu', 'Achu');

insert into healing_histories(id, num_of_record, login, name_of_medicine, name_of_weakness, name_of_syndrom) values (4, 1,
'expo33', 'pika', 'broken leg', 'Not planned');