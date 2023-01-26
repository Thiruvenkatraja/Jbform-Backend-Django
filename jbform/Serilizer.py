from rest_framework import serializers
from jbform.models import Jdform

class Jbformserializer(serializers.ModelSerializer):
    class Meta:
        model=Jdform
        fields=["_id",'candidatename','mobile','technology','startdate','followupdate','resource','status','feedback']