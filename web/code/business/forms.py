from django import forms
from .models.bzBrand import bzBrand
from .models.bzCreativeRendering import bzCreativeRendering
from .models.bzCreativeLayout import bzCreativeLayout
from .models.bzProduct import bzProduct

from vendor_printful.models.pfCatalogVariant import pfCatalogVariant
from vendor_printful.models.pfCatalogSize import pfCatalogSize
from vendor_printful.models.pfCatalogColor import pfCatalogColor


class bzCreativeRenderingForm(forms.ModelForm):

    class Meta:
        model = bzCreativeRendering
        fields = ['bzcreativelayout']

    def __init__(self, *args, **kwargs):
        super(bzCreativeRenderingForm, self).__init__(*args, **kwargs)
        try:
            self.fields['bzcreativelayout'].queryset = bzCreativeLayout.objects.filter(
                bzcreativecollection=self.instance.bzcreativedesign.bzcreativecollection)
        except:
            self.fields['bzcreativelayout'].queryset = bzCreativeLayout.objects.none()


class bzProductForm(forms.ModelForm):

    class Meta:
        model = bzProduct
        fields = [
            'pfSizes', 'pfColors',
        ]
        widgets = {
            'pfSizes': forms.CheckboxSelectMultiple(),
            'pfColors': forms.CheckboxSelectMultiple(),
            # 'get_pfvariants': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(bzProductForm, self).__init__(*args, **kwargs)

        try:
            if self.instance:
                self.fields['pfSizes'].queryset = self.instance.pfProduct.get_sizes()
            else:
                self.fields['pfSizes'].queryset = pfCatalogSize.objects.none()
        except:
            self.fields['pfSizes'].queryset = pfCatalogSize.objects.none()

        try:
            if self.instance:
                self.fields['pfColors'].queryset = self.instance.pfProduct.get_colors()
            else:
                self.fields['pfColors'].queryset = pfCatalogColor.objects.none()
        except:
            self.fields['pfColors'].queryset = pfCatalogColor.objects.none()
