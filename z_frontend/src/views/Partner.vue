<template>
<div>
    <div :class="windowWidth > 575 ? 'mt-5 px-5' : 'mt-5 px-3' ">

        <CRow>
            <CCol md='10' class="mx-auto">
                <CRow>
                    

                    <CCol sm='6'>
                        <img src="/img/partner/partner.svg" width="100%" />
                    </CCol>

                    <CCol sm='6'>
                        <h1 class="mt-5"> <span style="color: orange;">Вет плюс</span> - система автоматизации вашего бизнеса </h1>
                        <CButton v-if="windowWidth > 575" @click="scroll(1234567)" class="orange__btn" style="border-radius: 15px; width: 250px;"> Оставить заявку </CButton>
                    </CCol>

                    <CCol sm='12' v-if="windowWidth < 575">
                        <CButton @click="scroll(1234567)" class="orange__btn w-100" style="border-radius: 15px; width: 250px;"> Оставить заявку </CButton>
                    </CCol>
                </CRow>
            </CCol>

            <!--
            <CCol sm='12' class="mt-5">
                <img src="/img/partner/11.svg" width="90%" class="mx-auto d-block" />
            </CCol>
            -->
        </CRow>

        <CRow class="mt-5">
            <CCol sm='10' class="mx-auto">
                <CRow>
                    <CCol sm='6'>
                        <h2>Сотрудничая с нами, <span style="color: orange;">вы получаете</span> </h2>
                        <li>Многократный рост записей</li>
                        <li>Повышение репутации вашей клиники/ваших профессиональных навыков</li>
                        <li>Выгода, запись от платформы в разы дешевле контекстной рекламы</li>
                        <li>Удобный сервис в использовании, идет навстречу специалистам/клиникам и адаптируется под их задачи и цели</li>
                        <br><br>
                        <CButton v-if="windowWidth > 575" @click="scroll(1234567)" class="orange__btn" style="border-radius: 15px; width: 250px;"> Оставить заявку </CButton>
                    </CCol>

                    <CCol sm='6'>
                        <CRow>
                            <CCol sm='3'>
                                <CCard class="card__part">
                                    <img src="/img/partner/auto.svg" width="100" height="100" />
                                    <p class="main__text">Автоматизация бизнес процессов</p>
                                    <p class="second__text">Абсолютно все процессы вашего бизнеса будут автоматизированы</p>
                                </CCard>
                            </CCol>

                            <CCol sm='3'>
                                <CCard class="card__part"
                                        style="position: relative; top: -10px;">
                                    <img src="/img/partner/third_party.svg" width="100" height="100" />
                                    <p class="main__text">Больше постоянных клиентов</p>
                                    <p class="second__text">Теперь клиенты могут записаться к Вам онлайн в режиме 24/7</p>
                                </CCard>
                            </CCol>

                            <CCol sm='3'>
                                <CCard class="card__part">
                                    <img src="/img/partner/bar_chart.svg" width="100" height="100" />
                                    <p class="main__text">Сокращение неявок</p>
                                    <p class="second__text">Система будет блокировать несерьезных клиентов, которых слишком часто отменяют запись</p>
                                </CCard>
                            </CCol>

                            <CCol sm='3'>
                                <CCard class="card__part"
                                        style="position: relative; top: -10px;">
                                    <img src="/img/partner/value_chain.svg" width="100" height="100" />
                                    <p class="main__text">Больше постоянных клиентов</p>
                                    <p class="second__text">Вы будете точно знать, какая выручка у вашей компании сегодня, за неделю, за месяц</p>
                                </CCard>
                            </CCol>

                            <CCol sm='12' v-if="windowWidth < 575">
                                <CButton @click="scroll(1234567)" class="orange__btn w-100" style="border-radius: 15px; width: 250px;"> Оставить заявку </CButton>
                            </CCol>

                        </CRow>
                    </CCol>
                </CRow>
            </CCol>
        </CRow>
    </div>

    <div v-if="windowWidth > 575" style="background-color: #fff;
                    width: 100%;">
        <CRow>
            <CCol sm='10' class="mx-auto">
                <CRow> 
                    <CCol sm='6'>
                        <img src="/img/partner/team.svg" />
                    </CCol>

                    <CCol sm='6'>
                        <h2>Команда <span style="color: orange;">Вет Плюс</span> </h2>
                        <p>Быстроразвивающийся и постоянно совершенствующийся портал поиска 
                            ветеринарных услуг с отличной командой сотрудников. 
                            Наши менеджеры С радостью ответит на все ваши вопросы, 
                            решит технические проблемы и дадут персональные рекомендации для вашей 
                            страницы</p>
                    </CCol>
                </CRow>
            </CCol>
        </CRow>
        </div>

        <div v-if="windowWidth < 575" class="px-3" style="background-color: #fff; width: 100%;">
            <CRow>
                <CCol sm='12'>
                    <h2>Команда <span style="color: orange;">Вет Плюс</span> </h2>
                    <p>Быстроразвивающийся и постоянно совершенствующийся портал поиска 
                        ветеринарных услуг с отличной командой сотрудников. 
                        Наши менеджеры С радостью ответит на все ваши вопросы, 
                        решит технические проблемы и дадут персональные рекомендации для вашей 
                        страницы</p>
                </CCol>
                <CCol sm='12'>
                    <img src="/img/partner/team.svg" class="w-100" />
                </CCol>
            </CRow>
        </div>


        <CRow v-if="windowWidth > 575">
            <CCol sm='10' class="mx-auto">
                <CRow>
                    <CCol sm='6'>
                        <h2>Мы предлагаем <span style="color: orange;">Вам</span> </h2>        
                    </CCol>

                    <CCol sm='3'>
                        <CCard class="card__horz_uno">
                            <img src="/img/partner/1.svg" style="width: 33px;height:125px;" />
                            <p>Предоставляем вам CRM-систему</p>
                        </CCard>
                    </CCol>

                    <CCol sm='3'>
                        <CCard class="card__horz_dos">
                            <img src="/img/partner/2.svg" />
                            <p>Увеличение потока пациентов</p>
                        </CCard>
                    </CCol>

                    <CCol sm='3'>
                        <div class="w-100"></div>
                    </CCol>

                    <CCol sm='3'>
                        <CCard class="card__horz_uno">
                            <img src="/img/partner/3.svg" />
                            <p>Постоянный доступ к Личному кабинету с информацией о входящих заявках</p>
                        </CCard>
                    </CCol>

                    <CCol sm='3'>
                        <CCard class="card__horz_dos">
                            <img src="/img/partner/4.svg" />
                            <p>Создание положительного имиджа</p>
                        </CCard>
                    </CCol>

                    <CCol sm='3'>
                        <CCard class="card__horz_uno">
                            <img src="/img/partner/5.svg" />
                            <p>Самостоятельная актуализация информации в личном кабинете врача</p>
                        </CCard>
                    </CCol>

                </CRow>
            </CCol>
        </CRow>

        <div v-if="windowWidth < 575" class="px-3">
            <CRow>
                <CCol sm='12' class="text-center">
                    <h2>Мы предлагаем <span style="color: orange;">Вам</span> </h2>
                </CCol>

                <CCol sm='12'>
                    <CCard class="card__horz_uno">
                        <img src="/img/partner/1.svg" style="width: 33px;height:125px;" />
                        <p>Предоставляем вам CRM-систему</p>
                    </CCard>
                </CCol>

                <CCol sm='12'>
                    <CCard class="card__horz_dos" :style=" `position:relative; left: calc(${windowWidth}px - 300px - 20px);` ">
                        <img src="/img/partner/2.svg" />
                        <p>Увеличение потока пациентов</p>
                    </CCard>
                </CCol>

                <CCol sm='12'>
                    <div class="w-100"></div>
                </CCol>

                <CCol sm='12'>
                    <CCard class="card__horz_uno">
                        <img src="/img/partner/3.svg" />
                        <p>Постоянный доступ к Личному кабинету с информацией о входящих заявках</p>
                    </CCard>
                </CCol>

                <CCol sm='12'>
                    <CCard class="card__horz_dos" :style=" `position:relative; left: calc(${windowWidth}px - 300px - 20px);` ">
                        <img src="/img/partner/4.svg" />
                        <p>Создание положительного имиджа</p>
                    </CCard>
                </CCol>

                <CCol sm='12'>
                    <CCard class="card__horz_uno">
                        <img src="/img/partner/5.svg" />
                        <p>Самостоятельная актуализация информации в личном кабинете врача</p>
                    </CCard>
                </CCol>
            </CRow>
        </div>


        <div v-if="windowWidth > 575" style="background-color: #fff;
                    width: 100%;"
            class="mb-5">

            <CRow>
                <CCol sm='12' v-if="done == false">
                    <h2 class="text-center">Оставить заявку</h2>
                </CCol>
                <CCol sm='12' v-if="done == false">
                    <p class="text-center mx-auto" style="width: 495px;">Если вы заинтересованы в сотрудничестве с нами, 
оставьте заявку и мы обязательно свяжемся с Вами!</p>
                </CCol>

                <CCol sm='10' class="mx-auto">
                    <CRow v-if="done == false">
                        <CCol sm='3'>
                            <CInput class="test" placeholder="Имя" v-model="name" />
                        </CCol>
                        <CCol sm='3'>
                            <CInput placeholder="Номер телефона" v-model="phone" maxlength="10" />
                        </CCol>
                        <CCol sm='3'>
                            <CInput placeholder="Ваш e-mail" v-model="email" />
                        </CCol>
                        <CCol sm='3'>
                            <CButton class="orange__btn w-100" @click="savePartnerBid"> Отправить заявку </CButton>
                        </CCol>
                    </CRow>
                    <CRow v-else>
                        <CCol sm='12'>
                            <p class="done">Спасибо за Вашу заявку, мы расмотрим её в ближайшее время и свяжемся с Вами</p>
                        </CCol> 
                    </CRow>
                    <p v-if="phoneLenErr">Не правильно указан номер</p>
                    <p v-if="phoneErr">Поле номер не должно быть пустым</p>
                    <p v-if="nameErr">Поле имя не должно быть пустым</p>
                    <p v-if="emailErr">Поле e-mail не должно быть пустым</p>

                </CCol>

            </CRow>


        </div>

        <div v-if="windowWidth < 575" style="background-color: #fff; width: 100%;" class="px-3 mb-5">
            <CRow>
                <CCol sm='12' v-if="done == false">
                    <h2 class="text-center">Оставить заявку</h2>
                </CCol>
                <CCol sm='12' v-if="done == false">
                    <p class="text-center">Если вы заинтересованы в сотрудничестве с нами, 
оставьте заявку и мы обязательно свяжемся с Вами!</p>
                </CCol>

                <CCol sm='12' class="px-3">
                    <CRow v-if="done == false">
                        <CCol sm='12'>
                            <CInput class="test" placeholder="Имя" v-model="name" />
                        </CCol>
                        <CCol sm='12'>
                            <VuePhoneNumberInput placeholder="123" v-model="phone" default-country-code="KZ" maxlength="12" class="mb-3" />
                        </CCol>
                        <CCol sm='12'>
                            <CInput placeholder="Ваш e-mail" v-model="email" />
                        </CCol>
                        <CCol sm='12'>
                            <CButton class="orange__btn w-100" @click="savePartnerBid"> Отправить заявку </CButton>
                        </CCol>
                    </CRow>
                    <CRow v-else>
                        <CCol sm='12'>
                            <p class="done">Спасибо за Вашу заявку, мы расмотрим её в ближайшее время и свяжемся с Вами</p>
                        </CCol> 
                    </CRow>
                    <p v-if="phoneLenErr">Не правильно указан номер</p>
                    <p v-if="phoneErr">Поле номер не должно быть пустым</p>
                    <p v-if="nameErr">Поле имя не должно быть пустым</p>
                    <p v-if="emailErr">Поле e-mail не должно быть пустым</p>

                </CCol>

            </CRow>
        </div>

        
</div>
</template>

<script>
import { getAPI } from '../axios-api';
import VuePhoneNumberInput from 'vue-phone-number-input';
import 'vue-phone-number-input/dist/vue-phone-number-input.css';
export default {
    name: "Partner",
    components: {
        VuePhoneNumberInput
    },
    data() {
        return {
            name: '',
            phone: '',
            email: '',

            nameErr: false,
            phoneErr: false,
            phoneLenErr: false,
            emailErr: false,

            done: false,

            windowWidth: window.innerWidth
        }
    },
    methods: {
        async scroll(offset){
            window.scrollTo({
                top: offset,
                behavior: 'smooth'
            });
        },

        savePartnerBid() {
            if(this.name == '') this.nameErr = true;
            if(this.phone == '') this.phoneErr = true;
            if(this.email == '') this.emailErr = true;

            for( var i = 0; i < this.phone.length; i++ ) {
                if(this.phone.charAt(i) >= '0' && this.phone.charAt(i) <= '9') {
                    //vse ok
                } else {
                    this.phoneLenErr = true;
                }
            }

            if(this.phone.length != 10) {
                this.phoneLenErr = true;
            }

            if(this.nameErr == false && this.phoneErr == false && this.emailErr == false && this.phoneLenErr == false) {
                getAPI.post(`/api/partner-bid/`, {name: this.name, phone: this.phone, email: this.email})
                .catch(err => {
                    console.log("error partner bid: ", err);
                })

                this.done = true;
            }
        }
    },
    computed: {
        b_refreshErrors() {
            if( this.nameErr || this.phoneErr || this.emailErr || this.phoneLenErr ) {
                return true;
            } else {
                return false;
            }
        }
    },
    watch: {
        b_refreshErrors(res) {
            if(res) {
                setTimeout(() => {
                    this.nameErr = false;
                    this.phoneErr = false;
                    this.emailErr = false;
                    this.phoneLenErr = false;
                }, 3000);
            }
        }
    },
}
</script>

<style scoped>
.test, .test:active, .test:focus {
    outline: none !important;
    box-shadow: none !important;
}

h1 {
    font-size: 48px;
    font-weight: 700;
    color: #000;
}

h2 {
    padding-top: 70px;
    font-size: 40px;
    font-weight: 600;
}

p {
    font-size: 20px; 
    font-weight: 400;
}

li {
    font-size: 20px;
    font-weight: 500;
}

.done {
    text-align: center;
    font-size: 22px;
}

.card__part {
    width: 241px;
    height: 290px;
    border-radius: 10px;
    box-shadow: 0 8px 8px 0 #00000010;
    padding: 30px 15px;
}

.card__part img {
    margin: 0 auto;
}

.card__part .main__text {
    text-align: center;
    font-size: 18px;
    font-weight: 600;
}

.card__part .second__text {
    color: #96A7AF;
    text-align: center;
    font-size: 14px;

}

.card__horz_uno, .card__horz_dos {
    width: 300px;
    height: 146px;
    border-radius: 10px;
    box-shadow: 0 18px 18px 0 #00000010;
    border: 0;
}

.card__horz_dos {
    box-shadow: none;
    background-color: #00000000;
}

.card__horz_uno img, .card__horz_dos img {
    width: 41px;
    height: 125px;
    margin-left: 0.6rem;
}

.card__horz_uno p, .card__horz_dos p {
    position: absolute;
    left: 60px;
    top: 40px;
    font-size: 18px;
}

.col-sm-3 {
    min-width: 250px;
}


@media screen and (max-width: 575px) {
    h1 {
        font-size: 40px;
    }

    .col-sm-3 {
        min-width: 0;
        max-width: 190px;
    }

    .card__part {
        width: 185px;
        height: 350px;
    }
}

</style>