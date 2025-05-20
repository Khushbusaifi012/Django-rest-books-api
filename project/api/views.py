from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import Bookserializer
from django.shortcuts import get_object_or_404

# Create your views here.
#list and create

class Booklist(APIView):
    def get(self,request):     #get data
        books=Book.objects.all()
        serializer=Bookserializer(books,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=Bookserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#retrieve,update and delete;;;
class Bookdetail(APIView):
    def get(self,request,pk):
        book=get_object_or_404(Book,pk=pk)
        serializer=Bookserializer(book)
        return Response(serializer.data)
    
    def put(self,request,pk):
        book=get_object_or_404(Book,pk=pk)
        serializer=Bookserializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        book=get_object_or_404(Book,pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
def book_list(request):
    return render(request, 'book_list.html')