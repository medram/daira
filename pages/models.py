from django.db import models
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField

# from filer.fields.image import FilerImageField
# from filer.fields.file import FilerFileField


class Page(models.Model):
	title 		= models.CharField(max_length=256)
	slug 		= models.SlugField(max_length=256, unique=True)
	# body		= RichTextUploadingField(null=True, blank=True)
	body		= RichTextField(null=True, blank=True)
	published 	= models.BooleanField(default=False)
	seo_keywords = models.CharField(max_length=512, default=None, blank=True, null=True, help_text='eg: keyword1, keyword2, keyword3 ...')
	seo_description = models.TextField(max_length=512, default=None, blank=True, null=True, help_text='Small description about this page.')
	created 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class Menu(models.Model):
	name = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.name


class MenuItem(models.Model):
	class Types(models.IntegerChoices):
		LINK = (1, 'link')
		PAGE = (2, 'page')
		#COLLECTION = (3, 'collection')

	class Meta:
		ordering = ('order',)

	class Visibility(models.IntegerChoices):
		ALL = (1, 'all')
		ONLY_GUEST = (2, 'only guest')
		ONLY_LOGGED_IN = (3, 'only logged in')
		ONLY_LOGGED_IN_ADMIN = (4, 'only logged in admin')

	name = models.CharField(max_length=30)
	type = models.IntegerField(choices=Types.choices, default=Types.LINK)
	path = models.CharField(max_length=128, null=True, blank=True)
	page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, blank=True)
	visibility = models.IntegerField(choices=Visibility.choices, default=Visibility.ALL)
	css_class = models.CharField(max_length=128, null=True, blank=True)
	order = models.IntegerField()

	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.name