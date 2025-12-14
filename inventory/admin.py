from django.contrib import admin
from .models import Item, Transaction
from .models import Issuance

admin.site.register(Item)
admin.site.register(Transaction)
@admin.register(Issuance)
class IssuanceAdmin(admin.ModelAdmin):
    list_display = ('id','item','quantity','issuer','user','receiver','issue_date','receive_date','component_status','received')
    list_filter = ('issuer','component_status','received')