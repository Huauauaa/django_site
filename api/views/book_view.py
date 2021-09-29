from django.views.decorators.csrf import csrf_exempt
from api.models.Book import Book
from api.serializers.BookSerializer import BookSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


@csrf_exempt
def book_view(request):
    method = request.method
    if method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)

    elif method == 'POST':
        print('post...........', request)
        data = JSONParser().parse(request)
        print(data)
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)

        return JsonResponse(serializer.errors, status=400)
