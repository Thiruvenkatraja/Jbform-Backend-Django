from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from jbform.models import Jdform
from jbform.Serilizer import Jbformserializer
from rest_framework.response import Response
from rest_framework import status

class JbApiview(APIView):
    serializer_class=Jbformserializer

    def post(self,request,format=None):
        data=request.data
        print(data)
        serializer=Jbformserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,_id,format=None):
        jbform_obj=Jdform.objects.get(_id=_id)
        serializer = Jbformserializer(data=request.data,instance=jbform_obj)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"Data Updated Successfully"})
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,_id,format=None):
        jbform_obj=Jdform.objects.get(_id=_id)
        serializer = Jbformserializer(data=request.data,instance=jbform_obj,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"Data Updated Successfully"})
        
    
    def get(self,request,_id=None,format=None):
        if _id:
            jbform_obj=Jdform.objects.get(_id=_id)
            serializer= Jbformserializer(jbform_obj)
        else:
            queryset=Jdform.objects.all()
            serializer= Jbformserializer(queryset,many=True)
        return Response(serializer.data)
    
    def delete(self,request,_id=None,format=None):
        Jdform.objects.get(_id=_id).delete()
        return Response({"Message":"Data Deleted Successfully"})
    

        
        