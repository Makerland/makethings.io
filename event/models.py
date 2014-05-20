# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth import models as auth_models
from positions import PositionField


class UserManager(auth_models.BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_superuser = user.is_staff = True
        user.save(using=self._db)
        return user


class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    event = models.ForeignKey('Event', null=True, blank=True, related_name='organizers')
    twitter = models.CharField(max_length=50, null=False, blank=True)
    photo = models.ImageField(upload_to='event/organizers/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Organizer'
        verbose_name_plural = 'Organizers'

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)


class Event(models.Model):
    city = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    main_organizer = models.ForeignKey(User, null=True, blank=True, related_name='+')

    def __unicode__(self):
        number = Event.objects.filter(city=self.city, country=self.country).count() + 1
        return u"{0}, {1} #{2}".format(self.city, self.country, number)


class Website(models.Model):
    STATUSES = (
        (0, 'Draft'),
        (1, 'Published'),
        (2, 'Done')
    )

    event = models.ForeignKey(Event, null=False, blank=False)
    url = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateField(null=True, blank=True)
    team = models.ManyToManyField(User, null=True, blank=True, related_name="websites")
    status = models.IntegerField(null=False, blank=False, default=0, choices=STATUSES)

    #About section
    about_title = models.CharField(max_length=255, null=False, blank=False, default="Make Things in ...")
    about_description = models.TextField(null=False, blank=False, default="Welcome to the free, one-day event that will get you excited and teach you everything you want to know about the world of hardware, Internet of Things and Maker Movement.")
    about_button = models.CharField(max_length=255, null=True, blank=True, default="Apply for a pass", help_text="Leave empty to hide button")
    about_url = models.URLField(null=True, blank=True)

    #Location & place section
    location_name = models.CharField(max_length=255, null=True, blank=True, default="Location: TBA")
    location_button = models.CharField(max_length=255, null=True, blank=True, default="Get directions »", help_text="Leave empty to hide button")
    location_url = models.URLField(null=True, blank=True, help_text="Google maps link")

    #Values section
    value_1 = models.CharField(max_length=255, null=True, blank=True, default="<b>Make Things</b> aims to give everyone a chance to start their journey with hardware.", help_text="Leave empty to hide section. HTML allowed.")
    value_2 = models.CharField(max_length=255, null=True, blank=True, default="Come & learn about <b>3D printing, Arduino, Raspberry Pi, drones, robots and DIY</b> in a friendly enviroment.", help_text="Leave empty to hide section. HTML allowed.")
    value_3 = models.CharField(max_length=255, null=True, blank=True, default="Become a Maker! Be a part of <b>global community of Makers</b>. Start making the future.", help_text="Leave empty to hide section. HTML allowed.")

    #Apply section
    apply_title = models.CharField(max_length=255, null=True, blank=True, default="Apply for a ticket!", help_text="Leave empty to hide whole 'Apply' section.")
    apply_description = models.TextField(null=True, blank=True, help_text="HTML allowed", default="Workshops are aimed for people of any age with basic knowledge of working with a computer. Most of the program is run in Polish, but basic reading skills in English are helpful - some materials are available only in English. We will choose a diverse group of people who are truly motivated and curious about learning. Event is free for everyone, we have a limited space for only 70 participants.<br /><br />You'll receive your acceptance letter by 19th June 2014.")
    apply_button = models.CharField(max_length=255, null=True, blank=True, default="Apply", help_text="Leave empty to hide button")
    apply_url = models.URLField(null=True, blank=True)

    #Workshop section
    workshops_title = models.CharField(max_length=255, null=True, blank=True, default="Workshops", help_text="Leave empty to hide whole 'Workshop' section.")

    #How it works
    howitworks_title = models.CharField(max_length=255, null=True, blank=True, default="How it works?", help_text="Leave empty to hide whole 'How it works' section.")
    howitworks_description = models.TextField(null=True, blank=True, help_text="HTML allowed", default="Make Things is all about learning, having fun and meeting new people. We care about people: you're in the center of the event and we will make sure you fell in love with the world of hardware. During the whole day we will have a couple of workshop stations that will be working all the time. It means that you can join a workshop anytime you want and stay for as long as you want. If you want to get a little bit of everything, you can do that. If you want to get a deep dive into one topic, you can do that. No fixed schedule, no boredom: just fun, robots and MAKING THINGS.")

    #Agenda / Sponsors section
    agenda_title = models.CharField(max_length=255, null=False, blank=False, default="Agenda")
    sponsors_title = models.CharField(max_length=255, null=False, blank=False, default="Sponsors")
    sponsors_description = models.CharField(max_length=255, null=True, blank=True, default="We couldn't be here without the amazing support of our sponsors:")

    #Social section
    newsletter_title = models.CharField(max_length=255, null=False, blank=False, default="Stay in touch:")
    newsletter_description = models.TextField(null=True, blank=True, default="If you want to ocasionally receive latest news about Make Things, Makerland or Internet of Things world, subscribe to our newsletter:")
    social_title = models.CharField(max_length=255, null=False, blank=False, default="Follow us on social media:")

    #Organizers section
    organizers_title = models.CharField(max_length=255, null=True, blank=True, default="Make Things in ... is organized by", help_text="Leave empty to hide whole 'Organizers' section.")

    mailchimp_id = models.CharField(max_length=100, null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.name()

    def name(self):
        return u"{0} website".format(self.event)


class WorkshopLeader(models.Model):
    event = models.ForeignKey(Event, related_name='workshop_leaders')
    name = models.CharField(max_length=255, null=False, blank=False)
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='event/organizers/', null=False, blank=False)

    def __unicode__(self):
        return self.name


class Workshop(models.Model):
    website = models.ForeignKey(Website, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True, help_text="HTML allowed")
    icon = models.ImageField(upload_to="event/workshops/", null=True, blank=True, help_text="Square, min. 200x200px.")
    is_public = models.BooleanField(default=True, null=False, blank=False)
    leaders = models.ManyToManyField(WorkshopLeader, null=True, blank=True)

    def __unicode__(self):
        return u"{0} at {1}".format(self.name, self.website.event)


class FAQ(models.Model):
    websites = models.ManyToManyField(Website, null=True, blank=True, related_name='faqs')
    question = models.TextField(null=False, blank=False)
    answer = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"

    def __unicode__(self):
        return u"Q&A #{0}".format(self.id)


class AgendaEntry(models.Model):
    website = models.ForeignKey(Website, null=False, blank=False, related_name='agenda_entries')
    workshop = models.ForeignKey(Workshop, null=True, blank=True, help_text="Use only if agenda item is a workshop. Leave blank otherwise.")
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=True, blank=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    is_highlighted = models.BooleanField(null=False, blank=False)
    is_break = models.BooleanField(null=False, blank=False)

    class Meta:
        ordering = ('website', 'start_time')
        verbose_name_plural = "Agenda entries"

    def __unicode__(self):
        return self.title


class Sponsor(models.Model):
    website = models.ForeignKey(Website, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    logo = models.ImageField(upload_to="event/sponsors/", null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=False, blank=False)
    order = PositionField()

    def __unicode__(self):
        return self.name
