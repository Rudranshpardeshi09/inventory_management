from django import forms
from .models import Issuance
from .constants import COMPONENT_STATUS


class IssuanceForm(forms.ModelForm):
    """
    Form for issuing inventory items with strict business validation.
    """

    class Meta:
        model = Issuance
        fields = [
            'item',
            'quantity',
            'user',
            'issuer',
            'receiver',
            'issue_condition',
            'remark',
        ]
        widgets = {
            'remark': forms.Textarea(attrs={'rows': 2}),
        }

    def clean(self):
        cleaned = super().clean()

        issuer = cleaned.get('issuer')
        receiver = cleaned.get('receiver')
        item = cleaned.get('item')
        qty = cleaned.get('quantity')

        # Issuer & receiver validation
        if issuer and receiver:
            if issuer.lower() == receiver.lower():
                raise forms.ValidationError(
                    "Issuer and receiver cannot be the same person."
                )

            # Business rule: Harsh <-> Gaurav only
            if issuer.lower() == "harsh" and receiver.lower() != "gaurav":
                raise forms.ValidationError(
                    "If issuer is Harsh, receiver must be Gaurav."
                )
            if issuer.lower() == "gaurav" and receiver.lower() != "harsh":
                raise forms.ValidationError(
                    "If issuer is Gaurav, receiver must be Harsh."
                )

        # Stock validation
        if item and qty is not None:
            if qty <= 0:
                raise forms.ValidationError(
                    "Quantity must be greater than zero."
                )

            # NOTE: final stock validation must still be enforced atomically in the view
            if item.quantity < qty:
                raise forms.ValidationError(
                    f"Only {item.quantity} units are available in stock."
                )

        return cleaned


class ReceiveForm(forms.Form):
    """
    Form for receiving issued items back into inventory.
    """

    issuance_id = forms.IntegerField(widget=forms.HiddenInput())
    component_status = forms.ChoiceField(choices=COMPONENT_STATUS)
    remark = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 2})
    )


class ExcelUploadForm(forms.Form):
    """
    Upload form for Excel / CSV inventory import.
    """
    file = forms.FileField(label="Excel file (.xlsx recommended)")
    has_header = forms.BooleanField(
        label="File has header row",
        required=False,
        initial=True
    )


class ColumnMappingForm(forms.Form):
    """
    Placeholder for dynamic Excel column mapping.
    Fields are generated in the view as map_<index>.
    """
    pass
