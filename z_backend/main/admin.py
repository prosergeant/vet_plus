from django.contrib import admin
from .models import * # Services, Teacher, MedicalCenter, Bids, Review, MedReview, CompletedTask
from .forms import * # TeacherCreationForm, TeacherChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
#admin.site.register(MedicalCenter)
admin.site.register(Bids)
admin.site.register(CompletedTask)
admin.site.register(Services)
admin.site.register(Messages)
admin.site.register(MedicalImage)
admin.site.register(MedicalServices)
admin.site.register(PartnerBid)

class TeacherAdmin(UserAdmin):
    add_form = TeacherCreationForm
    form = TeacherChangeForm
    model = Teacher
    list_display = ('email', 'is_staff', 'is_doctor', 'first_name', 'last_name', 'med',)
    list_filter  = ('email', 'is_staff', 'is_active', 'first_name', 'last_name', 'med',)
    fieldsets = (
        (None, {'fields': ('is_doctor', 'is_simpleuser', 'is_admin', 'is_med', 'email', 'password', 'phone', 'first_name', 'last_name', 'position', 'rating', 'text', 'photo', 'exp', 'med', 'services', 'address', 'time_start', 'time_end', 'price', 'date_birthday', 'tegs', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Teacher, TeacherAdmin)


@admin.action(description='Опубликовать')
def make_published(modeladmin, request, queryset):
    queryset.update(moderate=True)
    all_moderated_reviews = modeladmin.model.objects.filter(moderate=True)
    print(queryset)


@admin.action(description='Скрыть')
def make_hiden(modeladmin, request, queryset):
    queryset.update(moderate=False)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('name', 'rating', 'moderate')
    list_filter = ('rating', 'doctor',)

    actions = [make_published, make_hiden]


@admin.register(MedReview)
class MedReviewAdmin(admin.ModelAdmin):
    model = MedReview
    list_display = ('medcenter', 'rating', 'moderate')
    list_filter = ('rating', 'medcenter',)

    actions = [make_published, make_hiden]


@admin.register(MedicalCenter)
class MedicalCenterAdmin(admin.ModelAdmin):
    model = MedicalCenter
    #list_display = ('__all__')
    list_filter = ('this_is',)


    

    