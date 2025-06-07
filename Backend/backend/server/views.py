from django.shortcuts import render
from django.http import HttpResponse
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product, Supplier, Payment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import logging

# Configure logging
logger = logging.getLogger(__name__)

def server_status(request):
    return HttpResponse("Server is running smoothly!")

# Create your views here.
## This view returns a list of all categories in JSON format.
## It uses the CategorySerializer to serialize the data.
@api_view(['GET', 'POST'])
def get_categories(request):
    try:
        if request.method == 'GET':
            categories = Category.objects.all()
            if not categories:
                logger.info("No categories found in the database")
                return Response(
                    {"message": "No categories found."},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            serializer = CategorySerializer(categories, many=True)
            logger.info(f"Successfully retrieved {len(categories)} categories")
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        elif request.method == 'POST':
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                category = serializer.save()
                logger.info(f"Successfully created new category: {category.name}")
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            logger.error(f"Failed to create category. Errors: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    except Exception as e:
        logger.error(f"Unexpected error in get_categories: {str(e)}")
        return Response(
            {"message": "An unexpected error occurred"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        logger.warning(f"Category with id {pk} not found")
        return Response(
            {"message": "Category not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    try:
        if request.method == 'GET':
            serializer = CategorySerializer(category)
            logger.info(f"Successfully retrieved category: {category.name}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                updated_category = serializer.save()
                logger.info(f"Successfully updated category: {updated_category.name}")
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(f"Failed to update category. Errors: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
        elif request.method == 'DELETE':
            category_name = category.name
            category.delete()
            logger.info(f"Successfully deleted category: {category_name}")
            return Response(
                {"message": f"Category {category_name} successfully deleted"},
                status=status.HTTP_204_NO_CONTENT
            )
            
    except Exception as e:
        logger.error(f"Unexpected error in category_detail: {str(e)}")
        return Response(
            {"message": "An unexpected error occurred"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

#======================================================Products========================================================

api_view(['GET', 'POST'])
def get_products(request):
    try:
        if request.method == 'GET':
            products = Product.objects.all()
            if not products:
                logger.info("No products found in the database")
                return Response(
                    {"message": "No products found."},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            serializer = ProductSerializer(products, many=True)
            logger.info(f"Successfully retrieved {len(products)} products")
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        elif request.method == 'POST':
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                product = serializer.save()
                logger.info(f"Successfully created new product: {product.name}")
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            logger.error(f"Failed to create product. Errors: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    except Exception as e:
        logger.error(f"Unexpected error in get_products: {str(e)}")
        return Response(
            {"message": "An unexpected error occurred"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        logger.warning(f"Product with id {pk} not found")
        return Response(
            {"message": "Product not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    try:
        if request.method == 'GET':
            serializer = ProductSerializer(product)
            logger.info(f"Successfully retrieved product: {product.name}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                updated_product = serializer.save()
                logger.info(f"Successfully updated product: {updated_product.name}")
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(f"Failed to update product. Errors: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
        elif request.method == 'DELETE':
            product_name = product.name
            product.delete()
            logger.info(f"Successfully deleted product: {product_name}")
            return Response(
                {"message": f"Product {product_name} successfully deleted"},
                status=status.HTTP_204_NO_CONTENT
            )
            
    except Exception as e:
        logger.error(f"Unexpected error in product_detail: {str(e)}")
        return Response(
            {"message": "An unexpected error occurred"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

#=======================================================Supplier========================================================

api_view(['GET', 'POST'])
def get_suppliers(request):
    try:
        if request.method == 'GET':
            suppliers = Supplier.objects.all()
            if not suppliers:
                logger.info("No suppliers found in the database")
                return Response(
                    {"message": "No suppliers found."},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            serializer = SupplierSerializer(suppliers, many=True)
            logger.info(f"Successfully retrieved {len(suppliers)} suppliers")
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        elif request.method == 'POST':
            serializer = SupplierSerializer(data=request.data)
            if serializer.is_valid():
                supplier = serializer.save()
                logger.info(f"Successfully created new supplier: {supplier.name}")
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            logger.error(f"Failed to create supplier. Errors: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    except Exception as e:
        logger.error(f"Unexpected error in get_suppliers: {str(e)}")
        return Response(
            {"message": "An unexpected error occurred"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
@api_view(['GET', 'PUT', 'DELETE'])
def supplier_detail(request, pk):
    try:
        supplier = Supplier.objects.get(pk=pk)
    except Supplier.DoesNotExist:
        logger.warning(f"Supplier with id {pk} not found")
        return Response(
            {"message": "Supplier not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    try:
        if request.method == 'GET':
            serializer = SupplierSerializer(supplier)
            logger.info(f"Successfully retrieved supplier: {supplier.name}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            serializer = SupplierSerializer(supplier, data=request.data)
            if serializer.is_valid():
                updated_supplier = serializer.save()
                logger.info(f"Successfully updated supplier: {updated_supplier.name}")
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(f"Failed to update supplier. Errors: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
        elif request.method == 'DELETE':
            supplier_name = supplier.name
            supplier.delete()
            logger.info(f"Successfully deleted supplier: {supplier_name}")
            return Response(
                {"message": f"Supplier {supplier_name} successfully deleted"},
                status=status.HTTP_204_NO_CONTENT
            )
            
    except Exception as e:
        logger.error(f"Unexpected error in supplier_detail: {str(e)}")
        return Response(
            {"message": "An unexpected error occurred"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
#========================================================Payment========================================================
@api_view(['GET', 'POST'])
def get_payments(request):
    try:
        if request.method == 'GET':
            payments = Payment.objects.all()
            if not payments:
                logger.info("No payments found in the database")
                return Response(
                    {"message": "No payments found."},
                    status=status.HTTP_404_NOT_FOUND
                )
            
            serializer = PaymentSerializer(payments, many=True)
            logger.info(f"Successfully retrieved {len(payments)} payments")
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        elif request.method == 'POST':
            serializer = PaymentSerializer(data=request.data)
            if serializer.is_valid():
                payment = serializer.save()
                logger.info(f"Successfully created new payment: {payment.id}")
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            logger.error(f"Failed to create payment. Errors: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    except Exception as e:
        logger.error(f"Unexpected error in get_payments: {str(e)}")
        return Response(
            {"message": "An unexpected error occurred"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
@api_view(['GET', 'PUT', 'DELETE'])
def payment_detail(request, pk):
    try:
        payment = Payment.objects.get(pk=pk)
    except Payment.DoesNotExist:
        logger.warning(f"Payment with id {pk} not found")
        return Response(
            {"message": "Payment not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    try:
        if request.method == 'GET':
            serializer = PaymentSerializer(payment)
            logger.info(f"Successfully retrieved payment: {payment.id}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            serializer = PaymentSerializer(payment, data=request.data)
            if serializer.is_valid():
                updated_payment = serializer.save()
                logger.info(f"Successfully updated payment: {updated_payment.id}")
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(f"Failed to update payment. Errors: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
        elif request.method == 'DELETE':
            payment_id = payment.id
            payment.delete()
            logger.info(f"Successfully deleted payment: {payment_id}")
            return Response(
                {"message": f"Payment {payment_id} successfully deleted"},
                status=status.HTTP_204_NO_CONTENT
            )
            
    except Exception as e:
        logger.error(f"Unexpected error in payment_detail: {str(e)}")
        return Response(
            {"message": "An unexpected error occurred"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )