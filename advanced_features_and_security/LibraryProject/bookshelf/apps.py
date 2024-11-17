from django.apps import AppConfig


class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType
        from .models import Book

        # Create groups
        editors_group, created = Group.objects.get_or_create(name='Editors')
        viewers_group, created = Group.objects.get_or_create(name='Viewers')
        admins_group, created = Group.objects.get_or_create(name='Admins')

        # Assign permissions
        content_type = ContentType.objects.get_for_model(Book)
        permissions = Permission.objects.filter(content_type=content_type)

        editors_group.permissions.add(
            permissions.get(codename='can_create'),
            permissions.get(codename='can_edit')
        )
        viewers_group.permissions.add(
            permissions.get(codename='can_view')
        )
        admins_group.permissions.add(*permissions)
