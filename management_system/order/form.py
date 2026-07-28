# forms.py
from django import forms

class CheckoutForm(forms.Form):
    user_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    city = forms.CharField(max_length=50)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        base_classes = (
            "w-full bg-[#1b1b1b] border border-gray-700 rounded-xl px-4 py-2.5 "
            "text-white placeholder-gray-500 focus:outline-none focus:ring-2 "
            "focus:ring-[#e08434] focus:border-transparent hover:border-gray-600 "
            "transition-all duration-200"
        )
        for field in self.fields.values():
            field.widget.attrs.update({'class': base_classes})
