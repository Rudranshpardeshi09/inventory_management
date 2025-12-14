# inventory/forms.py
from django import forms
from .models import Issuance
from .constants import ISSUER_CHOICES, COMPONENT_STATUS, ISSUE_CONDITION, CATEGORY_CHOICES

# Define these here again safely (this avoids ImportError)



class IssuanceForm(forms.ModelForm):
    class Meta:
        model = Issuance
        fields = ['item', 'quantity', 'user', 'issuer', 'receiver', 'issue_condition', 'remark']
        widgets = {
            'remark': forms.Textarea(attrs={'rows': 2}),
        }

    def clean(self):
        cleaned = super().clean()
        issuer = cleaned.get('issuer')
        receiver = cleaned.get('receiver')
        item = cleaned.get('item')
        qty = cleaned.get('quantity')

        # ✅ issuer and receiver cannot be same
        if issuer and receiver:
            if issuer.lower() == receiver.lower():
                raise forms.ValidationError("Issuer and receiver cannot be the same person.")

            # ✅ Only Harsh & Gaurav logic
            if issuer.lower() == "harsh" and receiver.lower() != "gaurav":
                raise forms.ValidationError("If issuer is Harsh, receiver must be Gaurav.")
            if issuer.lower() == "gaurav" and receiver.lower() != "harsh":
                raise forms.ValidationError("If issuer is Gaurav, receiver must be Harsh.")

        # ✅ stock validation
        if item and qty:
            if qty <= 0:
                raise forms.ValidationError("Quantity must be greater than zero.")
            if item.quantity < qty:
                raise forms.ValidationError(f"Only {item.quantity} units are available in stock.")

        return cleaned


class ReceiveForm(forms.Form):
    issuance_id = forms.IntegerField(widget=forms.HiddenInput())
    component_status = forms.ChoiceField(choices=COMPONENT_STATUS)
    remark = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 2}))


#excel upload
class ExcelUploadForm(forms.Form):
    file = forms.FileField(label="Excel file (.xlsx recommended)")
    has_header = forms.BooleanField(label="File has header row", required=False, initial=True)

class ColumnMappingForm(forms.Form):
    """
    This form will be created dynamically in the view. It maps excel columns -> model fields.
    Each mapping field name will be 'map_<excel_col_index>' so we can iterate in view.
    """
    pass