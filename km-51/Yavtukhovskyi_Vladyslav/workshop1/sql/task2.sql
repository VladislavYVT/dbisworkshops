--Second task

DECLARE
med_to_delete varchar(20);
BEGIN
med_to_delete := 'pika';
UPDATE HEALING_HISTORIES SET name_of_medicine_fk = NULL
where name_of_medicine_fk = med_to_delete;
DELETE FROM MEDICINE_IS_FOR_WEAKNESS WHERE name_of_medicine_fk = med_to_delete;
DELETE FROM MEDICINE WHERE name_of_medicine = med_to_delete;
END;


