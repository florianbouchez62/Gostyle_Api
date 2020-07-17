from django.contrib.auth.models import User, Group, Permission
from django.contrib.sessions.models import Session
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Promotion
import sys
import logging
import os


groups = {
    'Admins': {
        'permissions': ['view', 'add', 'delete', 'change'],
        'models': ['User', 'Permission', 'Session', 'Group', 'Promotion'],
        'users': ['Sabrinator', 'Fronque'],
    },
    'Gestionnaires': {
        'permissions': ['view', 'add', 'delete', 'change'],
        'models': ['Promotion'],
        'users': ['Maurice', 'Vanessa'],
    },
    'Users': {
        'permissions': ['view'],
        'models': ['Promotion'],
        'users': ['Maxime', 'Mohamed']
    },
    'Applications': {
        'permissions': ['view'],
        'models': ['Promotion'],
        'users': ['Application']
    }, 
}


@receiver(post_save, sender=Promotion)
def generate_qrcode(sender, instance, created, **kwargs) -> None:
    if created and 'test' not in sys.argv:
        instance.generate_qrcode()


def populate_models(sender, **kwargs):
    for group in groups:
        new_group, created = Group.objects.get_or_create(name=group)
        if created:
            for model in groups[group]['models']:
                for permission in groups[group]['permissions']:
                    model_add_perm = create_permission(permission, model)
                    new_group.permissions.add(model_add_perm)
            for user in groups[group]['users']:
                if group == "Admins":
                    name_user = create_admin(user)
                else:
                    name_user = create_user(user)
                token, token_created = Token.objects.get_or_create(user=name_user)
                new_group.user_set.add(name_user)
            logging.warning("{} groupp is created !".format(group))
        else:
            logging.warning("Groups {} already created !".format(group))


def create_permission(permission, model):
    name_permission = 'Can {} {}'.format(permission, model)

    try:
        model_add_perm = Permission.objects.get(name=name_permission)
    except Permission.DoesNotExist:
        logging.warning("Permission not found with name '{}'".format(name_permission))

    return model_add_perm


def create_user(user):
    name_user = User.objects.create_user( 
        username=user,
        email='{}@gostyle.com'.format(user),
        password=user,
        is_staff=True
    )
    return name_user


def create_admin(user):
    name_admin = User.objects.create_superuser( 
        username=user,
        email='{}@gostyle.com'.format(user),
        password=user,
        is_staff=True
    )
    return name_admin
