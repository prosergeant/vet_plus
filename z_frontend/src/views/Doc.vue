<template>
<div class="mt-5">
    <CRow>
        <CCol md='8' class="mx-auto">
            <h3 class="border-shmorder-50 ml-2">Специалисты</h3>
            <CRow>
                <CCol md='5'>
                    <img :src="currDocData.photo" style="min-height: 397px; border-radius:15px; object-fit:cover;" :class="windowWidth < 575 ? 'w-75 mx-auto d-block' : 'w-100' " /> 
                </CCol>

                <CCol md='7'>
                    <CCard class="p-3 infotab">
                        <h4> {{currDocData.first_name}} {{currDocData.last_name}} </h4>
                        <br>
                        <p class="gray">Должность</p>
                        <p> {{currDocData.position}} </p>
                        <br>
                        <p class="gray">Стаж работы по специальности</p>
                        <p>Более {{currDocData.exp}} лет</p>
                        <br>
                        <p class="gray">Место работы</p>
                        <p v-if="currDocData.med == null">Частный врач</p>
                        <p v-else> <router-link :to="{name: 'med', params: {id: currDocData.med.id}}"> {{currDocData.med.name}} </router-link></p>
                        <br>
                        <p class="gray">Время приема</p>
                        <p> {{currDocData.time_start}} - {{currDocData.time_end}} </p>
                        <br>
                        <CRow>
                            <CCol sm='12'>
                                <img src="/img/phone.png" v-if="showPhone" width="20" height="20" class="float-left mr-3"/>
                                <p style="color: orange; width: 200px;" v-if="showPhone"> +7 {{currDocData.phone}} </p>
                                <p class="show__phone" @click="plusNumPhoneSee" v-if="showPhone == false">Показать номер</p>
                            </CCol>
                        </CRow>
                        <br>
                        <p class="gray">Образование</p>

                        <CButton class="orange__btn" style="border-radius: 15px;" @click="Modal = true"> Записаться на прием </CButton>
                    </CCard>
                </CCol>

                    <CCol sm='11' class="mx-auto">
                        <CCard class="p-3">
                            

                            <CCard v-if="is_review_created == false">
                                <p class="text-center pt-2">Оставьте отзыв</p>
                                <p v-if="reviewErr" class="text-center pt-2">Поле отзыва не должно быть пустым</p>
                                <p v-if="authErr" class="text-center pt-2">Чтобы оставить отзыв необходимо авторизоваться</p>
                                <CInput class="px-2" placeholder="Введите ваш отзыв" v-model="ratingReviewModel" @keyup.enter="createReview" />
                                <StarRating v-model="selectOption" :star-size="30" :show-rating="false" class="mb-3" />
                                <!--
                                <CSelect class="px-2"
                                    :options="ratingOptions"
                                    v-model="selectOption"
                                    :value.sync="selectOption" /> -->
                                <CButton class="orange__btn" @click="createReview"> Отправить </CButton>
                            </CCard>

                            <CCard v-else style="background-color: #2eb85c; color: #fff;">
                                <h3 class="m-auto p-1 text-center">Спасибо! Ваш отзыв отправлен на модерацию</h3>
                            </CCard>

                            <CButton style="border-radius: 15px;
                                            width: 230px;" 
                                    class="mx-auto orange__btn"
                                    v-if="showReviews == false"
                                    @click="showReviews = true"> Показать отзывы </CButton>

                            <div v-if="showReviews">
                            <CCard v-for="i in reviewData" :key="i.id" class="card__review">
                                <p class="ml-2">{{i.author.email}}</p>  
                                <p class="ml-2">{{i.review}}</p>
                                <StarRating class="medcard__rating" :read-only="true" v-model="i.rating" :star-size="20" :show-rating="false" />
                            </CCard>
                            </div>
                        </CCard>
                    </CCol>
            </CRow>
        </CCol>
    </CRow>



<!-- modals -->
    <CModal
      title="Заявка"
      :show.sync="Modal"
      size="lg"
      :centered=true
    >
    <CRow>
        <CCol sm='8' class="mx-auto" v-if="is_created == false">
          <CInput v-model="name" placeholder="Ваше имя" required @keyup.enter="createBid()"> </CInput>
          <VuePhoneNumberInput class="mb-3" v-model="phone" default-country-code="KZ" maxlength="12" />
          
          <CSelect
                  
                  :options="currMedServicesNames"
                  v-model="select"
                  :value.sync="select"
                />

            <CInput v-model="someInfo" placeholder="Доп информация, не обязательное поле" />
        </CCol>

        <CCol sm='8' class="mx-auto" v-else>
            <CCard class="orange__btn">
                <h3 class="m-auto p-1 text-center">Спасибо! Ваша заявка отправлена врачу</h3>
            </CCard>
        </CCol>
    </CRow>
    <template #footer>
        <CButton v-if="is_created == false" @click="Modal = false" class="orange__btn">Отмена</CButton>
        <CButton v-if="is_created == false" @click="createBid()" class="orange__btn">Записаться</CButton>
        <CButton v-if="is_created == true" @click="Modal = false" class="orange__btn">Закрыть</CButton>
    </template>
    </CModal>


</div>
</template>

<script>
import { getAPI } from '../axios-api'
import serviceData from '../servicedata'
import StarRating from 'vue-star-rating'
import VuePhoneNumberInput from 'vue-phone-number-input';
import 'vue-phone-number-input/dist/vue-phone-number-input.css';

export default {
    name: "Doc",
    components: {
        StarRating,
        VuePhoneNumberInput
    },
    data() {
        return {
            currDocData: [],
            showPhone: false,
            dataIsLoaded: false,
            id: this.$route.params.id,
            is_open: null,
            Modal: false,
            medOptions: serviceData, //[1,2,3]
            medOptionsClear: ['Выберите услугу'],
            currMedServices: [],
            currMedServicesNames: [],

            ratingOptions: [1,2,3,4,5],
            selectOption: 5,
            ratingReviewModel: null,
            is_review_created: false,
            reviewErr: false,
            authErr: false,
            phoneLenErr: false,
            reviewData: [],
            showReviews: false,

            name: '',
            phone: '',
            select: 'Выберите услугу',
            is_created: false,
            someInfo: null,
            is_auth: this.$store.state.is_auth,
            userInfo: [],
            userID: 0,

            windowWidth: window.innerWidth,
        }
    },
    computed: {
        compiledHtml()
        {
            return this.currDocData.text;
        },
        b_dataIsLoaded() {
            if(this.dataIsLoaded){
                return true;
            } else {
                return false;
            }
        },

        b_refreshErrors() {
            if( this.reviewErr || this.authErr || this.phoneLenErr ) {
                return true;
            } else {
                return false;
            }
        }
    },
    methods: {
        fetchUserInfo() {
            if(this.is_auth) {
                getAPI.get(`/api/user-info/`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
                .then(res => {
                    this.userInfo = res.data;
                    this.name = this.userInfo.name;
                    this.phone = this.userInfo.phone;
                    this.userID = this.userInfo.id;
                })
                .catch(err => {
                    console.log("error get user info: ", err);
                })
            }
            
        },

        fetchCurrDocData() {
            getAPI.get(`/api/doc/${this.$route.params.id}/`)
            .then(res => {
                this.currDocData = res.data;
                this.currDocData.rating.toFixed(2);
                this.dataIsLoaded = true;

                let medID = this.currDocData.med.id;
                if(medID != null || medID != '') {
                    this.loadMedServices(medID);
                }
            })
            .catch(err => {
                console.log("error fetch curr doc data: ", err);
            })
        },

        getIsOpen() {
            const today = new Date();
            const time = today.getHours();
            const str = this.currDocData.time_end;
            const time_end = str.slice(0,2);
            const time_start = this.currDocData.time_start.slice(0,2);
            let b_is_open = false;
            if(time <= parseInt(time_end) && time >= parseInt(time_start)) b_is_open = true;
            this.is_open = b_is_open  ? "Открыто" : "Закрыто";
        },

        loadMedServices(id) {
            getAPI.get(`/api/get-med-services/${id}/`)
            .then(res => {
                this.currMedServices = res.data;

                for(var i = 0; i < this.currMedServices.length; i++) {
                    this.currMedServicesNames.push(this.currMedServices[i].name);
                }
            })
            .catch(err => {
                console.log("error get curr med services: ", err)
            })
        },

        createBid(){

            this.phoneLenErr = false;

            /*
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
            */

            if(this.phoneLenErr == false) {

                let medID = -1;
                if(this.currDocData.med != null) medID = this.currDocData.med.id;

                let data = {
                    "name"    : this.name,
                    "phone"   : this.phone,
                    "select"  : this.select,
                    "id"      : this.$route.params.id,
                    "someInfo": this.someInfo,
                    "customerID": this.userID,
                    "in_med_center": false,
                    "medCenter": medID //this.currDocData.med.id
                }

                getAPI.post(`/api/create-bid/`, data)
                .then(res => {
                    console.log('create bid ok: ', res);
                    this.is_created = true;
                })
                .catch(err => {
                    console.log('error create bid: ', err);
                })
            }
        },

        createReview() {

            this.reviewErr = false;

            if(!this.ratingReviewModel) {
                this.reviewErr = true;
            } else {

                let data = {
                    "review": this.ratingReviewModel,
                    "rating": this.selectOption,
                    "id": this.$route.params.id
                }

                getAPI.post(`/api/create-review/`, data, {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
                .then(res => {
                    console.log('create review ok: ', res);
                    //this.is_created = true;
                    this.is_review_created = true;
                })
                .catch((error) => {
                    if(error.response) {
                        console.log('error create review: ', error);
                        console.log(error.response.data);
                        console.log(error.response.status);
                        console.log(error.response.headers);

                        if(error.response.status == 401) {
                            this.authErr = true;
                        }
                    }

                    
                })

            }
        },

        fetchReviewData() {
            getAPI.get(`/api/review/`)
            .then(res => {
                for(var i = 0; i < res.data.length; i++){
                    if(res.data[i].moderate && res.data[i].doctor.id == this.$route.params.id) {
                        this.reviewData.push(res.data[i]);
                    }
                }
                console.log("reviewData: ", this.reviewData);
            })
            .catch(err => {
                console.log("error fetch review data: ", err);
            })
        },

        plusNumPhoneSee() {
            this.showPhone = true;
            let n = this.currDocData.num_phone_see;
            n++;

            let data = {
                "num_phone_see": n
            }

            getAPI.patch(`/api/doc/${this.$route.params.id}/`, data)
            .then(() => {
                console.log("num_phone_see++");
            })
            .catch(err => {
                console.log("error num_phone_see++: ", err);
            })

        },

        medViewsPlus() {
            if(this.currDocData.med != null) {
                let medId = this.currDocData.med.id;
            
                getAPI.get(`/api/med/${medId}/`)
                .then(res => {
                    let newViews = res.data.views + 1;

                    let data = {
                        "views": newViews
                    }

                    getAPI.patch(`/api/med/${medId}/`, data)
                    .then(() => {
                        console.log("med views ++");
                    })
                    .catch(err => {
                        console.log("error med views++: ", err);
                    })
                })
                .catch(err => {
                    console.log("error load med data: ", err);
                })

                getAPI.get(`/api/doc/${this.currDocData.id}/`)
                .then(res => {
                    let newViews = res.data.num_page_see + 1;

                    let data = {
                        "num_page_see": newViews
                    }

                    getAPI.patch(`/api/doc/${this.currDocData.id}/`, data)
                    .then(() => {
                        console.log("doc views ++");
                    })
                    .catch(err => {
                        console.log("error doc views++: ", err);
                    })
                })
                .catch(err => {
                    console.log("error load doc data: ", err);
                })
            }
            
        },

        onResize() {
            this.windowWidth = window.innerWidth;
        },
    },
    mounted() {
        this.fetchCurrDocData();
        this.fetchReviewData();

        this.$nextTick(() => {
            window.addEventListener('resize', this.onResize);
        })
    },
    beforeDestroy() { 
        window.removeEventListener('resize', this.onResize); 
    },
    watch: {
        b_dataIsLoaded(res){
            if(res){
                this.getIsOpen();
                this.medViewsPlus();
                this.fetchUserInfo();
            }
        },

        b_refreshErrors(res) {
            if(res) {
                setTimeout(() => {
                    this.reviewErr = false;
                    this.authErr = false;
                    this.phoneLenErr = false;
                }, 3000);
            }
        }
    },
    filters: {
        max_digits(amount) {
            const amt = Number(amount)
            return amt && amt.toLocaleString(undefined, {maximumFractionDigits:2}) || '0'
        },

        onlyHM (value) {
            return String(value).slice(0, 5);
        },

        oneDecimal: function (value) {
            return value.toFixed(1)
        },
        noDecimal(value) {
            return Math.floor(value);  
        },
        toStars: function (value) {
            let result = ''
            while(result.length < value) {
                result+='★' 
            }
            return result
        },
    }
}
</script>

<style scoped>
.success {
    background-color: forestgreen;
    color: white;
}

.show__phone {
    color: orange;
    width: 120px;
    position: relative;
    left: 10px;
    border-bottom: 1px dashed orange;
}

.show__phone:hover {
    cursor: pointer;
}

.border-shmorder-50 {
    position: relative;
    display: inline-block;
    font-size: 200%;
    font-weight: 500;
    margin-bottom: 2rem;
}

.border-shmorder-50::after {
    content:"";
    position:absolute;
    bottom:-5px;
    width:50%;
    height:4px;
    margin-left:-100%;
    background: #FF8A34;
}

.infotab p {
    margin: 0;
    font-weight: 600;
}

.gray {
    color: #96A7AF;
}

.card {
    border: none;
}

.card__review {
    box-shadow: 0 4px 4px 0 rgba(0,0,0,0.2);
    border-radius: 15px;
}


.medcard__rating {
  position: absolute;
  top: 5px;
  right: 15px;
  font-size: 21px;
}

.medcard__stars--active {
  color: orange;
}
.medcard__stars--inactive {
  color: #CCCCCC;
}
</style>