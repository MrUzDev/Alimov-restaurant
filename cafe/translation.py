from modeltranslation.translator import register, TranslationOptions, translator
from cafe.models import Menu, Contact, AboutUs


class MenuTranslationOptions(TranslationOptions):
    fields = ['title', 'body']


class CategoriesTranslationOptions(TranslationOptions):
    fields = ['location', 'body']


class AboutUsTranslationOptions(TranslationOptions):
    fields = ['body', ]


translator.register(Menu, MenuTranslationOptions)
translator.register(Contact, CategoriesTranslationOptions)
translator.register(AboutUs, AboutUsTranslationOptions)