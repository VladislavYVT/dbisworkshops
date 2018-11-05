/*=============================================================*/
/* Table: Medicine                                              */
/*==============================================================*/
create table Medicine 
(
   name_of_medicine     VARCHAR2(20)         not null,
   constraint PK_MEDICINE primary key (name_of_medicine)
);

/*==============================================================*/
/* Table: Medicine_is_for_weakness                              */
/*==============================================================*/
create table Medicine_is_for_weakness 
(
   name_of_medicine_fk  VARCHAR2(20),
   name_of_weakness_fk  VARCHAR2(20),
   constraint PK_MEDICINE_IS_FOR_WEAKNESS primary key (name_of_weakness_fk, name_of_medicine_fk)
);

/*==============================================================*/

/*==============================================================*/
/* Table: Syndromes                                             */
/*==============================================================*/
create table Syndromes 
(
   name_of_syndrom      VARCHAR2(20)         not null,
   constraint PK_SYNDROMES primary key (name_of_syndrom)
);

/*==============================================================*/
/* Table: "Userss"                                                */
/*==============================================================*/
create table "Userss" 
(
   login                VARCHAR2(16)         not null,
   password             VARCHAR2(16)         not null,
   user_name	        VARCHAR2(40),
   date_of_birth        DATE                 not null,
   constraint PK_USER primary key (login)
);

/*==============================================================*/
/* Table: Weakness                                              */
/*==============================================================*/
create table Weakness 
(
   name_of_weakness     VARCHAR2(20)         not null,
   constraint PK_WEAKNESS primary key (name_of_weakness)
);

/*==============================================================*/
/* Table: Weakness_has_syndrom                                  */
/*==============================================================*/
create table Weakness_has_syndrom 
(
   name_of_weakness_fk  VARCHAR2(20),
   name_of_syndmrome_fk VARCHAR2(20),
   constraint PK_WEAKNESS_HAS_SYNDROM primary key (name_of_syndmrome_fk, name_of_weakness_fk)
);


/*==============================================================*/
/* Table: healing_histories                                     */
/*==============================================================*/
create table healing_histories 
(
   id                   INTEGER              not null,
   num_of_record        INTEGER,
   login_fk             VARCHAR2(16)         not null,
   name_of_medicine_fk  VARCHAR2(20),
   name_of_weakness_fk  VARCHAR2(20),
   name_of_syndrom_fk   VARCHAR2(20)         not null,
   date_of_begin        DATE,
   date_of_end          DATE,
   constraint PK_HEALING_HISTORIES primary key (id)
);

/*==============================================================*/

/*==============================================================*/

/*==============================================================*/


alter table Medicine_is_for_weakness
   add constraint FK_MEDICINE_MEDICINE__WEAKNESS foreign key (name_of_weakness_fk)
      references Weakness (name_of_weakness);

alter table Medicine_is_for_weakness
   add constraint FK_MEDICINE_MEDICINE__MEDICINE foreign key (name_of_medicine_fk)
      references Medicine (name_of_medicine);

alter table Weakness_has_syndrom
   add constraint FK_WEAKNESS_WEAKNESS__SYNDROME foreign key (name_of_syndmrome_fk)
      references Syndromes (name_of_syndrom);

alter table Weakness_has_syndrom
   add constraint FK_WEAKNESS_WEAKNESS__WEAKNESS foreign key (name_of_weakness_fk)
      references Weakness (name_of_weakness);

alter table healing_histories
   add constraint FK_HEALING__MEDICINE__MEDICINE foreign key (name_of_medicine_fk)
      references Medicine (name_of_medicine);

alter table healing_histories
   add constraint FK_HEALING__SYNDROMES_SYNDROME foreign key (name_of_syndrom_fk)
      references Syndromes (name_of_syndrom);

alter table healing_histories
   add constraint FK_HEALING__USER_HAS__USER foreign key (login_fk)
      references "Userss" (login);

alter table healing_histories
   add constraint FK_HEALING__WEAKNESS__WEAKNESS foreign key (name_of_weakness_fk)
      references Weakness (name_of_weakness);

CREATE OR REPLACE  TRIGGER NO_HEAL_DELETE
BEFORE DELETE ON HEALING_HISTORIES
FOR EACH ROW
BEGIN
    IF :old.date_of_end - sysdate > 3 THEN 

    raise_application_error(-20001,'Records can not be deleted');

    END IF;
END;

CREATE OR REPLACE TRIGGER NO_MORE_THEN_40
BEFORE INSERT ON HEALING_HISTORIES
FOR EACH ROW
DECLARE
num_exist number;
logi varchar(20);
BEGIN
logi := :new.login_fk;
SELECT COUNT(*) INTO num_exist FROM HEALING_HISTORIES WHERE login_fk = logi;
IF num_exist >= 40 THEN 
    raise_application_error(-20002, 'You can not insert more values to this user');
END IF; 
END;

ALTER TABLE "Userss" 
ADD CONSTRAINT reg_for_login CHECK(REGEXP_LIKE(login, '[A-Za-z0-9]{1,20}'));

ALTER TABLE "Userss" 
ADD CONSTRAINT reg_for_name CHECK(REGEXP_LIKE(user_name, '[A-Za-z\s]{1,20}'));

ALTER TABLE "Userss" 
ADD CONSTRAINT reg_for_birth CHECK(REGEXP_LIKE(date_of_birth, '\d\d.[0-1]\d.[1-2]\d\d\d'));

ALTER TABLE HEALING_HISTORIES 
ADD CONSTRAINT reg_for_begin_heal CHECK(REGEXP_LIKE(date_of_begin, '\d\d.[0-1]\d.[1-2]\d\d\d'));

ALTER TABLE HEALING_HISTORIES 
ADD CONSTRAINT reg_for_end_heal CHECK(REGEXP_LIKE(date_of_end, '\d\d.[0-1]\d.[1-2]\d\d\d'));

ALTER TABLE MEDICINE
ADD CONSTRAINT reg_for_medicine_name CHECK(REGEXP_LIKE(name_of_medicine, '[A-Za-z0-9\s]{1,20}'));

ALTER TABLE WEAKNESS
ADD CONSTRAINT reg_for_weakness_name CHECK(REGEXP_LIKE(name_of_weakness, '[A-Za-z0-9\s]{1,20}'));

ALTER TABLE SYNDROMES
ADD CONSTRAINT reg_for_syndrom_name CHECK(REGEXP_LIKE(name_of_syndrom, '[A-Za-z0-9\s]{1,20}'));


