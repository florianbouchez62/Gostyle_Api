from django.test import TestCase, Client
from rest_framework import status
from User.models import Promotion
from User.serializers import PromotionSerializers

client = Client()


class PromotionCreateObjectsTest(TestCase):
    
    def setUp(self):
        Promotion.objects.create_promotion(libelle='test1Active', description='desc', active=True)
        Promotion.objects.create_promotion(libelle='test2Active', description='desc', active=True)
        Promotion.objects.create_promotion(libelle='testNotActive', description='desc', active=False)
        Promotion.objects.create_promotion(libelle='testDefaultActive', description='desc')
    
    def test_everything_is_created(self):
        nbItems = Promotion.objects.all().count()
        self.assertEqual(nbItems, 4)
    
    def test_number_of_active_objects(self):
        nbActiveItems = Promotion.objects.filter(active=True).count()
        self.assertEqual(nbActiveItems, 2)
    
    def test_number_of_not_active_objects(self):
        nbNotActiveObjects = Promotion.objects.filter(active=False).count()
        self.assertEqual(nbNotActiveObjects, 2)

    def test_object_default_pourcentage(self):
        promotionObject = Promotion.objects.get(libelle='test1Active')
        self.assertEqual(promotionObject.get_pourcentage(), 0.0)
    
    def test_object_default_active(self):
        promotionObject = Promotion.objects.get(libelle='testDefaultActive')
        self.assertEqual(promotionObject.get_active(), False)


class GetPromotionObjectsTest(TestCase):

    def setUp(self):
        self.promotionActive1 = Promotion.objects.create_promotion(libelle='test1Active', description='desc', active=True)
        self.promotionActive2 = Promotion.objects.create_promotion(libelle='test2Active', description='desc', active=True)
        self.promotionNotActive = Promotion.objects.create_promotion(libelle='testNotActive', description='desc', active=False)
        self.promotionDefaultActive = Promotion.objects.create_promotion(libelle='testDefaultActive', description='desc')
        self.nb_objects = Promotion.objects.all().count()

    def test_get_all_promotions_statuscode_200(self):
        response = client.get('/promotions/')
        promotions = Promotion.objects.filter(active=True)
        serializer = PromotionSerializers(promotions, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_single_promotion_statuscode_200(self):
        response = client.get('/promotions/{}/'.format(self.promotionActive1.pk))
        promotion = Promotion.objects.get(libelle='test1Active')
        serializer = PromotionSerializers(promotion, many=False)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_promotions_objects(self):
        response = client.get('/promotions/')
        promotions = Promotion.objects.filter(active=True)
        serializer = PromotionSerializers(promotions, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_get_valid_single_promotion(self):
        response = client.get('/promotions/{}/'.format(self.promotionActive1.pk ))
        promotion = Promotion.objects.get(libelle='test1Active')
        serializer = PromotionSerializers(promotion)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_promotion(self):
        response = client.get('/promotions/{}/'.format(self.nb_objects+1))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
