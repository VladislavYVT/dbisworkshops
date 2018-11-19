set serveroutput on
DECLARE
res INT;
resres user_pack.tblUserSet;
checks userss.login%TYPE;
BEGIN
DBMS_OUTPUT.enable;
res := user_pack.loginin('expo1', '4321');
dbms_output.put_line('logs');
dbms_output.put_line(res);
res := user_pack.upd_user_name('expo1', 'Ya Ya Yaa');
dbms_output.put_line('upd_u_name');
dbms_output.put_line(res);
res := user_pack.new_user('expo123', '122344');
res := user_pack.upd_user_name('expo12', 'Ya Ya Ya42');
dbms_output.put_line(res);

END;

SELECT * FROM TABLE(user_pack.user_list('Ya Ya Yaa'));

