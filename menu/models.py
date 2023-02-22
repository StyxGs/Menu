from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название меню')

    class Meta:
        verbose_name = 'main menu'
        verbose_name_plural = 'menu'

    def __str__(self):
        return self.name


class CategoriesMenu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL')
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True,
                               db_index=True, verbose_name='Родительская категория', related_name="children")
    menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
