from rest_framework.views import APIView
from .models import Package
from rest_framework.response import Response
from . import serializers
class Track(APIView):
    def post(self, request):
        tc = request.data['tracking_code']
        try:
            package = Package.objects.get(tracking=tc)
            
        except:
            return Response({"Unknown Error"})
        ps=serializers.PackageSerializer(package)
        
        data={"package":ps.data}
        return Response(data)



""" class Categories(APIView):
    def get(self,request, *args, **kwargs):
        try:
            if verifyKey(request.headers['APIKEY']):
                items = Category.objects.all()
                serializer = serializers.CategorySeriliazer(items, many=True)
                resp = {"categories":serializer.data}
                return Response(resp)
            else:
                return Response({})
        except:
            return Response({}) """