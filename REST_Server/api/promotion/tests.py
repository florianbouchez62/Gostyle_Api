from django.test import TestCase, Client
from rest_framework import status
from promotion.models import Promotion

client = Client()

"""
class PromotionCreateObjectsTest(TestCase):

    def setUp(self):
        Promotion.objects.create(name='test1Active', description='desc', active=True)
        Promotion.objects.create(name='test2Active', description='desc', active=True)
        Promotion.objects.create(name='testNotActive', description='desc', active=False)
        Promotion.objects.create(name='testDefaultActive', description='desc')

    def test_everything_is_created(self):
        nbItems = Promotion.objects.all().count()
        self.assertEqual(nbItems, 4)

    def test_number_of_active_objects(self):
        nbActiveItems = Promotion.objects.filter(active=True).count()
        self.assertEqual(nbActiveItems, 2)

    def test_number_of_not_active_objects(self):
        nbNotActiveObjects = Promotion.objects.filter(active=False).count()
        self.assertEqual(nbNotActiveObjects, 2)

    def test_object_default_percentage(self):
        promotionObject = Promotion.objects.get(name='test1Active')
        self.assertEqual(promotionObject.get_promotion_percentage(), 0.0)

    def test_object_default_active(self):
        promotionObject = Promotion.objects.get(name='testDefaultActive')
        self.assertEqual(promotionObject.get_promotion_active(), False)
"""