# from django.contrib import admin
from django.utils.html import format_html
# from admin_extra_buttons.api import ExtraButtonsMixin, button
# from admin_extra_buttons.utils import HttpResponseRedirectToReferrer

# Register your models here.

class ButtonMixin:

    def show_button(self, obj):
        return format_html(
            '<a class="btn" style="border: #6db0c9; background-color: rgb(109,176,201); padding: 5px; border-radius: 5px; color: white" href="/admin/{}/{}/{}/change/">نمایش</a>',
            obj._meta.app_label, obj._meta.model_name, obj.id)

    def change_button(self, obj):
        return format_html('<a class="btn" style="border: #6db0c9; background-color: rgb(109,176,201); padding: 5px; border-radius: 5px; color: white" href="/admin/{}/{}/{}/change/">ویرایش</a>',
                           obj._meta.app_label, obj._meta.model_name, obj.id)

    def delete_button(self, obj):
        return format_html('<a class="btn" style="border: #d95858; background-color: rgb(217,88,88); padding: 5px; border-radius: 5px; color: white" href="/admin/{}/{}/{}/delete/">حذف</a>',
                           obj._meta.app_label, obj._meta.model_name, obj.id)


# class CustomExtraButtonsMixin(ExtraButtonsMixin, admin.ModelAdmin):
#
#     @button(permission='demo.add_demomodel1',
#             change_form=True,
#             html_attrs={'style': 'background-color:#88FF88;color:black'})
#     def refresh(self, request):
#         self.message_user(request, 'refresh called')
#         # Optional: returns HttpResponse
#         return HttpResponseRedirectToReferrer(request)


