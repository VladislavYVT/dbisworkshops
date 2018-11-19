CREATE OR REPLACE PACKAGE USER_PACK IS


    TYPE user_logpas IS RECORD(

    logs userss.login%TYPE,

    pass userss.password%TYPE
);


TYPE userRec IS RECORD(

    logs userss.login%TYPE,

    pass userss.password%TYPE,
    
    u_name userss.user_name%TYPE,

    u_birth userss.date_of_birth%TYPE

);

TYPE tblUserSet IS TABLE OF userRec;

FUNCTION del_user (logs IN userss.login%TYPE, pass IN userss.password%Type)

    RETURN INTEGER;

FUNCTION upd_user_pass (logs IN userss.login%TYPE, old_pass IN userss.password%TYPE, new_pass IN userss.password%TYPE)

    RETURN INTEGER;

FUNCTION upd_user_name (logs IN userss.login%TYPE, u_name IN userss.user_name%TYPE)

    RETURN INTEGER;
    
FUNCTION upd_user_birth (logs IN userss.login%TYPE, u_birth IN userss.date_of_birth%TYPE)

    RETURN INTEGER;
    
FUNCTION new_user (logs IN userss.login%TYPE, pass IN userss.password%TYPE)

    RETURN INTEGER;

FUNCTION get_user (logs IN userss.login%TYPE)

    RETURN userRec;
    
FUNCTION loginin (logs IN userss.login%type, pass IN userss.password%type)

    RETURN INT;

FUNCTION user_list (u_name IN USERSS.user_name%type)

    RETURN tblUserSet
    PIPELINED ;
    
END USER_PACK;



create or replace PACKAGE BODY USER_PACK IS
FUNCTION del_user (logs IN userss.login%TYPE, pass IN userss.password%Type)

    RETURN INTEGER
    IS

    checks user_logpas;
    BEGIN
    SELECT LOGIN, PASSWORD INTO checks FROM USERSS WHERE login = logs;
    IF checks.logs is NULL then return 1; END IF;
    IF checks.pass != pass then return 2; END IF;
    delete from userss where login = logs;
    return 0;

end del_user;

FUNCTION upd_user_pass (logs IN userss.login%TYPE, old_pass IN userss.password%TYPE, new_pass IN userss.password%TYPE)

    RETURN INTEGER
    IS
    checks user_logpas;
    BEGIN
    SELECT LOGIN, PASSWORD INTO checks FROM userss where login=logs;
    IF checks.logs is NULL then return 1; END IF;
    IF new_pass = old_pass then return 2; end if;
    if checks.pass != old_pass then return 2; end if;
    UPDATE USERSS SET password = new_pass WHERE login = logs;
    return 0;
    END upd_user_pass;

FUNCTION upd_user_name (logs IN userss.login%TYPE, u_name IN userss.user_name%TYPE)

    RETURN INTEGER
    IS
    checks userss.login%TYPE;
    BEGIN
    SELECT LOGIN INTO checks FROM userss where login=logs;
    IF checks is NULL then return 1; END IF;
    UPDATE USERSS SET user_name = u_name WHERE login = logs;
    return 0;
    END upd_user_name;

FUNCTION upd_user_birth (logs IN userss.login%TYPE, u_birth IN userss.date_of_birth%TYPE)

    RETURN INTEGER
    IS
    checks userss.login%TYPE;
    BEGIN
    SELECT LOGIN INTO checks FROM userss where login=logs;
    IF checks is NULL then return 1; END IF;
    UPDATE USERSS SET date_of_birth = u_birth WHERE login = logs;
    return 0;
    END upd_user_birth;


FUNCTION new_user (logs IN userss.login%TYPE, pass IN userss.password%TYPE)

    RETURN INTEGER
        IS
    checks userss.login%TYPE;
    BEGIN
    SELECT LOGIN INTO checks FROM userss where login=logs;
    IF checks is NOT NULL then return 1; END IF;

    EXCEPTION 
    WHEN no_data_found THEN
    INSERT INTO USERSS(login, password, date_of_birth) VALUES (logs, pass, sysdate);
    return 0;
    
    END new_user;

FUNCTION get_user (logs IN userss.login%TYPE)

    RETURN userRec
    IS
    res userRec;
    BEGIN
    SELECT LOGIN ,
PASSWORD ,
USER_NAME ,
DATE_OF_BIRTH  INTO res FROM USERSS WHERE login = logs;
return res;
    END get_user;

FUNCTION loginin (logs IN userss.login%type, pass IN userss.password%type)

    RETURN INT
    IS
    checks user_logpas;
    BEGIN
    SELECT LOGIN , PASSWORD   INTO checks FROM USERSS WHERE login = logs;
    IF(checks.logs = logs) AND (checks.pass = pass) THEN return 1; ELSE return  2  ; END IF;
END loginin;

FUNCTION user_list (u_name IN USERSS.user_name%type)

    RETURN tblUserSet

    PIPELINED 
    IS
    CURSOR u_cur IS 
    SELECT LOGIN , PASSWORD , USER_NAME , DATE_OF_BIRTH  FROM  USERSS WHERE user_name = u_name;
    BEGIN 
    FOR curr in u_cur 
    LOOP
        PIPE ROW(curr);
    END LOOP;
    END user_list;


END USER_PACK;

