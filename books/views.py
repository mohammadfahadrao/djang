import json
import pdb
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.serializers import serialize


from books.models import Questions

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welome </h1>")

def show(request, question_id):
   question =  Questions.objects.get(id=question_id)
   question_json = serialize('json', [question])
    # Deserialize the JSON string into a Python dictionary
   question_data = json.loads(question_json)
   return JsonResponse(question_data, safe=False)

def show_single_obj(request, question_id):
    question = Questions.objects.get(id=question_id)
    question_dict = {
            'id': question.id,
            'publisher_email': question.publisher_email,
            'publisher_name': question.publisher_name,
            # Add more fields as needed
        }
    return JsonResponse(question_dict)