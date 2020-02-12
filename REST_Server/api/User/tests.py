from django.test import TestCase, Client
from rest_framework import status
from User.models import Promotion
from User.serializers import PromotionSerializers

client = Client()

class PromotionCreateObjectsTest(TestCase):
    
    def setUp(self):
        Promotion.objects.create(libelle='Test1', description='')
        Promotion.objects.create(libelle='', description='')

    def test_promotion_get_libelle(self):
        promotion_test1 = Promotion.objects.get(libelle='Test1')
        self.assertEqual(promotion_test1.get_promotion_libelle(), "Test1")
    
    def test_promotion_empty_libelle(self):
        promotion_emptyLibelle = Promotion.objects.get(libelle='')
        self.assertEqual(promotion_emptyLibelle.get_promotion_libelle(), "")


class GetAllPromotionsTest(TestCase):

    def setUp(self):
        Promotion.objects.create(libelle='test1', description='')
        Promotion.objects.create(libelle='test2', description='')

    def test_get_all_promotions(self):
        response = client.get('/promotions/')
        promotions = Promotion.objects.all()
        serializer = PromotionSerializers(promotions, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSinglePromotionTest(TestCase):

    def setUp(self):
        self.test1 = Promotion.objects.create(libelle='test1', description='')
        self.test2 = Promotion.objects.create(libelle='test2', description='')
        self.nb_objects = Promotion.objects.all().count() + 2
    
    def test_get_valid_single_promotion(self):
        response = client.get('/promotions/{}/'.format(self.test1.pk))
        promotion = Promotion.objects.get(pk=self.test1.pk)
        serializer = PromotionSerializers(promotion)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_promotion(self):
        response = client.get('/promotions/{}/'.format(self.nb_objects+1))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)