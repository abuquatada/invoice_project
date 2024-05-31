from rest_framework import routers, serializers,viewsets
from.models import*
from .models import Invoices
from .models import Customers
from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser



class customersserializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields = '__all__'



class productsserializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'



class invoicesserializer(serializers.ModelSerializer):
    CustomerID = customersserializer()

    class Meta:
        model = Invoices
        fields ='__all__'


    def create(self,validated_data):
        customer_data = validated_data.pop('CustomerID')
        print(customer_data)
        customer_data = Customers.objects.create(**customer_data)
        invoice = Invoices.objects.create(**validated_data,CustomerID=customer_data)
        return invoice
        



    def update(self, instance, validated_data):
        # print('\n\n\n',instance,'\n\n\n')
        # print('\n\n\n',validated_data,'\n\n\n')
        customer_data = validated_data.pop('CustomerID')
        # print('\n\n\n',customer_data,'\n\n\n')
        customer_data_data = instance.CustomerID

        customer_data_data.CustomerName = customer_data.get('CustomerName', customer_data_data.CustomerName)
        customer_data_data.ContactName = customer_data.get('ContactName', customer_data_data.ContactName)
        customer_data_data.Address = customer_data.get('Address', customer_data_data.Address)
        customer_data_data.City = customer_data.get('City', customer_data_data.City)
        customer_data_data.PostalCode = customer_data.get('PostalCode', customer_data_data.PostalCode)
        customer_data_data.Country = customer_data.get('Country', customer_data_data.Country)
        customer_data_data.Email = customer_data.get('Email', customer_data_data.Email)
        customer_data_data.Phone = customer_data.get('Phone', customer_data_data.Phone)
        customer_data_data.save()

        print('\n\n\n',customer_data_data,'\n\n\n')
        

        # instance.CustomerID = validated_data.get('CustomerID', instance.CustomerID)
        instance.InvoiceDate = validated_data.get('InvoiceDate', instance.InvoiceDate)
        instance.DueDate = validated_data.get('DueDate', instance.DueDate)
        instance.TotalAmount = validated_data.get('TotalAmount', instance.TotalAmount)
        instance.Status = validated_data.get('Status', instance.Status)    
        instance.save()

        return instance






class invoiceItemsserializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceItems
        fields = '__all__'
        depth = 1




class paymentsserializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'
        depth = 1





class taxratesserializer(serializers.ModelSerializer):

    class Meta:
        model = TaxRates
        fields = '__all__'



class coreuserserializer(serializers.ModelSerializer):

    class Meta:
        model = CoreUser
        fields = '__all__'
        depth = 1


class roleserializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'

        