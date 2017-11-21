from django.db import models

SEX = (
    ('M', 'Male'),
    ('F', 'Female'),
)

CRIME = (
    ('M', 'Murder'),
)

CASE_STATUS = (
    ('AA', 'Adult Arrest'),
    ('JA', 'Juvenile Arrest'),
    ('AO', 'Adult Other'),
    ('JO', 'Juvenile Other'),
    ('IC', 'Investigation Continued'),
)

ETHNICITIES = (
    # TODO: What do 'K' and 'S' mean (from spreadsheet)?
    ('W', 'White'),
    ('H', 'Hispanic'),
    ('B', 'Black or African American'),
    ('A', 'Asian'),
    ('AI', 'American Indian or Alaska Native'),
    ('ME', 'Middle Eastern'),
    ('PI', 'Pacific Islander'),
    ('O', 'Other'),
)

class District(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    bureau = models.CharField(
        max_length = 32,
        null = False,
    )
    division = models.CharField(
        max_length = 32,
        null = False,
    )
    reporting_district = models.CharField(
        max_length = 32,
        null = False,
    )

class Case(models.Model):
    dr_nbr = models.CharField(
        primary_key = True,
        max_length = 32,
    )
    date_fully_reviewed = models.DateTimeField(
        null = True,
        blank = True
    )
    motive = models.CharField(
        max_length = 32,
        null = False,
    )
    adjudication = models.CharField(
        max_length = 32,
        null = True,
        blank = True
    )
    evidence_destroyed = models.BooleanField(
        null = False,
        default = False,
    )
    status = models.CharField(
        max_length = 2,
        choices =  CASE_STATUS,
        null = True,
        blank = True
    )
    status_date = models.DateTimeField(
        null = True,
        blank = True
    )
    # Should this be part of Event?
    court_case_number = models.CharField(
        max_length = 32,
        null = True,
        blank = True
    )
    notes = models.TextField(
        null = True,
        blank = True
    )

    # TODO: What type should solvability_factor be?
    # solvability_factor = models.

    related_cases = models.ManyToManyField(
        'self',
        null = True,
        blank = True
    )
    district = models.ForeignKey(
        District,
        null = False,
    )
class Event(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    date_occurred = models.DateTimeField(
        null = False,
    )
    date_reported = models.DateTimeField(
        null = False,
    )
    address = models.CharField(
        max_length = 50,
        null = False,
    )
    weapon = models.CharField(
        max_length = 32,
        null = True,
        blank = True
    )
    crime_committed = models.CharField(
        max_length = 1,
        choices = CRIME,
        default = 'M',
        null = False,
    )
    coroner_case_number = models.CharField(
        max_length = 32,
        null = True,
        blank = True
    )
    case = models.ForeignKey(
        Case,
        null = False,
    )

class Person(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    first_name = models.CharField(
        max_length = 32,
        null = True,
        blank = True
    )
    last_name = models.CharField(
        max_length = 32,
        null = True,
        blank = True
    )
    age = models.IntegerField(
        null = True,
        blank = True
    )
    sex = models.CharField(
        max_length = 32,
        choices = SEX,
        null = True,
        blank = True
    )
    ethnicity = models.CharField(
        max_length  = 1,
        choices = ETHNICITIES,
        # TODO: Add ETHNICITIES choices
        null = True,
        blank = True
    )
    description = models.CharField(
        max_length = 64,
        null = True,
        blank = True
    )
    case = models.ForeignKey(
        Case,
        null = False,
    )

class Binder(models.Model):
    # TODO: Expand this entity to track more binder info
    master_dr = models.CharField(
        primary_key = True,
        max_length = 16,
    )
    check_out_date = models.DateTimeField(
        null = True,
        blank = True
    )

class History(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    date_edited = models.DateTimeField(
        null = False,
    )
    edited_by = models.CharField(
        max_length = 32,
        null = False,
    )
    # TODO: Add traking for what was changed
    case = models.ForeignKey(
        Case,
        null = False,
    )
