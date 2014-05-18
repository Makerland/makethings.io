# -*- encoding: utf-8 -*-
import random
import string
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
import click

from event.models import *

class Command(BaseCommand):
	help = 'Creates new Make Things event'

	def handle(self, *args, **options):

		#Basics
		click.echo("Hello sir or madam! My name is Verynicebot and I'm here to help you create your new Make Things event. So exciting!")
		click.echo("Let's start with some basics.")
		city = click.prompt("What is the name of the city?")
		country = click.prompt("What is the name of the country?")
		date = click.prompt("What is the date of the event? (Format: YYYY-MM-DD)")
		url = click.prompt("What should be the URL of website? makethings.io/xxxx")
		click.echo(u"Ok, got that! Your new event will happen in {0}, {1} on {2}".format(city, country, date))

		#Main organizer
		team = []
		click.echo("Now let's talk about the team. First the main organizer:")
		main_name = click.prompt("First and last name")
		main_email = click.prompt("E-mail address")
		try:
			team.append({'first_name': main_name.split(' ')[0], 'last_name': main_name.split(' ')[1], 'email': main_email})
		except IndexError:
			team.append({'first_name': main_name, 'last_name': '', 'email': main_email})
		click.echo(u"All right, the main organizer of Make Things in {0} is {1} ({2})".format(city, main_name, main_email))

		#Team
		add_team = click.prompt("Do you want to add additional team members? y/n")
		i = 1
		while add_team != 'n':
			i += 1
			name = click.prompt("First and last name of #{0} member".format(i))
			email = click.prompt("E-mail address of #{0} member".format(i))
			if len(name) > 0:
				try:
					team.append({'first_name': name.split(' ')[0], 'last_name': name.split(' ')[1], 'email': email})
				except IndexError:
					team.append({'first_name': main_name, 'last_name': '', 'email': main_email})
				click.echo(u"All right, the #{0} team member of Make Things in {1} is {2} ({3})".format(i, city, name, email))
			add_team = click.prompt("Do you want to add additional team members? y/n")


		#Save data
		click.echo("OK! That's it. Now I'll create your event.")
		click.echo("Here is an access info for team members:")
		main_organizer = None
		members = []
		for member in team:
			member['password'] = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
			user = User.objects.create(email=member['email'],
										first_name=member['first_name'],
										last_name=member['last_name'],
										is_active=True,
										is_staff=True)
			user.set_password(member['password'])
			user.save()
			user.groups.add(1)

			organizer = Organizer.objects.create(user=user, name=u"{0} {1}".format(member['first_name'], member['last_name']))
			if not main_organizer:
				main_organizer = organizer
			members.append(organizer)
			click.echo(u"{0} - email: {1} password: {2}".format(member['first_name'], member['email'], member['password']))

		event = Event.objects.create(city=city, country=country, main_organizer=main_organizer)
		website = Website.objects.create(event=event, url=url, date=date, status=0, about_title=u"Make Things in {0}".format(city), organizers_title=u"Make Things in {0} is organized by".format(city))
		for member in members:
			website.team.add(member)

		Workshop.objects.create(website=website, name='Sample workshop')
		faq = FAQ.objects.create(question='Sample question?', answer='Sample answer')
		faq.websites.add(website)
		AgendaEntry.objects.create(website=website, start_time='09:00', title='Start!', is_highlighted=True, is_break=False)

		click.echo(u"Website is ready here: http://makethings.io/{0}".format(url))
		click.echo("Congrats on yet another event!")











