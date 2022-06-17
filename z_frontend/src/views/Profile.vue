<template>
    <div class="mt-5">
        <!-- doctor v2 -->
        <div v-if="userdata.is_doctor">
            <CRow>
                <CCol md='10' class="mx-auto">
                    <CRow>
                        <CCol md='4'>
                            <CCard class="p-1">
                                <CRow>
                                    <CCol sm='10' class="text-center mx-auto">
                                        <img :src="userdata.photo" style="border-radius: 50%; width: 74px; height: 74px;" class="mb-3 mt-3">
                                    </CCol>

                                    <CCol sm='12' class="text-center mb-3">
                                        <h4>{{userdata.first_name}} {{userdata.last_name}}</h4>
                                    </CCol>

                                    <CCol sm='10' class="mx-auto my-3">
                                        <CButton class="w-100" style="color: white; background-color: #FF8A34;" @click="editTab = true, infoTab = false, inputTab = false, endedTab = false, journalTab = false"> Редактировать данные </CButton>
                                    </CCol>

                                    <CCol sm='12'>
                                        <div class="w-100">
                                            <span style="visibility:hidden;"> invis </span>
                                        </div>
                                    </CCol>

                                    <CCol sm='10' class="mx-auto my-1">
                                        <CButton
                                        class="w-100" 
                                        :class="infoTab ? 'pressed_tab' : '' "
                                        @click="infoTab = true, inputTab = false, endedTab = false, journalTab = false, editTab = false"> Информация </CButton>
                                    </CCol>

                                    <CCol sm='10' class="mx-auto my-1">
                                        <CButton 
                                        class="w-100" 
                                        :class="inputTab ? 'pressed_tab' : '' "
                                        @click="loadBids(), infoTab = false, inputTab = true, endedTab = false, journalTab = false, editTab = false"> Входящие заявки </CButton>
                                    </CCol>

                                    <CCol sm='10' class="mx-auto my-1">
                                        <CButton 
                                        class="w-100" 
                                        :class="endedTab ? 'pressed_tab' : '' "
                                        @click="loadBids(), infoTab = false, inputTab = false, endedTab = true, journalTab = false, editTab = false"> Завершенные заявки </CButton>
                                    </CCol>

                                    
                                    <CCol sm='10' class="mx-auto my-1">
                                        <CButton 
                                        class="w-100" 
                                        :class="journalTab ? 'pressed_tab' : '' "
                                        @click="infoTab = false, inputTab = false, endedTab = false, journalTab = true, editTab = false"> Расписание </CButton>
                                    </CCol>
                                    

                                    <CCol sm='12'>
                                        <div class="w-100">
                                            <span style="visibility:hidden;"> invis </span>
                                        </div>
                                    </CCol>

                                </CRow>
                            </CCard>
                        </CCol>

                        <CCol md='8'>
                            <CCard class="p-3 infotab" v-if="infoTab">
                                <h3>Информация</h3>
                                <br>
                                <h4> {{userdata.first_name}} {{userdata.last_name}} </h4>
                                <br>
                                <p class="gray">Должность</p>
                                <p> {{userdata.position}} </p>
                                <br>
                                <p class="gray">Стаж работы по специальности</p>
                                <p>Более {{userdata.exp}} лет</p>
                                <br>
                                <p class="gray">Место работы</p>
                                <p v-if="userdata.med == null">Частный врач</p>
                                <p v-else> <router-link :to="{name: 'med', params: {id: userdata.med.id}}"> {{userdata.med.name}} </router-link></p>
                                <br>
                                <p class="gray">Время приема</p>
                                <p> {{userdata.time_start}} - {{userdata.time_end}} </p>
                                <br>
                                <CRow>
                                    <CCol sm='1' >
                                        <img src="/img/phone.png" width="20" height="20" class="ml-4"/>
                                    </CCol>
                                    <CCol sm='11'>
                                        <p> +7 {{userdata.phone}} </p>
                                    </CCol>
                                </CRow>
                                <br>
                                <p class="gray">Образование</p>
                            </CCard>

                            <CCard class="p-3" v-if="editTab">
                                <h3>Редактировать профиль</h3>
                                <CRow>
                                    <CCol sm='6'>
                                        <CInput label="Фамилия" :placeholder="userdata.last_name" v-model="last_name" />
                                    </CCol>

                                    <CCol sm='6'>
                                        <CInput label="Имя" :placeholder="userdata.first_name" v-model="first_name" />
                                    </CCol>

                                    <CCol sm='6'>
                                        <CRow>
                                            <CCol sm='12'>
                                                <p class="mb-2">Дата рождения</p>
                                            </CCol>

                                            <CCol sm='4'>
                                                <CSelect :placeholder="dayOfBirth" :options="optionDay" v-model="dayOfBirth" :value.sync="dayOfBirth" />
                                            </CCol>

                                            <CCol sm='4'>
                                                <CSelect :placeholder="monthOfBirth" :options="optionMonth" v-model="monthOfBirth" :value.sync="monthOfBirth" />
                                            </CCol>

                                            <CCol sm='4'>
                                                <CSelect :placeholder="yearOfBirth" :options="optionYear" v-model="yearOfBirth" :value.sync="yearOfBirth" />
                                            </CCol>
                                        </CRow>
                                    </CCol>

                                    <CCol sm='6'>
                                        <p class="m-0 mb-1">Номер телефона</p>
                                        <VuePhoneNumberInput v-model="phone" maxlength="12" default-country-code="KZ" />
                                    </CCol>

                                    <CCol sm='12'>
                                        <CInput label="Образование" />
                                    </CCol>

                                    <CCol sm='12'>
                                        <CInput label="Специализация" :placeholder="userdata.position" v-model="position" />
                                    </CCol>

                                    <CCol sm='12'>
                                        <CInput v-if="userdata.med == null" label="Место работы" disabled placeholder="Частный врач" />
                                        <CInput v-else label="Место работы" disabled />
                                    </CCol>


                                    <CCol sm='6'>
                                        <CInput label="Стаж работы" :placeholder="userdata.exp" v-model="exp" />
                                    </CCol>

                                    <CCol sm='6'>
                                        <CInput label="Время приема" :placeholder="`${userdata.time_start} - ${userdata.time_end}`" />
                                    </CCol>

                                    <CCol sm='8'>
                                        <p>Если у вас имеются сертификаты, вы можете загрузить их на свою страницу</p>
                                        <p class="attach" @click="attach">Прикрепить файл</p>
                                    </CCol>

                                    <CCol sm='4'>
                                        <CButton class="save__changes" @click="saveChanges"> Сохранить изменения </CButton>
                                        <p style="background-color: orange;
                                                width: 100px;
                                                text-align: center;
                                                border-radius: 15px;
                                                color: #fff;
                                                position:relative;
                                                top: 10px;"
                                                v-if="is_changesSaved">Сохраненно</p>
                                    </CCol>
                                </CRow>
                            </CCard>

                            <CCard class="p-3" v-if="inputTab" style="min-height: 500px;">
                                <h3>Входящие заявки</h3>
                                <br>
                                <CRow>
                                    <CCol sm='2'>
                                        <p>Имя</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Услуга</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Дата записи</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Номер телефона</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Врач</p>
                                    </CCol>

                                </CRow>

                                <CCard style="background-color: #F9FAFC;
                                            padding: 1rem;">
                                <CRow v-for="i in bidsData" :key="i.id">
                                    <CCol sm='2'>
                                        <p><strong> {{i.name}} </strong></p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p><strong>{{i.select}}</strong></p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p><strong>{{i.date | toDate}}</strong></p>
                                        <p><strong>{{i.date | toTime}}</strong></p>
                                    </CCol>

                                    <CCol sm='3'>
                                        <CButton v-if="i.show_phone == false" color="success" class="m-0 p-0" style="height: 20px;" @click="showPhone(i.id)"> Показать номер </CButton> <p><strong v-if="i.show_phone">+7{{i.phone}}</strong></p>
                                    </CCol>


                                    <CCol sm='2'>
                                        <CButton class="orange__btn" @click="makeComplete(i.id)">Завершить</CButton>
                                    </CCol>

                                    <CCol sm='12'>
                                        <CCard style="background-color: #fff;
                                                    min-height: 45px;
                                                    padding: 0.5rem;">
                                            <p v-if="i.someInfo">Доп коментарий: {{i.someInfo}} </p>
                                            <p v-else>Без комментария</p>
                                        </CCard>
                                    </CCol>
                                    
                                </CRow>
                                </CCard>
                            </CCard>

                            <CCard class="p-3" v-if="endedTab" style="min-height: 500px;">
                                <h3>Завершенные заявки</h3>
                                <br>
                                <CRow>
                                    <CCol sm='2'>
                                        <p>Имя</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Услуга</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Дата записи</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Номер телефона</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Врач</p>
                                    </CCol>

                                </CRow>

                                <CCard style="background-color: #F9FAFC;
                                            padding: 1rem;">
                                <CRow v-for="i in bidsDataComplete" :key="i.id">
                                    <CCol sm='2'>
                                        <p><strong> {{i.name}} </strong></p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p><strong>{{i.select}}</strong></p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p><strong>{{i.date | toDate}}</strong></p>
                                        <p><strong>{{i.date | toTime}}</strong></p>
                                    </CCol>

                                    <CCol sm='3'>
                                        <p><strong>+7 {{ i.phone }}</strong></p>
                                    </CCol>


                                    <CCol sm='2'>
                                        <p v-if="i.who != null"><strong> {{i.who.first_name}} {{i.who.last_name | toFirstLetter}}. </strong></p>
                                    </CCol>

                                    <CCol sm='12'>
                                        <CCard style="background-color: #fff;
                                                    min-height: 45px;
                                                    padding: 0.5rem;">
                                            <p v-if="i.someInfo">Доп коментарий: {{i.someInfo}} </p>
                                            <p v-else>Без комментария</p>
                                        </CCard>
                                    </CCol>
                                    
                                </CRow>
                                </CCard>
                            </CCard>

                            <CCard class="p-3" v-if="journalTab">
                                <h3>Расписание</h3>
                                <JqxScheduler ref="myScheduler"
                                    :localization="{
                                        '/': '/',
                                        // separator of parts of a time (e.g. ':' in 05:44 PM)
                                        ':': ':',
                                        firstDay:1,
                                        days: {
                                            names: ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'],
                                            namesAbbr: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
                                            namesShort: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб']
                                        },
                                        months: {
                                            names: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октабрь', 'Ноябрь', 'Декабрь', ''],
                                            namesAbbr: ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек', '']
                                        },
                                        backString: 'Назад',
                                        forwardString: 'Вперед',
                                        toolBarPreviousButtonString: 'Предыдущий',
                                        toolBarNextButtonString: 'Следующий',
                                        emptyDataString: 'Пустая строка',
                                        loadString: 'Загругка...',
                                        clearString: 'Чисто',
                                        todayString: 'Сегодня',
                                        dayViewString: 'День',
                                        weekViewString: 'Неделя',
                                        monthViewString: 'Месяц',
                                        timelineDayViewString: 'Zeitleiste Day',
                                        timelineWeekViewString: 'Zeitleiste Woche',
                                        timelineMonthViewString: 'Zeitleiste Monat',
                                        loadingErrorMessage: 'Произошла ошибка во время загрузки',
                                        editRecurringAppointmentDialogTitleString: 'Добавить новое событие',
                                        editRecurringAppointmentDialogContentString: 'Wollen Sie nur dieses eine Vorkommen oder die Serie zu bearbeiten ?',
                                        editRecurringAppointmentDialogOccurrenceString: 'Vorkommen bearbeiten',
                                        editRecurringAppointmentDialogSeriesString: 'Bearbeiten Die Serie',
                                        editDialogTitleString: 'Изменить событие',
                                        editDialogCreateTitleString: 'Добавить новое событие',
                                        contextMenuEditAppointmentString: 'Изменить событие',
                                        contextMenuCreateAppointmentString: 'Добавить новое событие',
                                        editDialogSubjectString: 'Тема',
                                        editDialogLocationString: 'Место',
                                        editDialogFromString: 'От',
                                        editDialogToString: 'До',
                                        editDialogAllDayString: 'Весь день',
                                        editDialogExceptionsString: 'Исключения',
                                        editDialogResetExceptionsString: 'Zurücksetzen auf Speichern',
                                        editDialogDescriptionString: 'Описание',
                                        editDialogResourceIdString: 'Календарь',
                                        editDialogStatusString: 'Статус',
                                        editDialogColorString: 'Цвет',
                                        editDialogColorPlaceHolderString: 'Цвет',
                                        editDialogTimeZoneString: 'Часовой пояс',
                                        editDialogSelectTimeZoneString: 'Выбрать часовой пояс',
                                        editDialogSaveString: 'Сохранить',
                                        editDialogDeleteString: 'Удалить',
                                        editDialogCancelString: 'Отмена',
                                        editDialogRepeatString: 'Повторить',
                                        editDialogRepeatEveryString: 'Wiederholen alle',
                                        editDialogRepeatEveryWeekString: 'woche(n)',
                                        editDialogRepeatEveryYearString: 'Jahr (en)',
                                        editDialogRepeatEveryDayString: 'Tag (e)',
                                        editDialogRepeatNeverString: 'Нет',
                                        editDialogRepeatDailyString: 'Ежедневно',
                                        editDialogRepeatWeeklyString: 'Еженедельно',
                                        editDialogRepeatMonthlyString: 'Ежемесячно',
                                        editDialogRepeatYearlyString: 'Ежегодно',
                                        editDialogRepeatEveryMonthString: 'Monate (n)',
                                        editDialogRepeatEveryMonthDayString: 'Day',
                                        editDialogRepeatFirstString: 'erste',
                                        editDialogRepeatSecondString: 'zweite',
                                        editDialogRepeatThirdString: 'dritte',
                                        editDialogRepeatFourthString: 'vierte',
                                        editDialogRepeatLastString: 'letzte',
                                        editDialogRepeatEndString: 'Ende',
                                        editDialogRepeatAfterString: 'Nach',
                                        editDialogRepeatOnString: 'Am',
                                        editDialogRepeatOfString: 'von',
                                        editDialogRepeatOccurrencesString: 'Eintritt (e)',
                                        editDialogRepeatSaveString: 'Vorkommen Speichern',
                                        editDialogRepeatSaveSeriesString: 'Save Series',
                                        editDialogRepeatDeleteString: 'Vorkommen löschen',
                                        editDialogRepeatDeleteSeriesString: 'Series löschen',

                                        AM: null,
                                        PM: null,

                                        
                                    }"

                                    :editDialogCreate="function (dialog, fields, editAppointment) {
                                    fields.timeZoneContainer.hide();
                                    fields.repeatContainer.hide();
                                    fields.statusContainer.hide();
                                    fields.colorContainer.hide();
                                    }"

                                    @appointmentChange="onAppointmentChange($event)"
                                    
                                    width="100%" :height="600" :source="dataAdapter" :date="date" :showLegend="true" :view="'weekView'"
                                    :appointmentDataFields="appointmentDataFields" :resources="resources" :views="views"
                                />

                            </CCard>
                        </CCol>
                    </CRow>
                </CCol>
            </CRow>
        </div>

      <!-- simple user v2 -->
        <div v-if="userdata.is_simpleuser">
            <CRow>
                <CCol md='10' class="mx-auto">
                    <CRow>
                        <CCol md='4'>
                            <CCard class="p-1">
                                <CRow>
                                    <CCol sm='10' class="text-center mx-auto">
                                        <img :src="userdata.photo" style="border-radius: 50%; width: 74px; height: 74px;" class="mb-3 mt-3">
                                    </CCol>

                                    <CCol sm='12' class="text-center mb-3">
                                        <h4 class="m-0">{{userdata.first_name}} {{userdata.last_name}}</h4>
                                    </CCol>

                                   

                                    <CCol sm='12'>
                                        <CRow class="">
                                            <CCol sm='5' class="mx-auto">
                                                <img src="/img/wallet.png" width="24" height="24" class="float-left mr-2" :style="windowWidth < 575 ? `margin-left: calc((${windowWidth}px - 196px)/2)` : '' " />
                                                <p style="color: orange;" class="m-0 mr-2 float-left"> <strong> {{userdata.money}} </strong> </p>
                                                <p><strong>бонусов</strong></p>
                                            </CCol>
                                        </CRow>
                                    </CCol>

                                    <CCol sm='10' class="mx-auto my-3">
                                        <CButton class="w-100" style="color: white; background-color: #FF8A34;" @click="editTab = true, infoTab = false, inputTab = false"> Редактировать данные </CButton>
                                    </CCol>

                                    <CCol sm='12'>
                                        <div class="w-100">
                                            <span style="visibility:hidden;"> invis </span>
                                        </div>
                                    </CCol>

                                    <CCol sm='10' class="mx-auto my-1">
                                        <CButton
                                        class="w-100" 
                                        :class="infoTab ? 'pressed_tab' : '' "
                                        @click="infoTab = true, inputTab = false, editTab = false"> Информация </CButton>
                                    </CCol>

                                    <CCol sm='10' class="mx-auto my-1">
                                        <CButton 
                                        class="w-100" 
                                        :class="inputTab ? 'pressed_tab' : '' "
                                        @click="infoTab = false, inputTab = true, editTab = false"> История </CButton>
                                    </CCol>

                                    <CCol sm='12'>
                                        <div class="w-100">
                                            <span style="visibility:hidden;"> invis </span>
                                        </div>
                                    </CCol>

                                </CRow>
                            </CCard>
                        </CCol>

                        <CCol md='8'>
                            <CCard class="p-3" v-if="infoTab">
                                <h3>Информация</h3>
                                <CRow>
                                    <CCol sm='6'>
                                        <CInput label="Фамилия" :placeholder="userdata.last_name" disabled />
                                    </CCol>

                                    <CCol sm='6'>
                                        <CInput label="Имя" :placeholder="userdata.first_name" disabled />
                                    </CCol>

                                    <CCol sm='6'>
                                        <CRow>
                                            <CCol sm='12'>
                                                <p class="mb-2">Дата рождения</p>
                                            </CCol>

                                            <CCol sm='4'>
                                                <CSelect :placeholder="dayOfBirth" :options="optionDay" disabled />
                                            </CCol>

                                            <CCol sm='4'>
                                                <CSelect :placeholder="monthOfBirth" :options="optionMonth" disabled />
                                            </CCol>

                                            <CCol sm='4'>
                                                <CSelect :placeholder="yearOfBirth" :options="optionYear" disabled />
                                            </CCol>
                                        </CRow>
                                    </CCol>

                                    <CCol sm='6'>
                                        <CInput label="Номер телефона" maxlength="10" :placeholder="userdata.phone" disabled />
                                    </CCol>

                                    <CCol sm='6'>
                                        <CButton class="blue__btn w-100" @click="changeUserPassword = true"> Измененить пароль </CButton>
                                    </CCol>
                                    <CCol sm='6'>
                                        <div class="w-100"></div>
                                    </CCol>

                                    <CCol sm='6' class="mt-2" v-if="changeUserPassword">
                                        <CInput label="Новый пароль" v-model="password" />
                                    </CCol>
                                    <CCol sm='6' v-if="changeUserPassword">
                                        <div class="w-100"></div>
                                    </CCol>

                                    <CCol sm='6' v-if="changeUserPassword">
                                        <CButton class="blue__btn w-100" @click="changePassword"> Сохранить пароль </CButton>
                                    </CCol>

                                    <CCol sm='6' v-if="is_pass_updated">
                                        <p class="blue__btn text-center" style="border-radius: 15px;">Пароль успешно сохранен</p>
                                    </CCol>
                                </CRow>
                            </CCard>

                            <CCard class="p-3" v-if="editTab">
                                <h3>Редактировать профиль</h3>
                                <CRow>
                                    <CCol sm='6'>
                                        <CInput label="Фамилия" :placeholder="userdata.last_name" v-model="last_name" />
                                    </CCol>

                                    <CCol sm='6'>
                                        <CInput label="Имя" :placeholder="userdata.first_name" v-model="first_name" />
                                    </CCol>

                                    <CCol sm='6'>
                                        <CRow>
                                            <CCol sm='12'>
                                                <p class="mb-2">Дата рождения</p>
                                            </CCol>

                                            <CCol sm='4'>
                                                <CSelect :placeholder="dayOfBirth" :options="optionDay" v-model="dayOfBirth" :value.sync="dayOfBirth" />
                                            </CCol>

                                            <CCol sm='4'>
                                                <CSelect :placeholder="monthOfBirth" :options="optionMonth" v-model="monthOfBirth" :value.sync="monthOfBirth" />
                                            </CCol>

                                            <CCol sm='4'>
                                                <CSelect :placeholder="yearOfBirth" :options="optionYear" v-model="yearOfBirth" :value.sync="yearOfBirth" />
                                            </CCol>
                                        </CRow>
                                    </CCol>

                                    <CCol sm='6'>
                                        <p class="m-0 mb-1">Номер телефона</p>
                                        <VuePhoneNumberInput v-model="phone" maxlength="12" default-country-code="KZ" />
                                    </CCol>



                                    <CCol sm='4'>
                                        <CButton class="save__changes" @click="saveChanges"> Сохранить изменения </CButton>
                                        <p style="background-color: orange;
                                                width: 100px;
                                                text-align: center;
                                                border-radius: 15px;
                                                color: #fff;
                                                position:relative;
                                                top: 10px;"
                                                v-if="is_changesSaved">Сохраненно</p>
                                    </CCol>
                                    <CCol sm='2'>
                                        <div class="w-100"></div>
                                    </CCol>

                                    <CCol sm='6'>
                                        <CInput label="Сменить фото" type="file" id="img_user" />
                                        <CButton class="blue__btn w-50" style="height:30px;" @click.prevent="setNewImageUser"> Сменить </CButton>
                                    </CCol>
                                </CRow>
                            </CCard>

                            <CCard class="p-3" v-if="inputTab" style="min-height: 500px;">
                                <h3>История</h3>
                                <br>
                                <CRow>
                                    <CCol sm='2'>
                                        <p>Имя</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Услуга</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Дата записи</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Время записи</p>
                                    </CCol>

                                    <CCol sm='3'>
                                        <p>Оценка</p>
                                    </CCol>

                                </CRow>

                                <CRow v-for="i in completedTaskForCurrUser" :key="i.id">
                                    <CCol sm='2'>
                                        <p><strong> {{i.bid.who.first_name}} {{i.bid.who.last_name | toFirstLetter}}. </strong></p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p><strong>{{i.bid.select}}</strong></p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p><strong>{{i.bid.date | toDate}}</strong></p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p><strong>{{i.bid.date | toTime}}</strong></p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p><strong> {{i.score}} </strong></p>
                                    </CCol>

                                    <CCol sm='1'>
                                        <CButton 
                                            v-if="i.complete == false"
                                            style="position: relative;
                                            top: -10px;
                                            background-color: orange;
                                            color: #fff;
                                            height: 35px;"
                                            @click="ReviewModal = true, currIdOfCompletedTask = i.id"> Завершить </CButton>
                                    </CCol>

                                    <p v-if="i.someInfo" class="ml-3">Доп коментарий: <strong>{{i.bid.someInfo}}</strong></p>
                                    <hr>
                                </CRow>
                            </CCard>
                        </CCol>
                    </CRow>
                </CCol>
            </CRow>
        </div>


        <div v-if="userdata.is_med">
            <CRow> 
                <CCol md='10' class="mx-auto">
                    <CRow>
                        <CCol md='4'>
                            <CCard class="p-1">
                                <CRow>
                                    <CCol sm='10' class="text-center mx-auto">
                                        <img :src="currMedData.photo" style="border-radius: 15px; width: 90%; height: 90%;" class="mb-3 mt-3">
                                    </CCol>

                                    <CCol sm='12' class="text-center mb-3">
                                        <h4>{{currMedData.name}}</h4>
                                        <img style="position:absolute; top:5px;right: 70px;" src="/img/eye.png" width="20" height="20" />
                                        <p style="position:absolute;top:5px; right: 40px;"> {{currMedData.views}} </p>
                                    </CCol>

                                    <CCol sm='10' class="mx-auto my-3">
                                        <CButton class="w-100" style="color: white; background-color: #FF8A34;" @click="editProfileMode = true, infoTab = false, inputTab = false, endedTab = false"> Редактировать данные </CButton>
                                    </CCol>

                                    <CCol sm='12'>
                                        <div class="w-100">
                                            <span style="visibility:hidden;"> invis </span>
                                        </div>
                                    </CCol>

                                    <CCol sm='10' class="mx-auto my-1">
                                        <CButton
                                        class="w-100" 
                                        :class="infoTab ? 'pressed_tab' : '' "
                                        @click="infoTab = true, inputTab = false, endedTab = false, editProfileMode = false, setMap()"> Информация </CButton>
                                    </CCol>

                                    <CCol sm='10' class="mx-auto my-1">
                                        <CButton
                                        class="w-100" 
                                        :class="inputTab ? 'pressed_tab' : '' "
                                        @click="loadBidsDataForCurrMed() ,infoTab = false, inputTab = true, endedTab = false, editProfileMode = false"> Входящие заявки </CButton>
                                    </CCol>

                                    <CCol sm='10' class="mx-auto my-1">
                                        <CButton
                                        class="w-100" 
                                        :class="endedTab ? 'pressed_tab' : '' "
                                        @click="loadBidsDataForCurrMed(), infoTab = false, inputTab = false, endedTab = true, editProfileMode = false"> Завершенные заявки </CButton>
                                    </CCol>


                                    <CCol sm='12'>
                                        <div class="w-100">
                                            <span style="visibility:hidden;"> invis </span>
                                        </div>
                                    </CCol>

                                </CRow>
                            </CCard>
                        </CCol>

                        <CCol md='8'>
                            <CCard class="p-3" v-if="editProfileMode">
                                <h3>Редактировать данные</h3>

                                <CRow>
                                    <CCol sm='3'>
                                        <CButton class="w-100"
                                                :class="contactTabEd ? 'pressed_tab' : '' "
                                                @click="contactTabEd = true, TitleTabEd = false, serviceTabEd = false, doctorsTabEd = false"> Контактные данные </CButton> 
                                    </CCol>

                                    <CCol sm='3'>
                                        <CButton class="w-100"
                                                :class="TitleTabEd ? 'pressed_tab' : '' "
                                                @click="contactTabEd = false, TitleTabEd = true, serviceTabEd = false, doctorsTabEd = false"> Описание </CButton> 
                                    </CCol>

                                    <CCol sm='3'>
                                        <CButton class="w-100"
                                                :class="serviceTabEd ? 'pressed_tab' : '' "
                                                @click="contactTabEd = false, TitleTabEd = false, serviceTabEd = true, doctorsTabEd = false"> Услуги </CButton>
                                    </CCol>

                                    <CCol sm='3'>
                                        <CButton class="w-100"
                                                :class="doctorsTabEd ? 'pressed_tab' : '' "
                                                @click="contactTabEd = false, TitleTabEd= false, serviceTabEd = false, doctorsTabEd = true"> Врачи </CButton>
                                    </CCol>
                                </CRow>

                                <div v-if="contactTabEd" :key="currMedData.all_time">
                                    <CRow>
                                        <CCol sm='6'>
                                            <CInput label="Название" v-model="currMedData.name" />
                                        </CCol>

                                        <CCol sm='6'>
                                            <CInput label="Адрес" v-model="currMedData.address" />
                                        </CCol>

                                        <CCol sm='6'>
                                            <CSelect label="Район" :options="districtArray" :placeholder="districtArray[currMedData.district]" :value.sync="currMedData.district" />
                                        </CCol>
                                        <CCol sm='6' :v-bind="save_med_weekdays">
                                            <p class="m-0 mb-2">Дни работы</p>
                                            <WeekWork :save="save_med_weekdays" :medID="currMedData.id" />
                                        </CCol>

                                        <CCol sm='6'>
                                            <VuePhoneNumberInput class="mt-4" v-model="currMedData.phone" maxlength="12" default-country-code="KZ" />
                                        </CCol>

                                        <CCol sm='3' v-if="currMedData.all_time == false">
                                            <CInput label="Начало работы" v-model="currMedData.time_start" />
                                        </CCol>
                                        <CCol sm='3' v-if="currMedData.all_time == false">
                                            <CInput label="Конец работы" v-model="currMedData.time_end" />
                                        </CCol>
                                        <CCol sm='3' v-if="currMedData.all_time">
                                            <CInput label="Начало работы" placeholder="0:00" disabled/>
                                        </CCol>
                                        <CCol sm='3' v-if="currMedData.all_time">
                                            <CInput label="Конец работы" placeholder="0:00" disabled/>
                                        </CCol>

                                        <CCol sm='6' v-if="is_secondPhone == false && currMedData.phone2 == 0">
                                            <CButton class="blue__btn" style="height: 30px;" @click="is_secondPhone = true"> Добавить телефон </CButton>
                                        </CCol>

                                        <CCol sm='6' v-if="currMedData.phone2 != '' || is_secondPhone">
                                            <VuePhoneNumberInput class="mt-4" v-model="currMedData.phone2" maxlength="12" default-country-code="KZ" />
                                        </CCol>
                                        <CCol sm='6' v-if="currMedData.phone2 != '' || is_secondPhone">
                                            <CInput label="Комментарий к номеру" v-model="currMedData.phone2_comment" />
                                        </CCol>

                                        <CCol sm='6' v-if="is_secondPhone == true && is_thirdPhone == false">
                                            <CButton class="blue__btn" style="height: 30px;" @click="is_thirdPhone = true"> Добавить телефон </CButton>
                                        </CCol>

                                        <CCol sm='6' v-if="currMedData.phone3 != '' || is_thirdPhone">
                                            <VuePhoneNumberInput class="mt-4" v-model="currMedData.phone3" maxlength="12" default-country-code="KZ" />
                                        </CCol>
                                        <CCol sm='6' v-if="currMedData.phone3 != '' || is_thirdPhone">
                                            <CInput label="Комментарий к номеру" v-model="currMedData.phone3_comment" />
                                        </CCol>

                                        <CCol sm='10'>
                                            <div class="w-100"></div>
                                        </CCol>
                                        <CCol sm='2'>
                                            <CInputCheckbox :checked="currMedData.all_time" label="Круглосуточно" @click="currMedData.all_time = !currMedData.all_time"/>
                                        </CCol>

                                        <CCol sm='2'>
                                            <CCard style="border-radius: 15px; overflow:hidden; height:110px;">
                                                <img :src="currMedData.photo" style="height: 100%; object-fit:cover;">
                                            </CCard>
                                        </CCol>

                                        <CCol sm='2' v-for="i in currMedImages" :key="i.id">
                                            <CCard style="border-radius: 15px; overflow:hidden; height: 110px;">
                                                <img :src="i.image" class="" style="height:100%; object-fit:cover;">
                                                <span class="image__delete" @click="deleteImage(i.id)"> X </span>
                                            </CCard>
                                        </CCol>

                                        <CRow>
                                        <CCol sm='6'>
                                            <CInput label="Сменить титульное фото" type="file" id="img" />
                                            <CButton class="blue__btn w-50" style="height:30px;" @click.prevent="setNewImage"> Сменить </CButton>
                                        </CCol>
                                        <CCol sm='6'>
                                            <CInput label="Добавить фото" type="file" id="img_add" />
                                            <CButton class="blue__btn w-50" style="height:30px;" @click.prevent="addNewImage"> Добавить </CButton>
                                        </CCol>
                                        </CRow>

                                        <CCol sm='12' class="mt-3">
                                            <CButton class="orange__btn w-100" @click="saveMedContactTabEd"> Сохранить </CButton>
                                            <p class="mt-3" v-if="is_medContactTabSaved">Сохраненно</p>
                                        </CCol>
                                    </CRow>
                                </div>

                                <div v-if="TitleTabEd">
                                    <textarea class="w-100 form-control mt-2" style="height:300px;outline:none; box-shadow:none;" label="Описание" v-model="currMedData.text" />
                                    <CButton class="orange__btn mt-2 w-25" @click="saveMedTitleEd"> Сохранить </CButton>
                                    <p class="mt-3" v-if="is_medTextSaved">Сохраненно</p>
                                </div>

                                <div v-if="serviceTabEd">
                                    <CRow>
                                        <CCol sm='12' v-for="i in currMedServices" :key="i.id">
                                            <p> {{i.name}} </p>
                                            <p style="position:absolute;right: 20px;top:0px;"> {{i.price}} </p>
                                            <CButton @click="deleteMedService(i.id)" class="orange__btn" style="height: 25px;line-height: 15px;"> Удалить </CButton>
                                            <hr>
                                        </CCol>
                                    </CRow>
                                    <CButton @click="addServiceModal = true" class="orange__btn" style="height: 25px;line-height: 15px;"> Добавить </CButton>
                                </div>

                                <div v-if="doctorsTabEd">
                                    <div v-for="i in docOfThisMed" :key="i.pk" class="mt-3">
                                        <router-link :to="{name: 'doc', params: {id: i.pk}}">
                                            <DocCardHorz :card="i" v-if="windowWidth > 575" />
                                            <DocCard :card="i" v-if="windowWidth < 575" class="mx-auto" />
                                        </router-link>
                                        <CButton class="orange__btn" 
                                            :class="windowWidth < 575 ? 'mx-auto d-block' : '' "
                                            @click="setDeleteDoctorData(i), DeleteDoctorModal = true"> Удалить врача </CButton>
                                        <hr>
                                    </div>
                                    <CButton class="orange__btn" @click="loadDocsWithoutMeds(), AddDoctorModal = true" > Добавить врача </CButton>
                                </div>
                                
                            </CCard>


                            <CCard class="p-3" v-if="inputTab" style="min-height: 500px;">
                                <h3>Входящие заявки</h3>
                                <br>
                                <CRow>
                                    <CCol sm='2'>
                                        <p>Имя</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Услуга</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Дата записи</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Номер телефона</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Врач</p>
                                    </CCol>

                                </CRow>

                                <CCard style="background-color: #F9FAFC;
                                            padding: 1rem;">
                                <CRow v-for="i in bidsDataForCurrMed" :key="i.id">
                                    <CCol sm='2'>
                                        <p><strong> {{i.name}} </strong></p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p><strong>{{i.select}}</strong></p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p><strong>{{i.date | toDate}}</strong></p>
                                        <p><strong>{{i.date | toTime}}</strong></p>
                                    </CCol>

                                    <CCol sm='3'>
                                        <p><strong>+7 {{ i.phone }}</strong></p>
                                    </CCol>


                                    <CCol sm='2'>
                                        <p v-if="i.who != null"><strong> {{i.who.first_name}} {{i.who.last_name | toFirstLetter}}. </strong></p>
                                        <CButton class="orange__btn" v-else @click="bidIdForChangeDoc = i.id, SetDoctorModal = true">Назначить</CButton>

                                        <CButton class="blue__btn mb-2" v-if="i.who != null" @click="bidIdForChangeDoc = i.id, SetDoctorModal = true"> Сменить </CButton>
                                    </CCol>

                                    <p v-if="i.someInfo" class="ml-3">Доп коментарий: <strong>{{i.someInfo}}</strong></p>

                                    <CCol sm='12'>
                                        <CCard style="background-color: #fff;
                                                    min-height: 45px;
                                                    padding: 0.5rem;">
                                            <p v-if="i.someInfo">Доп коментарий: {{i.someInfo}} </p>
                                            <p v-else>Без комментария</p>
                                        </CCard>
                                    </CCol>
                                    
                                </CRow>
                                </CCard>
                            </CCard>


                            <CCard class="p-3 infotab" v-if="infoTab">
                                <h4>Информация</h4>

                                <CRow>
                                    <CCol sm='3'>
                                        <CButton class="w-100"
                                                :class="contactTab ? 'pressed_tab' : '' "
                                                @click="contactTab = true, serviceTab = false, doctorsTab = false, setMap()"> Контактные данные </CButton> 
                                    </CCol>

                                    <CCol sm='3'>
                                        <CButton class="w-100"
                                                :class="serviceTab ? 'pressed_tab' : '' "
                                                @click="contactTab = false, serviceTab = true, doctorsTab = false"> Услуги </CButton>
                                    </CCol>

                                    <CCol sm='3'>
                                        <CButton class="w-100"
                                                :class="doctorsTab ? 'pressed_tab' : '' "
                                                @click="contactTab = false, serviceTab = false, doctorsTab = true"> Врачи </CButton>
                                    </CCol>
                                </CRow>

                                <div v-if="contactTab" class="mt-2">
                                    <h4 style="white-space: pre-line">{{currMedData.text}}</h4>
                                    
                                    <br>
                                    <img src="/img/med/time_circle.png" width="24" height="24" class="float-left mr-2" />
                                    <p> {{currMedData.time_start | toTimeMed }} - {{currMedData.time_end | toTimeMed }} </p>

                                    <br>
                                    <img src="/img/med/call.png" width="24" height="24" class="float-left mr-2" />
                                    <p> <a :href="`tel:+7${currMedData.phone}`"> +7 {{currMedData.phone}} </a> </p>
                                    <p>Главный</p>
                                    
                                    <br v-if="currMedData.phone2 > 0">
                                    <img src="/img/med/call.png" width="24" height="24" class="float-left mr-2"  v-if="currMedData.phone2 > 0"/>
                                    <p  v-if="currMedData.phone2 > 0"> <a :href="`tel:+7${currMedData.phone2}`"> +7 {{currMedData.phone2}} </a> </p>
                                    <p v-if="currMedData.phone2_comment"> {{currMedData.phone2_comment}} </p>

                                    <br v-if="currMedData.phone3 > 0">
                                    <img src="/img/med/call.png" width="24" height="24" class="float-left mr-2"  v-if="currMedData.phone3 > 0"/>
                                    <p  v-if="currMedData.phone3 > 0"> <a :href="`tel:+7${currMedData.phone3}`"> +7 {{currMedData.phone3}} </a> </p>
                                    <p v-if="currMedData.phone3_comment"> {{currMedData.phone3_comment}} </p>

                                    <br>
                                    <img src="/img/med/location.png" width="24" height="24" class="float-left mr-2" />
                                    <p> {{currMedData.address}} </p>


                                    <CCard style="border-radius: 20px; overflow: hidden;" class="mt-3">
                                        <div id="MedMap" ref="MedMapRef" style="width:100%; height:400px"></div>
                                    </CCard>

                                </div>

                                <div v-if="serviceTab">
                                    <CRow>
                                        <CCol sm='12' v-for="i in currMedServices" :key="i.id">
                                            <p> {{i.name}} </p>
                                            <p style="position:absolute;right: 20px;top:0px;"> {{i.price}} </p>
                                            <hr>
                                        </CCol>
                                    </CRow>
                                </div>

                                <div v-if="doctorsTab">
                                    <div v-for="i in docOfThisMed" :key="i.pk" class="mt-3">
                                        <router-link :to="{name: 'doc', params: {id: i.pk}}">
                                            <DocCardHorz :card="i" v-if="windowWidth > 575" />
                                            <DocCard :card="i" v-if="windowWidth < 575" class="mx-auto" />
                                        </router-link>
                                    </div>
                                </div>
                                
                            </CCard>


                            <CCard class="p-3" v-if="endedTab" style="min-height: 500px;">
                                <h3>Завершенные заявки</h3>
                                <br>
                                <CRow>
                                    <CCol sm='2'>
                                        <p>Имя</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Услуга</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Дата записи</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Номер телефона</p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p>Врач</p>
                                    </CCol>

                                </CRow>

                                <CCard style="background-color: #F9FAFC;
                                            padding: 1rem;">
                                <CRow v-for="i in bidsDataForCurrMedCompleted" :key="i.id">
                                    <CCol sm='2'>
                                        <p><strong> {{i.name}} </strong></p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p><strong>{{i.select}}</strong></p>
                                    </CCol>

                                    <CCol sm='2'>
                                        <p><strong>{{i.date | toDate}}</strong></p>
                                        <p><strong>{{i.date | toTime}}</strong></p>
                                    </CCol>

                                    <CCol sm='3'>
                                        <p><strong>+7 {{ i.phone }}</strong></p>
                                    </CCol>


                                    <CCol sm='2'>
                                        <p v-if="i.who != null"><strong> {{i.who.first_name}} {{i.who.last_name | toFirstLetter}}. </strong></p>
                                    </CCol>

                                    <CCol sm='12'>
                                        <CCard style="background-color: #fff;
                                                    min-height: 45px;
                                                    padding: 0.5rem;">
                                            <p v-if="i.someInfo">Доп коментарий: {{i.someInfo}} </p>
                                            <p v-else>Без комментария</p>
                                        </CCard>
                                    </CCol>
                                    
                                </CRow>
                                </CCard>
                            </CCard>
                        </CCol>
                    </CRow>
                </CCol>
            </CRow>
        </div>


        <!--    Админ        -->
        <div v-if="userdata.is_admin">
            <h3>Список юзеров</h3>
            <CRow>
                <CCol sm='10'>
                    <CCard v-for="i in allUsers" :key="i.id">
                        <CRow>
                            <CCol sm='1'>
                                <img :src="i.photo" width="100%" />
                            </CCol>

                            <CCol sm='1'>
                                <p>id: {{i.id}}</p>
                                <p v-if="i.is_simpleuser"> Юзер </p>
                                <p v-else-if="i.is_doctor" style="color: green;"> Доктор</p>
                                <p v-else-if="i.is_admin" style="color: red;"> Админ </p>
                                <p v-else > Без роли </p>
                            </CCol>

                            <CCol sm='9'>
                                <p class="m-0">Дата создания: <strong>{{i.date_joined.slice(0,10)}}</strong></p>
                                <p class="m-0">Имя: <strong>{{i.first_name}} {{i.last_name}}</strong></p>
                                <p class="m-0">email: <strong>{{i.email}}</strong></p>
                            </CCol>

                            <CCol sm='1' v-if="i.is_doctor">
                                <router-link :to="{name: 'doc', params: {id: i.id}}"> К профилю </router-link>
                            </CCol>

                        </CRow>
                    </CCard>
                </CCol>
            </CRow>
        </div>



<!-- modals -->
<CModal
      title="Отзыв"
      :show.sync="ReviewModal"
      size="lg"
      :centered=true
    >
    <CRow>
        <CCol sm='8' class="mx-auto" v-if="is_created == false">
            <h3>Оцените работу врача</h3>
          <CInput v-model="review_text" placeholder="Отзыв" required > </CInput>

          <h4>Ваша оцена: {{score}}</h4>
          
          <CCol sm='8'>
              <br>
              <CRow style="position:relative; top: -10px;">
                  <CCol sm='2'>
                      <CButton class="blue__btn h-100" @click="score = 1"> 1 </CButton>
                  </CCol>

                  <CCol sm='2'>
                      <CButton class="blue__btn h-100" @click="score = 2"> 2 </CButton>
                  </CCol>

                  <CCol sm='2'>
                      <CButton class="blue__btn h-100" @click="score = 3"> 3 </CButton>
                  </CCol>

                  <CCol sm='2'>
                      <CButton class="blue__btn h-100" @click="score = 4"> 4 </CButton>
                  </CCol>

                  <CCol sm='2'>
                      <CButton class="blue__btn h-100" @click="score = 5"> 5 </CButton>
                  </CCol>
              </CRow>
          </CCol>

        </CCol>

        <CCol sm='8' class="mx-auto" v-else>
            <CCard class="orange__btn">
                <h3 class="m-auto p-1">Спасибо! Ваша заявка отправлена врачу</h3>
            </CCard>
        </CCol>
    </CRow>
    <template #footer>
        <CButton v-if="is_created == false" @click="Modal = false" class="blue__btn">Отмена</CButton>
        <CButton v-if="is_created == false" @click="setScore(score, currIdOfCompletedTask)" class="blue__btn">Отправить</CButton>
        <CButton v-if="is_created == true" @click="Modal = false" >Закрыть</CButton>
    </template>
    </CModal>

<CModal
      title="Добавить врача"
      :show.sync="AddDoctorModal"
      size="lg"
      :centered=true
    >
    <CRow>
        <CCol sm='8' class="mx-auto">
            <h3>Добавить врача</h3>

            <h4 v-if="addDoctorData">Выбран: {{addDoctorData.first_name}}</h4>
            <h4 v-else> Выбран: никто</h4>

            <CInput v-model="searchDocWithoutMed" placeholder="E-mail Врача" />

            <CRow>
                <CCol sm='12' v-for="i in filteredListDocsWithoutMed" :key="i.id">
                    <a style="cursor: pointer;" @click="setAddedDoc(i)">
                        <DocCardHorzDefault :card="i" />
                    </a>
                </CCol>
            </CRow>
            
        </CCol>
    </CRow>
    <template #footer>
        <CButton @click="AddDoctorModal = false" class="blue__btn">Отмена</CButton>
        <CButton @click="addDoctor()" class="blue__btn">Добавить</CButton>
    </template>
    </CModal>


<CModal
      title="Удалить врача"
      :show.sync="DeleteDoctorModal"
      size="md"
      :centered=true
    >
    <CRow>
        <CCol sm='8' class="mx-auto">
            <h4 v-if="show_name_of_deleted_doc">Удалить врача {{deleteDoctorData.fields.first_name}} {{deleteDoctorData.fields.last_name | toFirstLetter}}.</h4>
        </CCol>
    </CRow>

    <template #footer>
        <CButton @click="DeleteDoctorModal = false" class="blue__btn w-25">Нет</CButton>
        <CButton @click="deleteDoctor()" class="blue__btn w-25">Да</CButton>
    </template>
    </CModal>


<CModal
      title="Назначить врача"
      :show.sync="SetDoctorModal"
      size="lg"
      :centered=true
    >
    <CRow>
        <CCol sm='8' class="mx-auto">
            <h3>Назначить врача</h3>

            <h4 v-if="show_name_of_changed_doc == true">Выбран: {{changeDocInBid.fields.first_name}}</h4>
            <h4 v-else> Выбран: никто</h4>

            <CRow>
                <CCol sm='12' v-for="i in docOfThisMed" :key="i.pk">
                    <a style="cursor: pointer;" @click="setChangeDocInBid(i)">
                        <DocCardHorz :card="i" />
                    </a>
                </CCol>
            </CRow>
            
        </CCol>
    </CRow>
    <template #footer>
        <CButton @click="SetDoctorModal = false" class="blue__btn">Отмена</CButton>
        <CButton @click="setDoctor()" class="blue__btn">Назначить</CButton>
    </template>
    </CModal>


<CModal
      title="Добавить услугу"
      :show.sync="addServiceModal"
      size="lg"
      :centered=true
    >
    <CRow>
        <CCol sm='8' class="mx-auto">
            <h3>Добавить услугу</h3>

            <CInput label="Название" v-model="serviceName" />
            <CInput label="Цена" v-model="servicePrice" />
            
        </CCol>
    </CRow>
    <template #footer>
        <CButton @click="addServiceModal = false" class="blue__btn">Отмена</CButton>
        <CButton @click="addMedService" class="blue__btn">Добавить</CButton>
    </template>
    </CModal>

    </div>
</template>

<script>
import { getAPI } from '../axios-api'
import DocCardHorz from '../components/DocCardHorz.vue'
import DocCard from '../components/DocCardV2.vue'
import DocCardHorzDefault from '../components/DocCardHorzDefault.vue'
import DG from '2gis-maps'
import VuePhoneNumberInput from 'vue-phone-number-input';
import 'vue-phone-number-input/dist/vue-phone-number-input.css';

import JqxScheduler from 'jqwidgets-scripts/jqwidgets-vue/vue_jqxscheduler.vue';
import 'jqwidgets-scripts/jqwidgets/styles/jqx.base.css';
import 'jqwidgets-scripts/jqwidgets/styles/jqx.material.css';

import WeekWork from '../components/WeekWork.vue'

export default {
    components: { 
        DocCardHorz,
        DocCard,
        DocCardHorzDefault,
        VuePhoneNumberInput,
        JqxScheduler,
        WeekWork
     },
    name: 'Profile',
    data() {
        return {
                date: new jqx.date(), //new jqx.date(2016, 11, 23),
                appointmentDataFields: 
                {
                    from: 'start',
                    to: 'end',
                    id: 'id',
                    description: 'description',
                    location: 'location',
                    subject: 'subject',
                    resourceId: 'calendar'
                },
                resources:
                {
                    colorScheme: 'scheme01',
                    dataField: 'calendar',
                    source: new jqx.dataAdapter(this.source)
                },
                views:
                [
                    { type: "dayView", showWeekends: false, timeRuler: { formatString: 'HH:mm' } },
                    {
                        type: "weekView", workTime:
                        {
                            fromDayOfWeek: 0,
                            toDayOfWeek: 7,
                            fromHour: 0,
                            toHour: 24
                        },
                        timeRuler: { formatString: 'HH:mm' }
                    },
                    {type: 'monthView'}
                ],
                dataAdapter: new jqx.dataAdapter(this.source),
            userinfo: [],
            userinfo_load: false,
            userdata: [],
            currMedData: [],
            currMedImages: [],
            currMedServices: [],
            docOfThisMed: [],
            docWithoutMed: [],
            is_docs_without_med_loaded: false,
            changeDocInBid: [],
            show_name_of_changed_doc: false,
            bidIdForChangeDoc: 0,

            districtArray: ["",
                            "Ауэзовский",
                            "Медеуский", 
                            "Бостон", 
                            "Алмалинский", 
                            "Жетысуский", 
                            "Турксибский", 
                            "Алатауский", 
                            "Наурызбайский"],
            
            is_created: false,
            med_map: null,
            is_medData_loaded: false,
            is_secondPhone: false,
            is_thirdPhone: false,

            addDoctorData: [],
            deleteDoctorData: [],
            show_name_of_deleted_doc: false,
            searchDocWithoutMed: '',

            ReviewModal: false,
            AddDoctorModal: false,
            SetDoctorModal: false,
            DeleteDoctorModal: false,
            addServiceModal: false,

            serviceName: '',
            servicePrice: 0,

            first_name: '',
            last_name: '',
            position: '',
            phone: '',
            exp: 0,
            dateBirth: null,
            dayOfBirth: 0,
            monthOfBirth: 0,
            yearOfBirth: 0,
            password: '',

            save_med_weekdays: false,

            is_pass_updated: false,
            is_changesSaved: false,
            is_medTextSaved: false,
            is_medContactTabSaved: false,

            bidsData: [],
            bidsDataComplete: [],
            bidsDataForCurrMed:[],
            bidsDataForCurrMedCompleted:[],
            refreshBidTab: 0,
            refreshCompleteTab: 0,

            allUsers: [],
            completedTaskForCurrUser: [],
            review_text: '',

            score: 5,
            currIdOfCompletedTask: 0,

            optionDay: [], //[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            optionMonth: [],  //["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"],
            optionYear: [],

            infoTab: true,
            inputTab: false,
            endedTab: false,
            journalTab: false,
            contactTab: true,
            serviceTab: false,
            doctorsTab: false,

            contactTabEd: true, 
            TitleTabEd: false, 
            serviceTabEd: false, 
            doctorsTabEd: false,

            editProfileMode: false,
            changeUserPassword: false,
            windowWidth: window.innerWidth,
        }
    },
    beforeCreate: function () {      
            var user_id = localStorage.getItem('user_id')
        
            this.source =
                {
                    dataType: 'json',
                    dataFields: [
                        { name: 'id', type: 'string' },
                        { name: 'description', type: 'string' },
                        { name: 'location', type: 'string' },
                        { name: 'subject', type: 'string' },
                        { name: 'calendar', type: 'string' },
                        { name: 'start', type: 'date', format: 'yyyy-MM-ddTHH:mm:ss' },
                        { name: 'end', type: 'date', format: 'yyyy-MM-ddTHH:mm:ss' }
                    ],
                    id: 'id',
                    async: true,
                    cache: false,
                    url: `https://vetplus.kz/api/get-bid-data/${user_id}/` //generateAppointments()
                    //localdata: generateData(this.$store.state.accessToken)
                };
            this.dataAdapter = new jqx.dataAdapter(this.source);
        },
        
    methods: {
        onAppointmentChange($event) {
            console.log($event.args.appointment.originalData)

            getAPI.post(`/api/update-bid-data/`, {someInfo: $event.args.appointment.originalData.description ,
                                                  start: $event.args.appointment.originalData.start,
                                                  id: $event.args.appointment.originalData.id  })
            .catch(err => {
                console.log("error update bid in calendar: ", err);
            })
        },

        async getUserInfo() {
            await getAPI.get(`/api/user-info/`, {headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
            .then(res => {
                this.userinfo = res.data;
                this.userinfo_load = true;
            })
            .catch(err => {
                console.log('error getUserInfo: ',err);
            })
        },

        getUserData(id){
            getAPI.get(`/api/doc/${id}/`)
            .then(res => {
                this.userdata = res.data;
                //this.first_name = this.userdata.first_name;
                this.last_name = this.userdata.last_name != '' ? this.userdata.last_name : '';
                this.phone = this.userdata.phone;
                this.position = this.userdata.position;
                this.exp = this.userdata.exp;

                if(this.userdata.is_med == null && this.userdata.date_birthday != null) {
                    this.dateBirth = this.userdata.date_birthday;
                    this.dayOfBirth = this.dateBirth.slice(8,10);
                    this.monthOfBirth = this.dateBirth.slice(5,7);
                    this.yearOfBirth = this.dateBirth.slice(0,4);
                }                

                console.log('profile userdata: ', this.userdata);
            })
            .catch(err => {
                console.log("error getUserData: ", err); 
            })
        },

        getDocOfThisMed() {
            getAPI.get(`/api/get-curr-doc/${this.currMedData.id}/`)
            .then(res => {
                let data = JSON.parse(res.data);
                this.docOfThisMed = data;
            })
            .catch(err => {
                console.log("error while fetch get-curr-doc: ", err);
            })            
        },

        loadDocsWithoutMeds() {
            if(this.is_docs_without_med_loaded == false) {
                getAPI.get(`/api/doc-without-med/`)
                .then(res => {
                    this.docWithoutMed = res.data;
                    this.is_docs_without_med_loaded = true;

                    for(var i = 0; i < this.docWithoutMed.length; i++) {
                        this.docWithoutMed[i].photo = this.$store.state.base_url + '/upload/' + this.docWithoutMed[i].photo;
                    }

                    console.log("docs without meds: ", this.docWithoutMed);
                })
                .catch(err => {
                    console.log("error load docs without meds: ", err);
                })
            }
        },

        loadBidsDataForCurrMed() {

            this.bidsDataForCurrMedCompleted = [];
            this.bidsDataForCurrMed = [];

            getAPI.get(`/api/bids-curr-med/`, {headers: { Authorization: `Bearer ${this.$store.state.accessToken}` }})
            .then(res => {
                for(var i = 0; i < res.data.length; i++) {
                    if(res.data[i].is_completed) {
                        this.bidsDataForCurrMedCompleted.push(res.data[i]);
                    } else {
                        this.bidsDataForCurrMed.push(res.data[i]);
                    }
                }                
            })
            .catch(err => {
                console.log("error laod bids data for curr med: ", err);
            })
        },

        setChangeDocInBid(doctor) {
            this.changeDocInBid = doctor;
            this.show_name_of_changed_doc = true;
        },

        setAddedDoc(doctor) {
            this.addDoctorData = doctor;
        },

        addDoctor() {

            let data = {
                "medID": this.currMedData.id,
                "docID": this.addDoctorData.id
            }

            getAPI.patch(`/api/add-doc-med/`, data)
            .then(res => {
                console.log("add doctor success: ", res.data);
            })
            .catch(err => {
                console.log("error add doctor: ", err);
            })

            this.docOfThisMed = [];
            this.getDocOfThisMed();
            this.AddDoctorModal = false;
        },

        deleteDoctor() {
            
            let data = {
                "docID": this.deleteDoctorData.pk
            }

            getAPI.patch(`/api/delete-doc-med/`, data)
            .then(() => {
                this.docOfThisMed = [];
                this.getDocOfThisMed();
                this.DeleteDoctorModal = false;
            })
            .catch(err => {
                console.log("error delete doctor: ", err);
            })


        },

        setDeleteDoctorData(doctor) {
            this.deleteDoctorData = doctor;
            this.show_name_of_deleted_doc = true;
        },

        setDoctor() {
            
            //нужно передать id врача и id заявки

            //getAPI.patch(`/api/bid/${this.bidIdForChangeDoc}/`)

            let data = {
                "bidID": this.bidIdForChangeDoc,
                "docID": this.changeDocInBid.pk
            }

            getAPI.patch(`/api/change-doc-bid/`, data)
            .then(res => {
                console.log("setDoctor: ", res.data);

                //this.$router.go(0);
                this.bidsDataForCurrMed = [];
                this.loadBidsDataForCurrMed();
                this.SetDoctorModal = false;
            })
            .catch(err => {
                console.log('setDoctor error: ', err);
            })
        },

        saveChanges() {            
            let birthday = this.yearOfBirth + '-' + this.monthOfBirth + '-' + this.dayOfBirth;

            if(this.monthOfBirth == 0 || this.dayOfBirth == 0) {
                birthday = null;
            }

            if(this.first_name == '') {
                this.first_name = this.userdata.first_name
            }

            let data = {
                "first_name": this.first_name,
                "last_name": this.last_name,
                "date_birthday": birthday,
                "phone": this.phone,
                "positon": this.position
            }
            if(this.userinfo_load == true) {
                getAPI.patch(`/api/doc/${this.userinfo.id}/`, data)
                .then(res => {
                    console.log("user profile patched: ", res.data);
                    this.is_changesSaved = true;
                    this.editProfileMode = false;

                    this.getUserData(this.userinfo.id);

                    setTimeout(() => {
                        this.is_changesSaved = false;
                    }, 2000);
                })
                .catch(err => {
                    console.log("error profile patched: ", err);
                })
            }
            
        },

        saveMedTitleEd() {
            getAPI.patch(`/api/med/${this.currMedData.id}/`, {text: this.currMedData.text})
            .then(() => {
                this.is_medTextSaved = true;
                setTimeout(() => {
                    this.is_medTextSaved = false;
                }, 2000);
            })
            .catch(err => {
                console.log("error patch med text: ", err);
            })
        },

        saveMedContactTabEd() {

            if(      this.currMedData.district == '')                this.currMedData.district = 1;
            else if (this.currMedData.district == 'Ауэзовский')      this.currMedData.district = 1;
            else if (this.currMedData.district == 'Медеуский')       this.currMedData.district = 2;
            else if (this.currMedData.district == 'Бостандыкский')   this.currMedData.district = 3;
            else if (this.currMedData.district == 'Алмалинский')     this.currMedData.district = 4;
            else if (this.currMedData.district == 'Жетысуский')      this.currMedData.district = 5;
            else if (this.currMedData.district == 'Турксибский')     this.currMedData.district = 6;
            else if (this.currMedData.district == 'Алатауский')      this.currMedData.district = 7;
            else if (this.currMedData.district == 'Наурызбайский')   this.currMedData.district = 8;

            getAPI.patch(`/api/med/${this.currMedData.id}/`, { 
                name: this.currMedData.name,
                address: this.currMedData.address,
                phone: this.currMedData.phone,
                phone2: this.currMedData.phone2,
                phone2_comment: this.currMedData.phone2_comment,
                phone3_comment: this.currMedData.phone3_comment,
                phone3: this.currMedData.phone3,
                time_start: this.currMedData.time_start,
                time_end: this.currMedData.time_end,
                all_time: this.currMedData.all_time,
                district: this.currMedData.district })
            .then(() => {
                this.is_medContactTabSaved = true;
                setTimeout(() => {
                    this.is_medContactTabSaved = false;
                }, 2000);
            })
            .catch(err => {
                console.log("error patch med data: ", err);
            })

            this.save_med_weekdays = true;
        },

        setNewImage() {
            let form_data = new FormData();
            var img = document.getElementById('img').files[0];
            form_data.append('image',img,img.name);
            getAPI.post(`/api/set-new-image-med/`, form_data, {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`} } )
            .then(()=>{
                this.loadMedData(this.userinfo.is_med);
            })
            .catch(err => {
                console.log("error set new image: ", err)
            })
        },

        setNewImageUser() {
            let form_data = new FormData();
            var img = document.getElementById('img_user').files[0];
            form_data.append('image',img,img.name);
            getAPI.post(`/api/set-new-image-user/`, form_data, {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`} } )
            .then(()=>{
                this.getUserData(this.userinfo.id);
            })
            .catch(err => {
                console.log("error set new image: ", err)
            })
        },

        addNewImage() {
            let form_data = new FormData();
            var img = document.getElementById('img_add').files[0];
            form_data.append('image',img,img.name);
            getAPI.post(`/api/add-new-image-med/`, form_data, {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`} } )
            .then(()=>{
                this.loadMedData(this.userinfo.is_med);
            })
            .catch(err => {
                console.log("error add new image: ", err)
            })
        },

        deleteImage(id) {
            getAPI.delete(`/api/med-images/${id}/`)
            .then(() => {
                this.loadMedData(this.userinfo.is_med)
            })
            .catch(err => {
                console.log("error delete med image: ", err)
            })
        },

        loadBids() {
            this.bidsData = [];
            this.bidsDataComplete = [];

            getAPI.get(`/api/bid/`)
            .then(res => {
                let temp = [];
                let temp_completed = [];
                if(this.userinfo_load == true) {
                    for(var i = 0; i < res.data.length; i++){
                        if(res.data[i].who != null) {
                            if(res.data[i].who.id == this.userinfo.id) {
                                if(res.data[i].is_completed == false) {
                                    temp.push(res.data[i]);
                                } else {
                                    temp_completed.push(res.data[i]);
                                }
                            }
                        }
                         
                    }
                }

                this.bidsData = temp;
                this.bidsDataComplete = temp_completed;
            })
            .catch(err => {
                console.log("error load bids: ", err);
            })
        },

        makeComplete(id) {
            let data = {
                "is_completed": true
            }

            getAPI.patch(`/api/bid/${id}/`, data)
            .then(() => {
                console.log("bid move to complete: ", id);
                this.loadBids();
                this.refreshBidTab++;
            })
            .catch(err => {
                console.log('error move to completed: ', err);
            })

            getAPI.get(`/api/bid/${id}/`)
            .then(res => {
                if(res.data.customer != null) {
                    let completTask = {
                        "user": res.data.customer.id,
                        "bid" : res.data.id
                    }

                    getAPI.post(`/api/complete-task/`, completTask)
                    .then(() => {
                        console.log("new completet tast added to user");
                    })
                    .catch(err => {
                        console.log("error add completet task: ", err);
                    })
                }
            })
            .catch(err => {
                console.log("error get bid for completet task: ", err);
            })
        },

        makeUnComplete(id) {
            let data = {
                "is_completed": false
            }

            getAPI.patch(`/api/bid/${id}/`, data)
            .then(() => {
                console.log("bid move to bids: ", id);
                this.loadBids();
                this.refreshCompleteTab++;
            })
            .catch(err => {
                console.log('error move to bids: ', err);
            })
        },

        gotoMyPage(id) {
            this.$router.push(`/doc/${id}/`);
        },

        loadAllUsers() {
            getAPI.get(`/api/doc/`)
            .then(res => {
                this.allUsers = res.data;
            })
            .catch(err => {
                console.log("error load all users: ", err);
            })
        },

        loadCompletedTasks(id) {
            getAPI.get(`/api/completed-tasks/`)
            .then(res => {
                console.log("CT: ", res.data);
                for(var i = 0; i < res.data.length; i++) {
                    if(res.data[i].user.id == id) {
                        this.completedTaskForCurrUser.push(res.data[i]);
                    }
                }

                this.completedTaskForCurrUser.reverse();
            })
            .catch(err => {
                console.log("error loadCompletedTasks: ", err);
            })
        },

        setScore(value, id) {
            
            let currCT = [];

            for(var i = 0; i < this.completedTaskForCurrUser.length; i++) {
                if(this.completedTaskForCurrUser[i].id == id) {
                    currCT.push(this.completedTaskForCurrUser[i]);
                }
            }

            let review = `Был выполнен заказ №${currCT[0].bid.id} от ${currCT[0].bid.date}`;

            if( this.review_text != '' ) {
                review = this.review_text;
            }   

            let data = {
                    "review": review,
                    "rating": value,
                    "id": currCT[0].bid.who.id,
                    "moderate": false //true
                }

                getAPI.post(`/api/create-review/`, data, {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
                .then(res => {
                    console.log('create review ok: ', res);
                })
                .catch(error => {
                    console.log("error create review: ", error);
                })

                let CT_data = {
                    "complete": true,
                    "score": value
                }

                getAPI.patch(`/api/completed-tasks/${currCT[0].id}/`, CT_data)
                .then(() => {
                    console.log("CT patch complete");

                    let last_review_data = {
                        "moderate": false //true
                    }

                    getAPI.patch(`/api/review-last/`, last_review_data)
                    .then(() => {
                        console.log("last review published");
                    })
                    .catch(err => {
                        console.log("error published last review: ", err);
                    })
                })
                .catch(err => {
                    console.log("error ct patch: ", err);
                })

                setTimeout(() => {
                    this.$router.go(0);
                }, 150);
                
        },

        showPhone(id) {
            let data = {
                "show_phone": true
            }

            getAPI.patch(`/api/bid/${id}/`, data)
            .then(() => {
                console.log("show phone patched");

                this.loadBids();
            })
            .catch(err => {
                console.log("show phone patch error :", err);
            })
        },

        attach() {
            alert("Ты думал все так просто? :D")
        },

        changePassword() {
            let data = {
                "new_pass": this.password
            }

            getAPI.post(`/api/change-password/`, data, {headers: { Authorization: `Bearer ${this.$store.state.accessToken}` }})
            .then(() => {
                this.is_pass_updated = true;
                
                setTimeout(() => {
                    this.is_pass_updated = false;
                    this.changeUserPassword = false;
                }, 2500);
            })
            .catch(err => {
                console.log("error update pass: ", err)
            })
        },

        addMedService() {
            getAPI.post(`/api/add-new-med-service/`, {id: this.userinfo.is_med,
                                                    name: this.serviceName,
                                                    price: this.servicePrice})
            .then(() => {
                this.loadMedServices(this.userinfo.is_med);
                this.addServiceModal = false;
            })
            .catch(err => {
                console.log("error add service med: ", err)
            })
        },

        deleteMedService(id) {
            getAPI.delete(`/api/med-services/${id}/`)
            .then(() => {
                this.loadMedServices(this.userinfo.is_med);
                this.addServiceModal = false;
            })
            .catch(err => {
                console.log("error delete med service: ", err)
            })
        },

        loadMedImages(id) {
            getAPI.get(`/api/get-med-images/${id}/`)
            .then(res => {
                this.currMedImages = [];
                for(var i = 0; i < res.data.length; i++) {
                    res.data[i].image = this.$store.state.base_url + res.data[i].image;
                    this.currMedImages.push(res.data[i])
                }
            })
            .catch(err => {
                console.log("error get med images: ", err);
            })
        },

        loadMedServices(id) {
            getAPI.get(`/api/get-med-services/${id}/`)
            .then(res => {
                this.currMedServices = res.data;
            })
            .catch(err => {
                console.log("error get curr med services: ", err)
            })
        },

        loadMedData(id) {
            getAPI.get(`/api/med/${id}/`)
            .then(res => {
                this.currMedData = res.data;
                if(this.currMedData.phone2 != '') this.is_secondPhone = true;
                if(this.currMedData.phone3 != '') this.is_thirdPhone = true;

                
                this.loadMedImages(id);
                this.loadMedServices(id);

                this.is_medData_loaded = true;
            })
            .catch(err => {
                console.log("error get med data: ", err);
            })
        },

        setMap() {
            setTimeout(() => {
                this.med_map = new DG.map(this.$refs.MedMapRef, {
                center: [this.currMedData.coordX, this.currMedData.coordY],
                zoom: 16,
                minZoom: 10,
                fullscreenControl: false,
                scrollWheelZoom: false
                });

                DG.marker([this.currMedData.coordX, this.currMedData.coordY]).addTo(this.med_map); 
            }, 100);            
        },

        restartPage() {
            this.$router.go(0);
        }
    },
    mounted() {
        //this.$refs.myScheduler.ensureAppointmentVisible('id1');    
        
        this.getUserInfo();
        this.loadBids();

        for(var i = 2020; i > 1901; i--) {
            this.optionYear.push(i);
        }

        for(var i = 1; i <= 12; i++) {
            if(i == 1) this.optionMonth.push('Месяц')
            this.optionMonth.push(i);
        }

        for(var i = 1; i <= 31; i++) {
            if(i == 1) this.optionDay.push('Число')
            this.optionDay.push(i);
        }
    },
    computed: {
        b_userinfo() {
            if(this.userinfo_load) {
                return true;
            } else {
                return false;
            } 
        },

        b_medData() {
            if(this.is_medData_loaded) {
                return true;
            } else {
                return false;
            }
        },

        compiledHtml: function() {
            return this.currMedData.text;
        },

        filteredListDocsWithoutMed() {
        return this.docWithoutMed.filter(doc => {
            return doc.email.toLowerCase().includes(this.searchDocWithoutMed.toLowerCase())
        })
        }
    },
    watch: {
        b_userinfo(result){
            if(result){
                this.getUserData(this.userinfo.id);

                if(this.userinfo.is_admin) {
                    this.loadAllUsers();
                }

                if(this.userinfo.is_simpleuser) {
                    this.loadCompletedTasks(this.userinfo.id);
                }

                if(this.userinfo.is_med) {
                    this.loadMedData(this.userinfo.is_med);
                }
            }
        },

        b_medData(res) {
            if(res) {
                this.setMap();
                if(this.userinfo.is_med) {
                    this.getDocOfThisMed();
                }
            }
        }
    },
    filters: {
        toDateTime(value) {
            let str = String(value).slice(0,10);
            str += ' ';
            str += String(value).slice(11,16);
            return str;
        },

        toDate(value) {
            return String(value).slice(0,10);
        },

        toTime(value) {
            return String(value).slice(11,16);
        },

        toTimeMed(value) {
            return String(value).slice(0,5);
        },

        toFirstLetter(value) {
            return String(value).slice(0,1);
        }
    }
}
</script>

<style scoped>
hr {
    width: 100%;
    color: #ECECEC;
}

.infotab p {
    margin: 0;
    font-weight: 500;
}

.gray {
    color: #96A7AF;
}

.btn {
    border-radius: 15px;
    height: 45px;
    background-color: rgba(0,0,0,0);
    color: #A0B4C3;
    font-weight: 500;
    border: 0;
}

.btn:focus,.btn:active {
   outline: none !important;
   box-shadow: none;
}

.save__changes {
    background-color: orange;
    color: #fff;
    height: 35px;
}

.save__changes:active {
    background-color: orangered;
}

.attach {
    cursor: pointer;
    font-weight: 400;
    color: orange;
    border-bottom: 1px solid orange;
    width: 120px;
}

.pressed_tab {
    background-color: #C1E3D6;
    color: black;
    font-weight: 600;
}

.card {
    border-radius: 15px;
}

.image__delete {
    position: absolute;
    right: 5px;
    top: 5px;
    cursor: pointer;
    font-size: 10px;
    background-color: orange;
    color: white;
    border-radius: 12px;
    min-width: 16px;
    text-align: center;
}

@media screen and (min-width: 575px) {
    .btn_complete {
        background-color: orange;
        color: white;
        position:relative;
        left: -80px;
        top: -5px;
        height: 35px;
    }
}
</style>