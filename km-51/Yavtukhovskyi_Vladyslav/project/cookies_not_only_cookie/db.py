
import cx_Oracle
from datetime import datetime


uname = 'Vlod'
password = 'xnjnjnj21a'
dsn = 'localhost:1521/xe'


class User:

    def __init__(self):
        self.__db = cx_Oracle.connect(uname, password, dsn)
        self.__cursor = self.__db.cursor()

    def login_user(self, user_login, user_password):
        print(user_login, user_password)
        res = self.__cursor.callfunc('USER_PACK.loginin', cx_Oracle.NUMBER, [user_login, user_password])
        if res == 1:
            return True
        else:
            return False

    def reg_user(self, user_login, user_password):
            print(user_login, user_password)
            res = self.__cursor.callfunc('USER_PACK.new_user', cx_Oracle.NUMBER, [user_login, user_password])
            if res == 1:
                return False
            else:
                self.__db.commit()
                return True

    def del_user(self, user_login, user_password):
            res = self.__cursor.callfunc('USER_PACK.del_user', cx_Oracle.NUMBER, [user_login, user_password])
            if res == 0:
                self.__db.commit();
                return True;
            else:
                return False;

    def upd_user_pass(self, user_login, user_password, user_new_password):
            res = self.__cursor.callfunc('USER_PACK.upd_user_pass', cx_Oracle.NUMBER, [user_login, user_password, user_new_password])
            if res == 0:
                self.__db.commit();
                return True;
            else:
                return False;

    def upd_user_name(self, user_login, user_name):

            res = self.__cursor.callfunc('USER_PACK.upd_user_name', cx_Oracle.NUMBER, [user_login, user_name])
            if res == 0:
                self.__db.commit();
                return True;
            else:
                return False;

    def upd_user_birth(self, user_login, u_birth):
        try:
            tod = datetime.today()
            if tod < u_birth:
                return False;
            res = self.__cursor.callfunc('USER_PACK.upd_user_birth', cx_Oracle.NUMBER, [user_login, u_birth])
            if res == 0:
                self.__db.commit();
                return True;
            else:
                return False;
        except Exception:
            return False;

    def get_user(self, user_login):
        try:
            querystring = "select * from userss where login = '%s'" % user_login
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result;
        except Exception:
            return None;


    def user_list(self):
        try:
            querystring = "select login, password, user_name, date_of_birth from userss"
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result;
        except Exception:
            return None;

    def new_synd(self, syndrom_name):
        res = self.__cursor.callfunc('synd.new_synd', cx_Oracle.NUMBER, [syndrom_name])
        if res == 0:
            return True;
        else:
            return False;

    def del_synd(self, syndrom_name):
        res = self.__cursor.callfunc('synd.del_synd', cx_Oracle.NUMBER, [syndrom_name])
        if res == 0:
            self.__db.commit()
            return True;
        else:
            return False;

    def list_syndromes(self):
        try:
            querystring = "select * from syndromes"
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result;
        except Exception:
            return None;

    def upd_synd(self, syn, new_syn):
        res = self.__cursor.callfunc('synd.upd_synd', cx_Oracle.NUMBER, [syn, new_syn])
        if res == 0:
            return True;
        else:
            return False;

    def new_med(self, name_of_medicine):
        res = self.__cursor.callfunc('meds.new_med', cx_Oracle.NUMBER, [name_of_medicine])
        if res == 0:
            return True;
        else:
            return False;

    def del_med(self, name_of_medicine):
        res = self.__cursor.callfunc('meds.del_med', cx_Oracle.NUMBER, [name_of_medicine])
        if res == 0:
            return True;
        else:
            return False;

    def upd_med(self, name_of_medicine, new_med):
        res = self.__cursor.callfunc('meds.upd_med', cx_Oracle.NUMBER, [name_of_medicine, new_med])
        if res == 0:
            return True;
        else:
            return False;

    def list_meds(self):
        querystring = "select * from medicine"
        res = self.__cursor.execute(querystring)
        result = self.__cursor.fetchall()
        return result;

    def new_weak(self, name_of_weak):
        res = self.__cursor.callfunc('weaks.new_weak', cx_Oracle.NUMBER, [name_of_weak])
        if res == 0:
            return True;
        else:
            return False;

    def del_weak(self, name_of_weak):
        res = self.__cursor.callfunc('weaks.del_weak', cx_Oracle.NUMBER, [name_of_weak])
        if res == 0:
            return True;
        else:
            return False;

    def upd_weak(self, name_of_weak, new_weak):
        res = self.__cursor.callfunc('weaks.upd_weak', cx_Oracle.NUMBER, [name_of_weak, new_weak])
        if res == 0:
            return True;
        else:
            return False;

    def list_weaks(self):
        try:
            querystring = "select * from weakness"
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result
        except Exception:
            return None;

    def new_syndrom_of_weakness(self, weakness, syndrom):
        res = self.__cursor.callfunc('weak_has_synd.new_record', cx_Oracle.NUMBER, [weakness, syndrom])
        if res == 0:
            return True;
        else:
            return False;

    def del_syndrom_of_weakness(self, weakness, syndrom):
        res = self.__cursor.callfunc('weak_has_synd.del_record', cx_Oracle.NUMBER, [weakness, syndrom])
        if res == 0:
            return True;
        else:
            return False;

    def list_weaks_by_syndrom(self,syndrom):
        try:
            querystring = "select name_of_weakness from weakness_has_syndrom where name_of_syndrom = '%s'" % syndrom
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result;
        except Exception:
            return None;


    def list_syndromes_of_weakness(self,weakness):
        try:
            querystring = "select name_of_syndrom from weakness_has_syndrom where name_of_weakness = '%s'" % weakness
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result;
        except Exception:
            return None;

    def list_weak_with_synd(self):
        try:
            querystring = "select * from weakness_has_syndrom"
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result;
        except Exception:
            return None;

    def new_medicine_for_weakness(self, medicine, weakness):
        res = self.__cursor.callfunc('medicine_is_for_weakness.new_record', cx_Oracle.NUMBER, [medicine, weakness])
        if res == 0:
            return True;
        else:
            return False;

    def del_medicine_for_weakness(self, medicine, weakness):
        res = self.__cursor.callfunc('medicine_is_for_weakness.del_record', cx_Oracle.NUMBER, [medicine, weakness])
        if res == 0:
            return True;
        else:
            return False;


    def list_weaks_by_medicine(self,medicine):
        try:
            querystring = "select name_of_weakness from medicine_is_for_weakness where name_of_medicine = '%s'" % medicine
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result;
        except Exception:
            return None;


    def list_medicine_of_weakness(self,weakness):
        try:
            querystring = "select name_of_medicine from medicine_is_for_weakness where name_of_weakness = '%s'" % weakness
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result;
        except Exception:
            return None;

    def list_medicine_for_weakness(self):
        try:
            querystring = "select * from medicine_is_for_weakness"
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result;
        except Exception:
            return None;

    def new_healing_record(self, logs, weak, med, syn, diag_date, begin_date, end_date):
        tod = datetime.today()
        if ((tod< diag_date) or  (tod< begin_date) or (tod<end_date) or (begin_date>end_date)):
            return False
        res = self.__cursor.callfunc('heal_hist.new_record', cx_Oracle.NUMBER, [logs, weak, med, syn, diag_date, begin_date, end_date])
        if res == 0:
            return True;
        else:
            return False;

    def del_healing_record(self, logs, weak, med, syn, diag_date, begin_date, end_date):
        res = self.__cursor.callfunc('heal_hist.del_record', cx_Oracle.NUMBER, [logs, weak, med, syn, diag_date, begin_date, end_date])
        if res == 0:
            return True;
        else:
            return False;


    def stat_meds_for_weakness(self,weakness):
        try:
            querystring = "select name_of_medicine, count(*) from healing_histories where name_of_weakness = '%s' group by name_of_medicine" % weakness
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result;
        except Exception:
            return None;


    def stat_weaks_for_syndrom(self,syndrom):
        try:
            querystring = "select name_of_weakness, count(*) from healing_histories where name_of_syndrom = '%s' group by name_of_weakness order by count(*) desc" % syndrom
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result;
        except Exception:
            return None;

    def max_medicine_for_weakness(self, weakness):
        try:
            querystring = "select name_of_medicine from (select name_of_medicine, count(*) from healing_histories where name_of_weakness = '%s' group by name_of_medicine order by count(*) desc ) where rownum<=1" % weakness
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result
        except Exception:
            return None

    def user_history(self, logs):
        try:
            querystring = "select name_of_weakness, name_of_medicine, name_of_syndrom, date_of_diagnosis, date_of_begin, date_of_end from healing_histories where healing_histories.login = '%s' order by date_of_diagnosis" % logs
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result;
        except Exception:
            return None;

    def stat_weak_by_date(self, weakness):
        try:
            querystring ="select date_of_begin, count(*) from healing_histories where name_of_weakness = '%s' group by date_of_begin" %weakness
            res = self.__cursor.execute(querystring)
            result = self.__cursor.fetchall()
            return result;
        except Exception:
            return None;

    def upd_diag(self, nm, new_nm):
        res = self.__cursor.callfunc('diag.upd_diag', cx_Oracle.NUMBER, [nm, new_nm])
        if res==0:
            return 0
        else:
            return 1
