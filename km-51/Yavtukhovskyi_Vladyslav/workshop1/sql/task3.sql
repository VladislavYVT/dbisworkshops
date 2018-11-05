UPDATE medicine set name_of_medicine = 'nepotribni'
where name_of_medicine not in(
select name_of_medicine from medicine
where name_of_medicine in (select name_of_medicine_fk  from healing_histories  UNION select name_of_medicine_fk from medicine_is_for_weakness));

