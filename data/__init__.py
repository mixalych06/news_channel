__all__=(
    "Base",
    "News_Chita",
    "News_ZabNews",
    "News_Zab",
    "News_AmurLife",
    "News_ASN24",
    "News_AmurInfo"
)
from .base import Base
from .models_zab import News_Zab, News_Chita, News_ZabNews
from .models_amur import News_ASN24, News_AmurLife, News_AmurInfo