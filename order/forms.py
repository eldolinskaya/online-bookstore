from django.forms import ModelForm
from .models import Order
#from home.models import Profile
#from django.contrib.auth.models import User

class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'user_name',
            'buying_type',
            'delivery_address',
            'mobile_number',
            'e_mail',
            'comments',
        ]
    
    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['delivery_address'].help_text = 'В случае самовывоза укажите ваш город'