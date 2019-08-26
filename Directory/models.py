# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class DetailsDatatable(models.Model):
#     username = models.CharField(db_column='Username', max_length=15)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=25)  # Field name made lowercase.
#     link = models.ForeignKey('DetailsDetails', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'Details_datatable'


# class DetailsDetails(models.Model):
#     fname = models.CharField(db_column='Fname', max_length=100)  # Field name made lowercase.
#     lname = models.CharField(db_column='Lname', max_length=100)  # Field name made lowercase.
#     mobile_no = models.CharField(db_column='Mobile_no', max_length=12)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
#     address = models.CharField(db_column='Address', max_length=500)  # Field name made lowercase.
#     city = models.CharField(db_column='City', max_length=25)  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=20)  # Field name made lowercase.
#     highestqualification = models.CharField(db_column='HighestQualification', max_length=25)  # Field name made lowercase.
#     pincode = models.IntegerField(db_column='PinCode')  # Field name made lowercase.
#     school = models.CharField(db_column='School', max_length=50)  # Field name made lowercase.
#     state = models.CharField(db_column='State', max_length=25)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Details_details'


# class PlayAlbum(models.Model):
#     artist = models.CharField(max_length=250)
#     album_title = models.CharField(max_length=500)
#     genre = models.CharField(max_length=100)
#     album_logo = models.CharField(max_length=1000)

#     class Meta:
#         managed = False
#         db_table = 'Play_album'


# class SelectBran(models.Model):
#     branch = models.CharField(max_length=100)
#     linka = models.ForeignKey('SelectCou', models.DO_NOTHING, db_column='linkA_id')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Select_bran'


# class SelectCou(models.Model):
#     course = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'Select_cou'


# class SelectSec(models.Model):
#     section = models.CharField(max_length=100)
#     linkc = models.ForeignKey('SelectSemes', models.DO_NOTHING, db_column='linkC_id')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Select_sec'


# class SelectSemes(models.Model):
#     semester = models.CharField(max_length=100)
#     linkb = models.ForeignKey(SelectBran, models.DO_NOTHING, db_column='linkB_id')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Select_semes'


# class TestSudo(models.Model):
#     fname = models.CharField(db_column='Fname', max_length=100)  # Field name made lowercase.
#     fa_name = models.CharField(db_column='Fa_Name', max_length=100)  # Field name made lowercase.
#     mobile_no = models.CharField(db_column='Mobile_no', max_length=100)  # Field name made lowercase.
#     fa_mobile_no = models.CharField(db_column='Fa_Mobile_no', max_length=100)  # Field name made lowercase.
#     email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
#     gender = models.CharField(db_column='Gender', max_length=20)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Test_sudo'


# class TestUser(models.Model):
#     email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.
#     link = models.ForeignKey(TestSudo, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'Test_user'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'

class StudentDropdown(models.Model):
    sno = models.AutoField(db_column='Sno', primary_key=True)  # Field name made lowercase.
    pid = models.IntegerField(db_column='Pid', blank=True, null=True)  # Field name made lowercase.
    field = models.CharField(db_column='Field', max_length=500, blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=500, blank=True, null=True)  # Field name made lowercase.
    is_edit = models.IntegerField(db_column='Is_Edit')  # Field name made lowercase.
    is_delete = models.IntegerField(db_column='Is_Delete')  # Field name made lowercase.
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Student_Dropdown'

class EmployeeDropdown(models.Model):
    sno = models.AutoField(db_column='Sno', primary_key=True)  # Field name made lowercase.
    pid = models.IntegerField(db_column='Pid', blank=True, null=True)  # Field name made lowercase.
    field = models.CharField(db_column='Field', max_length=500, blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=500, blank=True, null=True)  # Field name made lowercase.
    is_delete = models.IntegerField(db_column='Is_Delete')  # Field name made lowercase.
    is_edit = models.IntegerField(db_column='Is_Edit')  # Field name made lowercase.
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'employee_dropdown'


class Sections(models.Model):
    section_id = models.AutoField(db_column='Section_id', primary_key=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=45)  # Field name made lowercase.
    dept_detail = models.IntegerField(db_column='Dept_detail', blank=True, null=True)  # Field name made lowercase.
    sem_id = models.IntegerField(db_column='Sem_id')  # Field name made lowercase.
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sections'


class SemTiming(models.Model):
    uid = models.IntegerField(db_column='Uid', primary_key=True)  # Field name made lowercase.
    session = models.CharField(max_length=15, blank=True, null=True)
    sem_type = models.CharField(max_length=20, blank=True, null=True)
    sem_end = models.DateField(blank=True, null=True)
    session_name = models.CharField(max_length=25)
    sem_start = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sem_timing'




class StudentSemester(models.Model):
    sem_id = models.AutoField(db_column='Sem_Id', primary_key=True)  # Field name made lowercase.
    sem = models.IntegerField(db_column='Sem')  # Field name made lowercase.
    dept = models.IntegerField(db_column='Dept')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student_semester'


class Studentsession1920O(models.Model):
    uniq_id = models.IntegerField(db_column='Uniq_Id', primary_key=True)  # Field name made lowercase.
    mob = models.BigIntegerField(db_column='Mob', blank=True, null=True)  # Field name made lowercase.
    fee_status = models.CharField(db_column='Fee_Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    class_roll_no = models.IntegerField(db_column='Class_Roll_No', blank=True, null=True)  # Field name made lowercase.
    registration_status = models.IntegerField(db_column='Registration_Status', blank=True, null=True)  # Field name made lowercase.
    acc_reg = models.IntegerField(db_column='Acc_Reg', blank=True, null=True)  # Field name made lowercase.
    att_start_date = models.DateField(blank=True, null=True)
    reg_form_status = models.CharField(max_length=10)
    reg_date_time = models.DateTimeField(blank=True, null=True)
    section_id = models.IntegerField(db_column='Section_id', blank=True, null=True)  # Field name made lowercase.
    sem_id = models.IntegerField(db_column='Sem_id', blank=True, null=True)  # Field name made lowercase.
    session = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'studentSession_1920o'


class StudentCourseDetail(models.Model):
    course_duration = models.IntegerField(db_column='Course_duration')  # Field name made lowercase.
    course_id = models.ForeignKey('StudentDropdown' , models.DO_NOTHING,  db_column='Course_id', blank=True, null=True)  # Field name made lowercase.
    course_type = models.IntegerField(db_column='Course_type', blank=True, null=True)  # Field name made lowercase.
    dept = models.ForeignKey('EmployeeDropdown', models.DO_NOTHING, db_column='Dept_id', blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField()
    lateral_capacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Student_course_detail'


class StudentPrimdetail(models.Model):
    name = models.CharField(db_column='Name', max_length=500)  # Field name made lowercase.
    batch_from = models.IntegerField(db_column='Batch_from')  # Field name made lowercase.
    batch_to = models.IntegerField(db_column='Batch_to')  # Field name made lowercase.
    exam_roll_no = models.CharField(db_column='Exam_Roll_No', max_length=500)  # Field name made lowercase.
    general_rank = models.IntegerField(db_column='General_Rank', blank=True, null=True)  # Field name made lowercase.
    category_rank = models.IntegerField(db_column='Category_Rank', blank=True, null=True)  # Field name made lowercase.
    gen_rank = models.IntegerField(db_column='Gen_Rank', blank=True, null=True)  # Field name made lowercase.
    uni_roll_no = models.CharField(db_column='Uni_Roll_No', max_length=15, blank=True, null=True)  # Field name made lowercase.
    join_year = models.IntegerField(db_column='Join_Year')  # Field name made lowercase.
    email_id = models.CharField(db_column='Email_id', max_length=500, blank=True, null=True)  # Field name made lowercase.
    date_of_add = models.DateField(db_column='Date_Of_Add')  # Field name made lowercase.
    uniq_id = models.ForeignKey('Studentsession1920O',models.DO_NOTHING, db_column='Uniq_Id', primary_key=True)  # Field name made lowercase.
    form_fill_status = models.CharField(db_column='Form_Fill_Status', max_length=2)  # Field name made lowercase.
    fee_waiver = models.CharField(db_column='Fee_Waiver', max_length=41)  # Field name made lowercase.
    remark = models.CharField(max_length=500, blank=True, null=True)
    admission_category = models.IntegerField(db_column='Admission_category', blank=True, null=True)  # Field name made lowercase.
    admission_through = models.IntegerField(db_column='Admission_through', blank=True, null=True)  # Field name made lowercase.
    admission_type = models.IntegerField(db_column='Admission_type', blank=True, null=True)  # Field name made lowercase.
    dept_detail = models.ForeignKey('StudentCourseDetail',models.DO_NOTHING,db_column='Dept_detail', blank=True, null=True)  # Field name made lowercase.
    exam_type = models.IntegerField(db_column='Exam_type', blank=True, null=True)  # Field name made lowercase.
    lib_id = models.CharField(db_column='Lib_id', max_length=150, blank=True, null=True)  # Field name made lowercase.
    stu_type = models.IntegerField(db_column='Stu_Type', blank=True, null=True)  # Field name made lowercase.
    admission_status = models.IntegerField(blank=True, null=True)
    caste = models.IntegerField(db_column='Caste', blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    old_uniq_id = models.CharField(max_length=50)
    remark_detail = models.CharField(max_length=500, blank=True, null=True)
    time_stamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Student_primdetail'



