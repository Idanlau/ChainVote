from django.contrib import admin
from .models import Election,Candidates,Block,Vote,PrevHash,RealPrevHash

# Register your models here.
class CandidatesAdmin(admin.StackedInline):
    model = Candidates

class ElectionAdmin(admin.ModelAdmin):
    inlines = [CandidatesAdmin]

admin.site.register(Election,ElectionAdmin)
admin.site.register(Block)
admin.site.register(PrevHash)
