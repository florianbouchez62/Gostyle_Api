from django.test import TestCase, Client
from rest_framework import status
from promotion.models import Promotion

client = Client()

class PromotionCreateObjectsTest(TestCase):

    def setUp(self):
        Promotion.objects.create(code='test1', description='desc', start_date='2025-12-01', end_date='2025-12-30', percentage='50', image='/Images/Fixtures/sweat_nike.jpg', active=True)
        Promotion.objects.create(code='test_default_notactive', description='desc', start_date='2025-12-01', end_date='2025-12-30', percentage='50', image='/Images/Fixtures/sweat_nike.jpg')
        Promotion.objects.create(code='test_not_active', description='desc', start_date='2025-12-01', end_date='2025-12-30', percentage='50', image='/Images/Fixtures/sweat_nike.jpg', active=False)
        Promotion.objects.create(code='test_no_percentage', description='desc', start_date='2025-12-01', end_date='2025-12-30', image='/Images/Fixtures/sweat_nike.jpg', active=True)

    def test_everything_is_created(self):
        nbItems = Promotion.objects.all().count()
        self.assertEqual(nbItems, 4)

    def test_number_of_active_objects(self):
        nbActiveItems = Promotion.objects.filter(active=True).count()
        self.assertEqual(nbActiveItems, 3)

    def test_number_of_not_active_objects(self):
        nbNotActiveObjects = Promotion.objects.filter(active=False).count()
        self.assertEqual(nbNotActiveObjects, 1)

    def test_object_default_percentage(self):
        promotionObject = Promotion.objects.get(code='test_no_percentage')
        self.assertEqual(promotionObject.get_promotion_percentage(), 0.0)

    def test_object_default_active(self):
        promotionObject = Promotion.objects.get(code='test_default_notactive')
        self.assertEqual(promotionObject.get_promotion_active(), False)
