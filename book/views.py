from rest_framework.decorators import api_view
from .serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Books
from django.db.models import Q

@api_view(['POST'])
def create_user_book(request):
    serializer=BookSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'data created successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_book(request):
    # book_name=request.query_params.get('name')
    # book_author=request.query_params.get('author')
    # book_journal=request.query_params.get('journal')
    search = request.query_params.get('search')
    value=Books.objects.all()
    # if book_name:
    #     value=value.filter(Book_name__exact=book_name)
    # if book_author:
    #     value=value.filter(Book_author__exact=book_author)
    # if book_journal:
    #     value=value.filter(Book_journal__exact=book_journal)
    if search:
        value = value.filter(
            Q(Book_name__icontains=search) |
            Q(Book_author__icontains=search) |
            Q(Book_journal__icontains=search)
        )
    result =BookSerializer(value,many=True,context={'request':request})
    return Response({'mesage':'data fetched successfully','data':result.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_book(request,pk):
    values=Books.objects.get(pk=pk)
    results=BookSerializer(values)
    return Response({'message':'data fetched successfuly','data':results.data},status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_user_book(request,pk):
    table=Books.objects.get(pk=pk)
    serializer=BookSerializer(table,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'data created successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_user_book(request,pk):
    result=Books.objects.get(pk=pk)
    result.delete()
    return Response({'message':'data deleted successfully'},status=status.HTTP_204_NO_CONTENT)