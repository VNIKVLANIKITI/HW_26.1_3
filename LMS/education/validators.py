import re
from rest_framework.serializers import ValidationError


class ContentValidator:

    def __init__(self, field):
        self.field = field
    
    def __call__(self, value):
        reg = re.compile('^\b(https?:\/\/)?(www\.)?(youtube\.com\/watch\?v=[\w-]{11}|youtu\.be\/[\w-]{11})\b')
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError('Description content links on not Youtube.com')