# dashboard/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Count, Sum, F
from django.core.cache import cache
from django.conf import settings

class DashboardViewSet(viewsets.ViewSet):
    """
    Fully working dashboard viewset for Northwind database
    """
    basename = 'dashboard-stats'
    
    def list(self, request):
        cache_key = 'dashboard_stats'
        data = cache.get(cache_key)
        
        if not data or 'fresh' in request.query_params:
            from products.models import Product
            from orders.models import Order, OrderDetail
            from customers.models import Customer
            from categories.models import Category
            
            # Base metrics
            data = {
                'total_products': Product.objects.count(),
                'total_orders': Order.objects.count(),
                'pending_orders': Order.objects.filter(ShippedDate__isnull=True).count(),
                'total_customers': Customer.objects.count(),
                'total_revenue': OrderDetail.objects.aggregate(
                    revenue=Sum(F('UnitPrice') * F('Quantity'))
                )['revenue'] or 0,
            }
            
            # Get all reference data
            products = dict(Product.objects.values_list('ProductID', 'ProductName'))
            customers = dict(Customer.objects.values_list('CustomerID', 'CompanyName'))
            categories = dict(Category.objects.values_list('CategoryID', 'CategoryName'))
            
            # Get recent orders
            recent_orders = list(
                Order.objects
                .order_by('-OrderDate')[:5]
                .values(
                    'OrderID',
                    'OrderDate',
                    'ShippedDate',
                    'CustomerID'
                )
            )
            
            # Enhance orders with additional data
            for order in recent_orders:
                order['customer_name'] = customers.get(order['CustomerID'], 'Unknown Customer')
                
                order_details = list(
                    OrderDetail.objects
                    .filter(OrderID=order['OrderID'])
                    .values(
                        'UnitPrice',
                        'Quantity',
                        'ProductID'
                    )
                )
                for detail in order_details:
                    detail['product_name'] = products.get(detail['ProductID'], 'Unknown Product')
                order['order_details'] = order_details
            
            data['recent_orders'] = recent_orders
            
            # Calculate category distribution
            category_counts = {}
            for product in Product.objects.values('CategoryID', 'ProductID'):
                cat_id = product['CategoryID']
                category_counts[cat_id] = category_counts.get(cat_id, 0) + 1
            
            data['category_distribution'] = [
                {
                    'category_name': categories.get(cat_id, 'Uncategorized'),
                    'count': count
                }
                for cat_id, count in category_counts.items()
            ]
            
            # Cache with timeout from settings or default (300 seconds)
            cache_timeout = getattr(settings, 'DASHBOARD_CACHE_TIMEOUT', 300)
            cache.set(cache_key, data, timeout=cache_timeout)
        
        return Response(data)