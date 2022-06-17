import datetime
from django.db import models
from django.db.models.expressions import F
#from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
from django.conf import settings
#from django.core.validators import FileExtensionValidator
from .validators import validate_file_extension
from django.contrib.auth.models import AbstractUser

from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

class Teacher(AbstractUser):

    is_doctor = models.BooleanField(default=False)
    is_simpleuser = models.BooleanField(default=False) # загатовка на будущее, хотя все равно не так надо было сделать
    is_admin = models.BooleanField(default=False)
    is_med = models.ForeignKey("MedicalCenter", verbose_name=("Мед центр"), on_delete=models.CASCADE, null=True, blank=True, related_name="doc_is_med_foreign")

    #for docs and users
    username = None
    email      = models.EmailField(_('email address'), unique=True)
    phone      = models.CharField("Номер телефона", max_length=20, blank=True, null=True)
    first_name = models.CharField(verbose_name="Имя", max_length=100, default="Пользователь")
    last_name  = models.CharField(verbose_name="Фамилия", max_length=100, blank=True)
    text       = RichTextField(blank=True)  #models.TextField(verbose_name="О враче")
    photo      = models.ImageField(upload_to="photo", blank=True, default='photo/user_default.png')
    exp        = models.IntegerField(default=0)
    med        = models.ForeignKey("MedicalCenter", verbose_name=_("Медицинский центр"), on_delete=models.CASCADE, blank=True, null=True)
    services   = models.ManyToManyField("Services", verbose_name=("К какой услуге относится"), blank=True)
    address    = models.CharField(max_length=100, blank=True, null=True)
    time_start = models.TimeField(verbose_name="Начало работы", auto_now=False, auto_now_add=False, blank=True, null=True)
    time_end   = models.TimeField(verbose_name="До", auto_now=False, auto_now_add=False, blank=True, null=True)
    price      = models.IntegerField(default=0)
    rating     = models.FloatField(default=0.0)
    position = models.CharField(verbose_name=("Специализация"), max_length=500)
    num_phone_see = models.IntegerField(verbose_name=("Сколько раз посмотрели номер"), default=0)
    num_page_see = models.IntegerField(verbose_name=("Сколько раз посмотрели страницу"), default=0)
    tegs = models.TextField(verbose_name=("Теги"), blank=True, null=True)

    #for simple users
    cashback   = models.IntegerField(verbose_name=("Cashback"), default=0)
    money      = models.IntegerField(verbose_name=("Кошелек"), default=0)
    date_birthday = models.DateField(verbose_name=("Дата рождения"), auto_now=False, auto_now_add=False, blank=True, null=True)

    #services   = 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def is_open(self,current_date = datetime.datetime.now()):
        if self.time_end is None:
            return False
        
        return current_date < self.time_end

    class Meta:
        verbose_name = _('Врач')
        verbose_name_plural = _('Врачи') 


class MedicalCenter(models.Model):
    photo = models.ImageField(upload_to='med_photo', blank=True, default='med_photo/med_default.png')
    name    = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(verbose_name="Номер без (+7)", default="7776665544", max_length=12)
    phone2 = models.CharField(verbose_name="Номер без (+7)", blank=True, null=True, max_length=12)
    phone2_comment = models.CharField(verbose_name=("Комментарий к номеру"), max_length=50, blank=True, null=True)
    phone3 = models.CharField(verbose_name="Номер без (+7)", blank=True, null=True, max_length=12)
    phone3_comment = models.CharField(verbose_name=("Комментарий к номеру"), max_length=50, blank=True, null=True)
    time_start = models.TimeField(verbose_name="Начало работы", auto_now=False, auto_now_add=False, blank=True, null=True)
    time_end   = models.TimeField(verbose_name="До", auto_now=False, auto_now_add=False, blank=True, null=True)
    all_time = models.BooleanField(verbose_name=("Круглосуточно"), default=False)
    rating = models.FloatField(default=0.0)
    coordX = models.FloatField(verbose_name="Широта", default=0.0)
    coordY = models.FloatField(verbose_name="Долгота", default=0.0)
    views = models.IntegerField(verbose_name=("Количество просмотров"), default=0)
    tegs = models.TextField(verbose_name=("Теги"), blank=True, null=True)
    text = RichTextField(blank=True, null=True) #models.TextField(verbose_name=("О клинике"), null=True, blank=True)
    num_phone_see = models.IntegerField(verbose_name=("Сколько раз посмотрели номер"), default=0)

    pn = models.BooleanField(verbose_name=("Понедельник"), default=True)
    vt = models.BooleanField(verbose_name=("Вторник"), default=True)
    sr = models.BooleanField(verbose_name=("Среда"), default=True)
    cht = models.BooleanField(verbose_name=("Четверг"), default=True)
    pt = models.BooleanField(verbose_name=("Пятница"), default=True)
    sb = models.BooleanField(verbose_name=("Суббота"), default=False)
    vs = models.BooleanField(verbose_name=("Воскресенье"), default=False)

    MODEL_TYPE_CHOICES = (
      (1, 'Вет клиника'),
      (2, 'Зоомагазин'),
      (3, 'Аптека'),
      (4, 'Кинолог'),
      (5, 'Грумеры'),
      (6, 'Приют')
    )

    this_is = models.PositiveSmallIntegerField(choices=MODEL_TYPE_CHOICES, default=1)

    MODEL_TYPE_DISTRICT = (
        (1, 'Ауэзовский'),
        (2, 'Медеуский'), 
        (3, 'Бостандыкский'),
        (4, 'Алмалинский'),
        (5, 'Жетысуский'),
        (6, 'Турксибский'),
        (7, 'Алатауский'),
        (8, 'Наурызбайский')
    )

    district = models.PositiveSmallIntegerField(choices=MODEL_TYPE_DISTRICT, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Центр')
        verbose_name_plural = _('Центры') 


class MedicalImage(models.Model):
    image = models.ImageField(upload_to='med_photo')
    med = models.ForeignKey("MedicalCenter", verbose_name=("Мед центр"), on_delete=models.CASCADE)


class MedicalServices(models.Model):

    med = models.ForeignKey("MedicalCenter", verbose_name=("Мед центр"), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=("Название"), max_length=50)
    price = models.IntegerField(verbose_name=("Цена"))


class Services(models.Model):

    photo = models.FileField(upload_to='service_photo', blank=True, validators=[validate_file_extension])
    name  = models.CharField(max_length=100)
    views = models.IntegerField(verbose_name=("Количество просмотров"), default=0)
    tegs  = models.TextField(verbose_name=("Теги"), blank=True, null=True)
    text  = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги') 

class Bids(models.Model):

    name = models.CharField(verbose_name="Имя", max_length=50)
    date = models.DateTimeField(verbose_name=("Дата заявки"), auto_now=False, auto_now_add=True, blank=True, null=True)
    phone = models.CharField(verbose_name="Номер без (+7)", default="7776665544", max_length=12)
    select = models.CharField(verbose_name="Выбранная услуга", max_length=50)
    who = models.ForeignKey("Teacher", verbose_name=("Врач"), on_delete=models.CASCADE, related_name="bids_who", null=True, blank=True)   #models.IntegerField(verbose_name="id Врача")
    is_completed = models.BooleanField(verbose_name=("Выполенно"), default=False)
    someInfo = models.TextField(verbose_name=("Дополнительная информация"), blank=True, null=True)
    customer = models.ForeignKey("Teacher", verbose_name=("Заказчик"), on_delete=models.CASCADE, related_name="bids_customer", blank=True, null=True)
    
    in_med_center = models.BooleanField(verbose_name=("Заявка у клиники?"), default=False)
    med_center = models.ForeignKey("MedicalCenter", verbose_name=("Мед Центер"), on_delete=models.CASCADE, null=True, blank=True)

    show_phone = models.BooleanField(verbose_name=("Просмотрел врач номер"), default=False)
    date_show_phone = models.DateTimeField(verbose_name=("Время когда врач посмотрел номер"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Заявка')
        verbose_name_plural = _('Заявки') 


class CompletedTask(models.Model):

    user = models.ForeignKey("Teacher", verbose_name=("Тот кто оставлял заявку"), on_delete=models.CASCADE)
    bid = models.ForeignKey("Bids", verbose_name=("Заявка"), on_delete=models.CASCADE)
    complete = models.BooleanField(verbose_name=("Закончено"), default=False)
    score = models.IntegerField(verbose_name=("Оценка"), default=0)

    """
    @property
    def bid_date(self):
        return self.bid.date
    """

    class Meta:
        verbose_name = _('Выполненая заявка')
        verbose_name_plural = _('Выполненые заявки') 
    

class Review(models.Model):
    author = models.ForeignKey("Teacher", verbose_name=("Автор отзыва"), on_delete=models.CASCADE, related_name="author_teacher")
    doctor = models.ForeignKey("Teacher", verbose_name=("Доктор"), on_delete=models.CASCADE, related_name="doctor_teacher")
    review = models.TextField(verbose_name=("Отзыв"))
    rating = models.IntegerField(verbose_name=("Оценка"))
    moderate = models.BooleanField(verbose_name=("Опубликован"), default=False)

    def __str__(self):
        return "%s %s" % (self.doctor.first_name, self.doctor.last_name)

    @property
    def name(self):
        return "%s %s" % (self.doctor.first_name, self.doctor.last_name)

    class Meta:
        verbose_name = _('Отзыв врача')
        verbose_name_plural = _('Отзывы врачей') 
    

class MedReview(models.Model):

    author = models.ForeignKey("Teacher", verbose_name=("Автор отзыва"), on_delete=models.CASCADE, related_name="author_medreview")
    medcenter = models.ForeignKey("MedicalCenter", verbose_name=("Вет клиника"), on_delete=models.CASCADE, related_name="medcenter_medreview")
    review = models.TextField(verbose_name=("Отзыв"))
    rating = models.IntegerField(verbose_name=("Оценка"))
    moderate = models.BooleanField(verbose_name=("Опубликован"), default=False)

    def __str__(self):
        return str(self.medcenter)

    class Meta:
        verbose_name = _('Отзыв клиники')
        verbose_name_plural = _('Отзывы клиник') 
    

class PartnerBid(models.Model):

    name = models.CharField(verbose_name="Имя", max_length=50)
    date = models.DateTimeField(verbose_name=("Дата заявки"), auto_now=False, auto_now_add=True, blank=True, null=True)
    phone = models.CharField(verbose_name="Номер без (+7)", default="7776665544", max_length=11)
    email = models.CharField(verbose_name=("Почта"), max_length=50)

    class Meta:
        verbose_name = _('Партнерская заявка')
        verbose_name_plural = _('Партнерские заявки') 


class Messages(models.Model):

    name = models.CharField(verbose_name="Имя", max_length=50)
    date = models.DateTimeField(verbose_name=("Дата заявки"), auto_now=False, auto_now_add=True)
    phone = models.CharField(verbose_name="Номер без (+7)", default="7776665544", max_length=10)
    email = models.CharField(verbose_name=("Почта"), max_length=50)
    message = models.TextField(verbose_name=("Текст сообщения"))

    def __str__(self):
        return self.name 
    