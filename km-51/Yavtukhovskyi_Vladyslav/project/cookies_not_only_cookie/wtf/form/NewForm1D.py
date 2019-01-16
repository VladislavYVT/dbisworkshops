from flask_wtf import Form
from wtforms import StringField,   SubmitField,  PasswordField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import DateField


class Cr1D(Form):

   data_field = StringField("Name of entity : ",[
                                    validators.DataRequired("Please enter name of instance you want to create."),
                                    validators.Length(1, 20, "Name should be from 1 to 20 symbols")
                                 ])


   submit = SubmitField("Submit")


class Cr2D(Form):

   data1_field = StringField("Name of first entity in list: ",[
                                    validators.DataRequired("Please enter name of instance you want to create."),
                                    validators.Length(1, 20, "Name should be from 1 to 20 symbols")
                                 ])
   data2_field = StringField("Name of second entity in list: ",[
                                    validators.DataRequired("Please enter name of instance you want to create."),
                                    validators.Length(1, 20, "Name should be from 1 to 20 symbols")
                                 ])


   submit = SubmitField("Submit")


class DateB(Form):

   data_field = DateField("Date of birth: ", [validators.data_required("Please, enter you date of birth in format yyyy-mm-dd")] )
   submit = SubmitField("Submit")

class HistoryForm(Form):
   weakness_field = StringField("Name_of_weakness: ",[
                                    validators.DataRequired("Please enter name of instance you want to create."),
                                    validators.Length(1, 20, "Name should be from 1 to 20 symbols")
                                 ])
   medicine_field = StringField("Name_of_medicine: ",[
                                    validators.DataRequired("Please enter name of instance you want to create."),
                                    validators.Length(1, 20, "Name should be from 1 to 20 symbols")
                                 ])
   syndrom_field = StringField("Name_of_syndrom ",[
                                    validators.DataRequired("Please enter name of instance you want to create."),
                                    validators.Length(1, 20, "Name should be from 1 to 20 symbols")
                                 ])
   date_diagnosis = DateField("Date of diagnosis: ",
                          [validators.data_required("Please, enter you date of birth in format yyyy-mm-dd")])
   date_begin = DateField("Date of begin: ",
                          [validators.data_required("Please, enter you date of birth in format yyyy-mm-dd")])
   date_end = DateField("Date of end: ",
                          [validators.data_required("Please, enter you date of birth in format yyyy-mm-dd")])
   submit = SubmitField("Submit")


class upd_test(Form):
    data_new_field = StringField("Old_name_of_entity: ", [
        validators.DataRequired("Please enter name of instance you want to create."),
        validators.Length(1, 20, "Name should be from 1 to 20 symbols")
    ])
    data_old_field = StringField("New_name_of_entity: ", [
        validators.DataRequired("Please enter name of instance you want to create."),
        validators.Length(1, 20, "Name should be from 1 to 20 symbols")
    ])

    submit = SubmitField("Submit")
