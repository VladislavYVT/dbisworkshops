--/First task
INSERT INTO syndromes values ('NEW syndrom');
INSERT INTO medicine values ('NEW medicine');
DECLARE
IDS INT;
RECS INT;
logs varchar(20);
BEGIN
logs := 'expo12';
SELECT MAX(ID) INTO IDS FROM HEALING_HISTORIES;
SELECT MAX(NUM_OF_RECORD) INTO RECS FROM HEALING_HISTORIES WHERE login_fk = 'expo12';
INSERT INTO healing_histories (id, num_of_record, login_fk, name_of_medicine_fk, name_of_syndrom_fk) values (IDS +1, RECS +1, logs, 'NEW medicine', 'NEW syndrom');
END;

