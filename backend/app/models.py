from django.db import models

# Create your models here.

class VisaApplication(models.Model):
    CASE_NUMBER = models.CharField(max_length=255)
    CASE_STATUS = models.CharField(max_length=255,blank=True, null=True)
    CASE_SUBMITTED = models.DateField(blank=True, null=True)
    DECISION_DATE = models.DateField(blank=True, null=True)
    VISA_CLASS = models.CharField(max_length=255)
    EMPLOYMENT_START_DATE = models.DateField(blank=True, null=True)
    EMPLOYMENT_END_DATE = models.DateField(blank=True, null=True)
    EMPLOYER_NAME = models.CharField(max_length=255,blank=True, null=True)
    EMPLOYER_ADDRESS = models.CharField(max_length=255,blank=True, null=True)
    EMPLOYER_CITY = models.CharField(max_length=255,blank=True, null=True)
    EMPLOYER_STATE = models.CharField(max_length=255,blank=True, null=True)
    EMPLOYER_POSTAL_CODE = models.CharField(max_length=255,blank=True, null=True)
    EMPLOYER_COUNTRY = models.CharField(max_length=255,blank=True, null=True)
    EMPLOYER_PROVINCE = models.CharField(max_length=255,blank=True, null=True)
    EMPLOYER_PHONE = models.CharField(max_length=20,blank=True, null=True)
    EMPLOYER_PHONE_EXT = models.CharField(max_length=100,blank=True, null=True)
    AGENT_ATTORNEY_NAME = models.CharField(max_length=255,blank=True, null=True)
    AGENT_ATTORNEY_CITY = models.CharField(max_length=255,blank=True, null=True)
    AGENT_ATTORNEY_STATE = models.CharField(max_length=255,blank=True, null=True)
    JOB_TITLE = models.CharField(max_length=255,blank=True, null=True)
    SOC_CODE = models.CharField(max_length=255,blank=True, null=True)
    SOC_NAME = models.CharField(max_length=255,blank=True, null=True)
    NAIC_CODE = models.FloatField(blank=True, null=True)
    TOTAL_WORKERS = models.IntegerField(blank=True, null=True)
    FULL_TIME_POSITION = models.BooleanField(blank=True, null=True)
    PREVAILING_WAGE = models.FloatField(default=0.00,null=True)
    PW_UNIT_OF_PAY = models.CharField(max_length=255,default="Year",null=True)
    PW_WAGE_SOURCE = models.CharField(max_length=255,blank=True, null=True)
    PW_SOURCE_YEAR = models.FloatField(blank=True, null=True)
    PW_SOURCE_OTHER = models.CharField(max_length=255,blank=True, null=True)
    WAGE_RATE_OF_PAY_FROM = models.FloatField(blank=True, null=True)
    WAGE_RATE_OF_PAY_TO = models.FloatField(blank=True, null=True)
    WAGE_UNIT_OF_PAY = models.CharField(max_length=255,blank=True, null=True)
    H1B_DEPENDENT = models.CharField(max_length=3,blank=True, null=True)
    WILLFUL_VIOLATOR = models.CharField(max_length=3,blank=True, null=True)
    WORKSITE_CITY = models.CharField(max_length=255,blank=True, null=True)
    WORKSITE_COUNTY = models.CharField(max_length=255,blank=True, null=True)
    WORKSITE_STATE = models.CharField(max_length=255,blank=True, null=True)
    WORKSITE_POSTAL_CODE = models.CharField(max_length=100,blank=True, null=True)
    ORIGINAL_CERT_DATE = models.DateField(blank=True, null=True)