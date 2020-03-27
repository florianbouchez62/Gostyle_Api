from django.test import TestCase, Client
from rest_framework import status
from promotion.models import Promotion
from promotion.serializers import PromotionSerializers

client = Client()


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


class GetPromotionObjectsTest(TestCase):

    def setUp(self):
        self.promotionActive1 = Promotion.objects.create(name='test1Active', description='desc', active=True)
        self.promotionActive2 = Promotion.objects.create(name='test2Active', description='desc', active=True)
        self.promotionNotActive = Promotion.objects.create(name='testNotActive', description='desc', active=False)
        self.promotionDefaultActive = Promotion.objects.create(name='testDefaultActive', description='desc')
        self.nb_objects = Promotion.objects.all().count()

    def test_get_all_promotions_statuscode_200(self):
        response = client.get('/promotions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_single_promotion_statuscode_200(self):
        response = client.get('/promotions/{}/'.format(self.promotionActive1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_promotion(self):
        response = client.get('/promotions/-1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
