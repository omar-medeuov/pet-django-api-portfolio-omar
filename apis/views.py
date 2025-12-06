from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET", "POST"])
def index(request):
    if request.method == "POST":
        return Response({"message": "Got some data using POST"})
    elif request.method == "GET":
        return Response({"message": "Here's your GET data"})
