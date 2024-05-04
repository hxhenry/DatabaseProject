# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class HcyAccount(models.Model):
    ano = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0, db_comment='account number')
    aname = models.CharField(max_length=20, db_comment='account name')
    adoopen = models.DateTimeField(db_comment='date opened')
    a_type = models.CharField(max_length=1, db_comment='account type')
    owner = models.ForeignKey('HcyCustomer', models.DO_NOTHING, db_column='cemail', db_comment='customer email')
    stid = models.ForeignKey('HcyStreet', models.DO_NOTHING, db_column='stid', blank=True, null=True)
    baptno = models.CharField(max_length=10, blank=True, null=True, db_comment='Bank apartment number')

    class Meta:
        managed = False
        db_table = 'hcy_account'

    def __str__(self):
        return self.aname


class HcySavings(models.Model):
    ano = models.OneToOneField('HcyAccount', models.DO_NOTHING, db_column='ano', primary_key=True,
                               db_comment='account number')
    sintrate = models.DecimalField(max_digits=10, decimal_places=2, db_comment='SAVINGS INTEREST RATE')

    class Meta:
        managed = False
        db_table = 'hcy_savings'


class HcyChecking(models.Model):
    ano = models.OneToOneField('HcyAccount', models.DO_NOTHING, db_column='ano', primary_key=True,
                               db_comment='account number')
    csercharge = models.DecimalField(max_digits=10, decimal_places=2, db_comment='MONTHLY ACCOUNT MAINTENANCE FEES')

    class Meta:
        managed = False
        db_table = 'hcy_checking'


class HcyLoan(models.Model):
    ano = models.OneToOneField('HcyAccount', models.DO_NOTHING, db_column='ano', primary_key=True,
                               db_comment='account number')
    lrate = models.DecimalField(max_digits=10, decimal_places=2, db_comment='loan rate')
    lamount = models.DecimalField(max_digits=10, decimal_places=2, db_comment='LOAN AMOUNT')
    lmonths = models.IntegerField(db_comment='LOAN MONTHS')
    lpayments = models.DecimalField(max_digits=10, decimal_places=2)
    l_type = models.CharField(max_length=1, db_comment='LOAN TYPE')

    class Meta:
        managed = False
        db_table = 'hcy_loan'


class HcyHome(models.Model):
    ano = models.OneToOneField('HcyLoan', models.DO_NOTHING, db_column='ano', primary_key=True,
                               db_comment='account number')
    hbuily = models.DateTimeField(db_comment='home built year')
    hinsacc = models.FloatField(unique=True, db_comment='home insurance account number')
    hinsname = models.CharField(max_length=20, db_comment='home insurance name')
    hinyearly = models.DecimalField(max_digits=10, decimal_places=2,
                                    db_comment='home insurance yearly insurance premium')
    stid = models.ForeignKey('HcyStreet', models.DO_NOTHING, db_column='stid', blank=True, null=True)
    haptno = models.CharField(max_length=10, blank=True, null=True, db_comment='House apartment number')

    class Meta:
        managed = False
        db_table = 'hcy_home'


class HcyStudent(models.Model):
    ano = models.OneToOneField('HcyLoan', models.DO_NOTHING, db_column='ano', primary_key=True,
                               db_comment='account number')
    stuid = models.CharField(unique=True, max_length=20, db_comment='student id')
    sgrad = models.FloatField(db_comment='student is grad or undergrad')
    sexpgraddate = models.DateTimeField(db_comment='exptected graduation')
    uniid = models.ForeignKey('HcyUniversity', models.DO_NOTHING, db_column='uniid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hcy_student'


class HcyCustomer(models.Model):
    cusfname = models.CharField(max_length=20, db_comment='customer first name')
    cuslname = models.CharField(max_length=20, db_comment='customer last name')
    cemail = models.CharField(primary_key=True, max_length=20, db_comment='customer email')
    stid = models.ForeignKey('HcyStreet', models.DO_NOTHING, db_column='stid', blank=True, null=True)
    captno = models.CharField(max_length=10, blank=True, null=True, db_comment='customer apartment numbner')

    class Meta:
        managed = False
        db_table = 'hcy_customer'

    def __str__(self):
        return self.cemail


class HcyState(models.Model):
    sid = models.IntegerField(primary_key=True, db_comment='STATE ID')
    sname = models.CharField(max_length=20, db_comment='STATE NAME')

    class Meta:
        managed = False
        db_table = 'hcy_state'


class HcyCity(models.Model):
    cid = models.IntegerField(primary_key=True, db_comment='CITY ID')
    cname = models.CharField(max_length=20, db_comment='CITY NAME')
    sid = models.ForeignKey('HcyState', models.DO_NOTHING, db_column='sid')

    class Meta:
        managed = False
        db_table = 'hcy_city'


class HcyStreet(models.Model):
    stid = models.IntegerField(primary_key=True, db_comment='STREET ID')
    stname = models.CharField(max_length=20, db_comment='STREET NAME')
    cid = models.ForeignKey('HcyCity', models.DO_NOTHING, db_column='cid')
    zipcode = models.ForeignKey('HcyZip', models.DO_NOTHING, db_column='zipcode')

    class Meta:
        managed = False
        db_table = 'hcy_street'


class HcyZip(models.Model):
    zipcode = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0, db_comment='Zipcode')

    class Meta:
        managed = False
        db_table = 'hcy_zip'


class HcyUniversity(models.Model):
    uniid = models.SmallIntegerField(primary_key=True, db_comment='University ID')
    uname = models.CharField(max_length=30, blank=True, null=True, db_comment='University Name')

    class Meta:
        managed = False
        db_table = 'hcy_university'
