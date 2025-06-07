from rest_framework import serializers
from .models import Category, Product, Supplier,Payment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image_url']
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'required': True, 'allow_blank': False},
            'description': {'required': False, 'allow_blank': True},
            'image_url': {'required': False, 'allow_blank': True}
        }
        depth = 1
        # depth = 1 allows nested representation of related objects
        # For example, if Category has a foreign key to another model,
        # it will include that related model's fields in the serialized output.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'cost_price', 'image_url', 'quantity_in_stock', 'category', 'supplier']
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'required': True, 'allow_blank': False},
            'description': {'required': False, 'allow_blank': True},
            'image_url': {'required': False, 'allow_blank': True},
            'price': {'required': True, 'allow_null': False},
            'cost_price': {'required': True, 'allow_null': False},
            'quantity_in_stock': {'required': True, 'allow_null': False},
            'category': {'required': False, 'allow_null': True},
            'supplier': {'required': False, 'allow_null': True}
        }
        depth = 1

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product.supplier.field.related_model
        fields = ['id', 'name', 'contact_info']
        read_only_fields = ['id']
        extra_kwargs = {
            'name': {'required': True, 'allow_blank': False},
            'contact_info': {'required': False, 'allow_blank': True},
            
        }
        depth = 1   

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'payment_method', 'transaction_id', 'date']
        read_only_fields = ['id']
        extra_kwargs = {
            'amount': {'required': True, 'allow_null': False},
            'payment_method': {'required': True, 'allow_blank': False},
            'transaction_id': {'required': True, 'allow_blank': False},
            'date': {'required': True, 'allow_null': False}
        }
        depth = 1            
