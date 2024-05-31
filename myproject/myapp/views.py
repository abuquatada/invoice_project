from django.shortcuts import render
from django.shortcuts import render
from .models import * 
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Customers
# from django.contrib.auth import authenticate , login , logout
 



# Create your views here.


@api_view(['GET','POST','PUT','DELETE'])
def Customers_view(request):
    if request.method == 'GET':
        customer_object = Customers.objects.all()
        serializers_obj = customersserializer(customer_object,many=True)
        return Response(serializers_obj.data)
    

    elif request.method == 'POST':
        validated_data = request.data
        serializers_obj=customersserializer(data=validated_data)

        if serializers_obj.is_valid():
            serializers_obj.save()
            return Response({"message":"data posted successfully ","data":serializers_obj.data})
        
        else:
            return Response(serializers_obj.errors)
        

    elif request.method == 'PUT':
        validated_data = request.data
        customer_object = Customers.objects.get(CustomerID=validated_data['CustomerID'])
        serializers_obj = customersserializer(customer_object,data=validated_data)

        if serializers_obj.is_valid():
            serializers_obj.save()
            return Response({"message":"data updated successfully","data":serializers_obj.data})
        
        else:
            return Response(serializers_obj.errors)
        

    elif request.method == 'DELETE':
        delete = request.GET.get('delete')
        if delete:
            customer_object = Customers.objects.get(CustomerID=delete)
            customer_object.delete()
            return Response({"message":"data deleted successfully "})
        



@api_view(['GET','POST','PUT','DELETE'])
def Products_view(request):
    if request.method == 'GET':
        product_object = Products.objects.all()
        serializers_obj = productsserializer(product_object,many=True)
        return Response(serializers_obj.data)
    

    elif request.method == 'POST':
        validated_data = request.data
        serializers_obj=productsserializer(data=validated_data)

        if serializers_obj.is_valid():
            serializers_obj.save()
            return Response({"message":"data posted successfully ","data":serializers_obj.data})
        
        else:
            return Response(serializers_obj.errors)
        

    elif request.method == 'PUT':
        validated_data = request.data
        product_object = Products.objects.get(ProductID=validated_data['ProductID'])
        serializers_obj = productsserializer(product_object,data=validated_data)

        if serializers_obj.is_valid():
            serializers_obj.save()
            return Response({"message":"data updated successfully","data":serializers_obj.data})
        
        else:
            return Response(serializers_obj.errors)
        

    elif request.method == 'DELETE':
        delete = request.GET.get('delete')
        if delete:
            product_object = Products.objects.get(ProductID=delete)
            product_object.delete()
            return Response({"message":"data deleted successfully "})
        









@api_view(['GET','POST','PUT','DELETE'])
def Invoices_view(request):
    if request.method == 'GET':
        invoice_object = Invoices.objects.all()
        serializers_obj = invoicesserializer(invoice_object,many=True)
        return Response(serializers_obj.data)
    

    elif request.method == 'POST':
        validated_data = request.data
        serializers_obj=invoicesserializer(data=validated_data)

        if serializers_obj.is_valid():
            # customer= Customers.objects.get(CustomerID=validated_data['CustomerID'])
            
            # invoice = Invoices.objects.create(CustomerID=customer,
            #                               InvoiceDate=validated_data['InvoiceDate'],
            #                               DueDate=validated_data['DueDate'],
            #                               TotalAmount=validated_data['TotalAmount'],
            #                               Status=validated_data['Status'])
            serializers_obj.save()
            return Response({"message":"data posted successfully ","data":serializers_obj.data})
        
        else:
            return Response(serializers_obj.errors)
        

    elif request.method == 'PUT':
        validated_data = request.data
        invoice_object = Invoices.objects.get(InvoiceID=validated_data['InvoiceID'])
        serializers_obj = invoicesserializer(invoice_object,data=validated_data,partial=True)
        
        if serializers_obj.is_valid():
            serializers_obj.save()
            return Response({"message":"data updated successfully","data":serializers_obj.data} )
        
        else:
            return Response(serializers_obj.errors)
        

    elif request.method == 'DELETE':
        delete = request.GET.get('delete')
        if delete:
            invoice_object = Invoices.objects.get(InvoiceID=delete)
            invoice_object.delete()
            return Response({"message":"data deleted successfully "})
        








@api_view(['GET','POST','PUT','DELETE'])
def InvoicesItems_view(request):
    if request.method == 'GET':
        invoiceitems_object = InvoiceItems.objects.all()
        serializers_obj = invoiceItemsserializer(invoiceitems_object,many=True)
        return Response(serializers_obj.data)
    

    elif request.method == 'POST':
        validated_data = request.data
        serializers_obj=invoiceItemsserializer(data=validated_data)

        if serializers_obj.is_valid():
            invoice = Invoices.objects.get(InvoiceID=validated_data['InvoiceID'])
            product = Products.objects.get(ProductID=validated_data['ProductID'])
            invoiceitems = InvoiceItems.objects.create(InvoiceID=invoice,ProductID=product,
                                                       Quantity=validated_data['Quantity'],
                                                       UnitPrice=validated_data['UnitPrice'],TotalPrice=validated_data['TotalPrice'],TaxAmount=validated_data['TaxAmount'])

            return Response({"message":"data posted successfully ","data":serializers_obj.data})
        
        else:
            return Response(serializers_obj.errors)
        

    elif request.method == 'PUT':
        validated_data = request.data
        invoiceitems_object = InvoiceItems.objects.get(InvoiceItemID=validated_data['InvoiceItemID'])
        serializers_obj = invoiceItemsserializer(invoiceitems_object,data=validated_data)

        if serializers_obj.is_valid():
            serializers_obj.save()
            return Response({"message":"data updated successfully","data":serializers_obj.data})
        
        else:
            return Response(serializers_obj.errors)
        

    elif request.method == 'DELETE':
        delete = request.GET.get('delete')
        if delete:
            invoiceitems_object = InvoiceItems.objects.get(InvoiceItemID=delete)
            invoiceitems_object.delete()
            return Response({"message":"data deleted successfully "})
        







@api_view(['GET','POST','PUT','DELETE'])
def  Payments_view(request):
    if request.method == 'GET':
        payment_object = Payments.objects.all()
        serializers_obj = paymentsserializer(payment_object,many=True)
        return Response(serializers_obj.data)
    

    elif request.method == 'POST':
        validated_data = request.data
        serializers_obj=paymentsserializer(data=validated_data)

        if serializers_obj.is_valid():
            invoice = Invoices.objects.get(InvoiceID=validated_data['InvoiceID'])
            payment = Payments.objects.create(InvoiceID=invoice,
                                              PaymentDate=validated_data['PaymentDate'],
                                              Amount=validated_data['Amount'],
                                              PaymentMethod=validated_data['PaymentMethod'])
            
            return Response({"message":"data posted successfully ","data":serializers_obj.data})
        
        else:
            return Response(serializers_obj.errors)
        

    elif request.method == 'PUT':
        validated_data = request.data
        payment_object = Payments.objects.get(PaymentID=validated_data['PaymentID'])
        serializers_obj = paymentsserializer(payment_object,data=validated_data)

        if serializers_obj.is_valid():
            serializers_obj.save()
            return Response({"message":"data updated successfully","data":serializers_obj.data})
        
        else:
            return Response(serializers_obj.errors)
        

    elif request.method == 'DELETE':
        delete = request.GET.get('delete')
        if delete:
            payment_object = Payments.objects.get(PaymentID=delete)
            payment_object.delete()
            return Response({"message":"data deleted successfully "})
        






@api_view(['GET','POST','PUT','DELETE'])
def  TaxRates_view(request):
    if request.method == 'GET':
        taxrates_object = TaxRates.objects.all()
        serializers_obj = taxratesserializer(taxrates_object,many=True)
        return Response(serializers_obj.data)
    

    elif request.method == 'POST':
        validated_data = request.data
        serializers_obj=taxratesserializer(data=validated_data)

        if serializers_obj.is_valid():
            serializers_obj.save()
            return Response({"message":"data posted successfully ","data":serializers_obj.data})
        
        else:
            return Response(serializers_obj.errors)
        

    elif request.method == 'PUT':
        validated_data = request.data
        taxrates_object = TaxRates.objects.get(TaxRateID=validated_data['TaxRateID'])
        serializers_obj = taxratesserializer(taxrates_object,data=validated_data)

        if serializers_obj.is_valid():
            serializers_obj.save()
            return Response({"message":"data updated successfully","data":serializers_obj.data})
        
        else:
            return Response(serializers_obj.errors)
        

    elif request.method == 'DELETE':
        delete = request.GET.get('delete')
        if delete:
            taxrates_object = TaxRates.objects.get(TaxRateID=delete)
            taxrates_object.delete()
            return Response({"message":"data deleted successfully "})
        










@api_view(['GET','POST','PUT','DELETE'])
def  CoreUser_view(request):
    if request.method == 'GET':
        user_object = CoreUser.objects.all()
        serializers_obj = coreuserserializer(user_object,many=True)
        return Response(serializers_obj.data)
    

    elif request.method == 'POST':
        validated_data = request.data
        serializers_obj=coreuserserializer(data=validated_data)

        if serializers_obj.is_valid():
            role = Role.objects.get(RoleID = validated_data['RoleID'])
            coreUser = CoreUser.objects.create(RoleID = role,
                                               UserName=validated_data['UserName'],
                                               Password=validated_data['Password'])
            
            return Response({"message":"data posted successfully ","data":serializers_obj.data})
        
        else:
            return Response(serializers_obj.errors)
        

    elif request.method == 'PUT':
        validated_data = request.data
        user_object = CoreUser.objects.get(UserID=validated_data['UserID'])
        serializers_obj = coreuserserializer(user_object,data=validated_data)

        if serializers_obj.is_valid():
            serializers_obj.save()
            return Response({"message":"data updated successfully","data":serializers_obj.data})
        
        else:
            return Response(serializers_obj.errors)
        

    elif request.method == 'DELETE':
        delete = request.GET.get('delete')
        if delete:
            user_object= CoreUser.objects.get(UserID=delete)
            user_object.delete()
            return Response({"message":"data deleted successfully "})
        







@api_view(['GET','POST','PUT','DELETE'])
def Role_view(request):
    if request.method == 'GET':
        role_object = Role.objects.all()
        serializer_object = roleserializer(role_object,many=True)
        return Response(serializer_object.data)
    

    elif request.method == 'POST':
        validated_data = request.data
        serializer_object = roleserializer(data=validated_data)

        if serializer_object.is_valid():
            serializer_object.save()
            return Response({"message":"data posted successfully ","data":serializer_object.data})
        
        else:
            return Response(serializer_object.errors)
        

    elif request.method == 'PUT':
        validated_data = request.data
        role_object = Role.objects.get(RoleID =validated_data['RoleID'])
        serializer_object = roleserializer(role_object,data=validated_data)

        if serializer_object.is_valid():
            serializer_object.save()
            return Response({"message":"data updated successfully","data":serializer_object.data})
        
        else:
            return Response(serializer_object.errors)
        


    elif request.method == 'DELETE':
        delete = request.GET.get('delete')

        if delete:
            role_object = Role.objects.get(RoleID=delete)
            role_object.delete()
            return Response({"message":"data deleted successfully"})
        
        else:
            return Response(roleserializer.errors)