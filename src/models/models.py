from django.db import models

# Create your models here.
"""
class Role(models.Model):

    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125,null=True,blank=True)

    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True)


    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')
        ordering = ['name','created']


    def __str__(self):
        return self.name


class Department(models.Model):

    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125,null=True,blank=True)

    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True)


    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
        ordering = ['name','created']
    
    def __str__(self):
        return self.name
"""


class employeeRegistratoin(models.Model):

    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=25)
    password=models.CharField(max_length=10)
    phone=models.CharField(max_length=12)
    
    def __str__(self) -> str:
        return self.first_name

"""
attendance_choices = (
    ('absent', 'Absent'),
    ('present', 'Present'),
    ('first_half','First_Half'),
    ('second_half','Second_Half')
)

department =  models.ForeignKey(Department,verbose_name =_('Department'),on_delete=models.SET_NULL,null=True,default=None)
role =  models.ForeignKey(Role,verbose_name =_('Role'),on_delete=models.SET_NULL,null=True,default=None)
startdate = models.DateField(_('Employement Date'),help_text='date of employement',blank=False,null=True)
attendance = models.CharField(max_length=8, choices=attendance_choices, blank=True)
employeeid = models.CharField(_('Employee ID Number'),max_length=10,null=True,blank=True)
dateissued = models.DateField(_('Date Issued'),help_text='date staff id was issued',blank=False,null=True)

created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True,null=True)
updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True,null=True)
"""