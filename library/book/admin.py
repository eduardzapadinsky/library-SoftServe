from django.contrib import admin
from book import models as book_models
from order import models as order_models
from author import models as author_models


@admin.register(author_models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'display_books')


@admin.register(book_models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'display_author')
    fields = ('name', 'description')
    list_filter = ('name', 'id', 'authors__name')

@admin.register(order_models.Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Times', {
            'fields': ('end_at', 'plated_end_at')
        }),
        ('Main', {
                'fields': ('user', 'book')
            }),
    )
    list_display = ('book', 'user', 'plated_end_at')


