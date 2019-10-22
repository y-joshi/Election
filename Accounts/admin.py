from django.contrib import admin
from .models import Voter,Candidate,Constituency,State,Constituency_Result,Constituency_Votes,Alliance,Alliance_Result,Party,Party_Result
# Register your models here.

admin.site.register(Voter)
admin.site.register(Candidate)
admin.site.register(Constituency)
admin.site.register(State)
admin.site.register(Constituency_Result)
admin.site.register(Constituency_Votes)
admin.site.register(Alliance)
admin.site.register(Alliance_Result)
admin.site.register(Party)
admin.site.register(Party_Result)
