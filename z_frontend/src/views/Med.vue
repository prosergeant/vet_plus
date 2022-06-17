<template>
<div class="mt-5">
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

                            <CCol sm='2' v-for="i in currMedImages" :key="i.id" class="mx-auto">
                                <CCard style="border-radius: 15px; overflow:hidden; height: 50px; width:50px;">
                                    <img v-img :src="i.image" class="" style="height:100%; object-fit:cover;">
                                </CCard>
                            </CCol>

                            <CCol sm='10' class="mx-auto my-3" v-if="currMedData.this_is == 1 || currMedData.this_is == 4 || currMedData.this_is == 5">
                                <CButton class="w-100" style="color: white; background-color: #FF8A34;" @click="editTab = true, infoTab = false"> Оставить заявку </CButton>
                            </CCol>

                            <CCol sm='12'>
                                <div class="w-100">
                                    <span style="visibility:hidden;"> invis </span>
                                </div>
                            </CCol>

                            <CCol sm='10' class="mx-auto my-1" v-if="currMedData.this_is == 1 || currMedData.this_is == 4 || currMedData.this_is == 5">
                                <CButton
                                class="w-100" 
                                :class="infoTab ? 'pressed_tab' : '' "
                                @click="editTab = false, infoTab = true, setMap()"> Информация </CButton>
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
                        <h4>Информация</h4>

                        <CRow>
                            <CCol sm='3'>
                                <CButton class="w-100" :style="currMedData.this_is == 2 || currMedData.this_is == 3 ? 'cursor:auto;' : '' "
                                        :class="contactTab ? 'pressed_tab' : '' "
                                        @click="contactTab = true, serviceTab = false, doctorsTab = false, setMap()"> Контактные данные </CButton>
                            </CCol>

                            <CCol sm='3' v-if="currMedData.this_is == 1 || currMedData.this_is == 4 || currMedData.this_is == 5">
                                <CButton class="w-100"
                                        :class="serviceTab ? 'pressed_tab' : '' "
                                        @click="contactTab = false, serviceTab = true, doctorsTab = false"> Услуги </CButton>
                            </CCol>

                            <CCol sm='3' v-if="currMedData.this_is == 1 || currMedData.this_is == 4 || currMedData.this_is == 5">
                                <CButton class="w-100"
                                        :class="doctorsTab ? 'pressed_tab' : '' "
                                        @click="contactTab = false, serviceTab = false, doctorsTab = true"> Врачи </CButton>
                            </CCol>
                        </CRow>

                        <div v-if="contactTab" class="mt-2">
                            <h4 style="white-space: pre-line">{{currMedData.text}}</h4>
                            
                            <br>
                            <img src="/img/med/time_circle.png" width="24" height="24" class="float-left mr-2" />
                            <p> {{currMedData.time_start | toTime}} - {{currMedData.time_end | toTime}} </p>

                            <br>
                            <img src="/img/med/call.png" width="24" height="24" class="float-left mr-2" />
                            <p v-if="showPhone"> <a :href="`tel:+7${currMedData.phone}`"> +7 {{currMedData.phone}} </a> </p>
                            <p class="show__phone" @click="showPhone = true, plusNumPhoneSee()" v-if="showPhone == false">Показать номер</p>
                            <p>Главный</p>
                            
                            <br v-if="currMedData.phone2 > 0">
                            <img src="/img/med/call.png" width="24" height="24" class="float-left mr-2"  v-if="currMedData.phone2 > 0"/>
                            <p  v-if="currMedData.phone2 > 0 && showPhone2"> <a :href="`tel:+7${currMedData.phone2}`"> +7 {{currMedData.phone2}} </a> </p>
                            <p class="show__phone" @click="showPhone2 = true, plusNumPhoneSee()" v-if="currMedData.phone2 > 0 && showPhone2 == false">Показать номер</p>
                            <p v-if="currMedData.phone2_comment"> {{currMedData.phone2_comment}} </p>

                            <br v-if="currMedData.phone3 > 0">
                            <img src="/img/med/call.png" width="24" height="24" class="float-left mr-2"  v-if="currMedData.phone3 > 0"/>
                            <p  v-if="currMedData.phone3 > 0 && showPhone3"> <a :href="`tel:+7${currMedData.phone3}`"> +7 {{currMedData.phone3}} </a> </p>
                            <p class="show__phone" @click="showPhone3 = true, plusNumPhoneSee()" v-if="currMedData.phone3 > 0 && showPhone3 == false">Показать номер</p>
                            <p v-if="currMedData.phone3_comment"> {{currMedData.phone3_comment}} </p>

                            <br>
                            <img src="/img/med/location.png" width="24" height="24" class="float-left mr-2" />
                            <p> {{currMedData.address}} </p>


                            <CCard style="border-radius: 20px; overflow: hidden;" class="mt-3">
                                <div id="map" style="width:100%; height:400px"></div>
                            </CCard>

                        </div>

                        <div v-if="serviceTab">
                            <div v-for="i in currMedServices" :key="i.id" class="mt-2">
                                <p style="font-size:18px;color:#000;"> {{i.name}} </p>
                                <p class="text-right" style="position:relative; top: -25px;font-size:18px;color:#000;"> {{i.price}} KZT </p>
                                <hr class="my-0 mb-2" v-if="i.id != currMedServices.length">
                            </div>
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

                    <CCard class="p-3" v-if="editTab"> <!-- записаться -->
                        <h3>Записаться</h3>
                        
                        <CRow>
                            <CCol sm='8' class="mx-auto" v-if="is_created == false">
                            <CInput v-model="name" :placeholder="userInfo.name ? userInfo.name : 'Ваше имя' " required @keyup.enter="createBid()"> </CInput>
                            <VuePhoneNumberInput class="mb-3" v-model="phone" default-country-code="KZ" maxlength="12" />
                            
                            <CSelect
                                    
                                    :options="currMedServicesNames"
                                    v-model="bid_select_model"
                                    :value.sync="bid_select_model"
                                    />

                                <CInput v-model="someInfo" placeholder="Комментарий" />
                            </CCol>

                            <CCol sm='8' class="mx-auto" v-else>
                                <CCard class="orange__btn">
                                    <h3 class="m-auto p-1 text-center">Спасибо! Ваша заявка отправлена</h3>
                                </CCard>
                            </CCol>

                            <CCol sm='12'>
                                <div class="w-100"></div>
                            </CCol>
                            <CCol sm='6' class="mx-auto">
                                <CButton class="orange__btn w-100" @click="createBid" v-if="is_created == false"> Записаться </CButton>
                            </CCol>
                        </CRow>
                    </CCard>

                </CCol>
            </CRow>
        </CCol>

        <CCol sm='11' class="mx-auto">
            <CCard class="p-3">
                <CCard v-if="is_review_created == false">
                    <p class="text-center pt-2">Оставьте отзыв</p>
                    <p v-if="reviewErr" class="text-center pt-2">Поле отзыва не должно быть пустым</p>
                    <p v-if="authErr" class="text-center pt-2">Чтобы оставить отзыв необходимо авторизоваться</p>
                    <CInput class="px-2" placeholder="Введите ваш отзыв" v-model="ratingReviewModel" @keyup.enter="createReview" />
                    <StarRating v-model="selectOption" :star-size="30" :show-rating="false" class="mb-3" />
                    <CButton class="orange__btn" @click="createReviewMed"> Отправить </CButton>
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
                <CCard v-for="i in medReviewData" :key="i.id" class="card__review">
                    <p class="ml-2">{{i.author.email}}</p>  
                    <p class="ml-2">{{i.review}}</p>
                    <StarRating class="med__rating" :read-only="true" v-model="i.rating" :star-size="25" :show-rating="false" />
                </CCard>
                </div>
            </CCard>
        </CCol>
    </CRow>
</div>


</template>

<script>
import { getAPI } from '../axios-api'
import DG from '2gis-maps'
import CTableWrapper from './CTable'
import serviceData from '../servicedataV2'
import DocCardHorz from '../components/DocCardHorz'
import DocCard from '../components/DocCardV2'
import StarRating from 'vue-star-rating'
import VuePhoneNumberInput from 'vue-phone-number-input';
import 'vue-phone-number-input/dist/vue-phone-number-input.css';

export default {
    name: "Med",
    components: {
        CTableWrapper,
        DocCardHorz,
        DocCard,
        StarRating,
        VuePhoneNumberInput
    },
    data() {
        return {
            id: this.$route.params.id,
            windowWidth: window.innerWidth,
            is_auth: this.$store.state.is_auth,

            currMedData: [],
            currMedImages: [],
            currMedServices: [],
            currMedServicesNames: [],
            dataIsLoaded: false,
            map: null,
            Modal: false,
            name: '',
            phone: '',
            sData: serviceData,
            docOfThisMed: [],
            is_created: false,
            bid_select_model: 'Выберите услугу',
            bid_select_opt: serviceData,
            bid_select_opt_clear: ['Выберите услугу'],
            someInfo: '',
            phoneLenErr: false,

            is_review_created: false,
            ratingReviewModel: null,
            ratingOptions: [1,2,3,4,5],
            selectOption: 5,
            reviewErr: false,
            authErr: false,
            medReviewData: [],
            showReviews: false,

            infoTab: true,
            inputTab: false, 
            endedTab: false, 
            editTab: false,
            contactTab: true,
            serviceTab: false,
            doctorsTab: false, 

            userInfo: [],
            userID: 0,

            showPhone: false,
            showPhone2: false,
            showPhone3: false
        }
    },
    methods: {
        getsData(){
            return this.sData.slice(0);
        },

        fetchUserInfo() {
            if(this.is_auth) {
                getAPI.get(`/api/user-info/`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
                .then(res => {
                    this.userInfo = res.data;
                    //this.name = this.userInfo.name;
                    this.phone = this.userInfo.phone;
                    this.userID = this.userInfo.id;

                })
                .catch(err => {
                    console.log("error get user info: ", err);
                })
            }
            
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

                for(var i = 0; i < this.currMedServices.length; i++) {
                    this.currMedServicesNames.push(this.currMedServices[i].name);
                }
            })
            .catch(err => {
                console.log("error get curr med services: ", err)
            })
        },

        fetchCurrMedData()
        {
            getAPI.get(`/api/med/${this.id}/`)
            .then(res => {
                this.currMedData = res.data;

                this.loadMedImages(this.id);
                this.loadMedServices(this.id);

                this.dataIsLoaded = true;
            })

        },
        setMap() {
            if(this.dataIsLoaded){
                setTimeout(() => {
                    this.map = new DG.map("map", {
                        center: [this.currMedData.coordX, this.currMedData.coordY],
                        zoom: 16,
                        // zoomControl: false,
                        minZoom: 10,
                        fullscreenControl: false,
                        scrollWheelZoom: false
                    });

                    DG.marker([this.currMedData.coordX, this.currMedData.coordY]).addTo(this.map);
                }, 100);
            }
        },

        getDocOfThisMed() {
            getAPI.get(`/api/get-curr-doc/${this.currMedData.id}/`)
            .then(res => {
                let data = JSON.parse(res.data);
                this.docOfThisMed = data;
                console.log("adasasda: ", data);
            })
            .catch(err => {
                console.log("error while fetch get-curr-doc: ", err);
            })
        },

        fetchMedReviewData() {
            getAPI.get(`/api/medreview/`)
            .then(res => {
                for(var i = 0; i < res.data.length; i++){
                    if(res.data[i].moderate && res.data[i].medcenter.id == this.$route.params.id) {
                        this.medReviewData.push(res.data[i]);
                    }
                }
                console.log("reviewData: ", this.medReviewData);
            })
            .catch(err => {
                console.log("error fetch med review data: ", err);
            })
        },

        createReviewMed() {

            this.reviewErr = false;

            if(!this.ratingReviewModel) {
                this.reviewErr = true;
            } else {

                let data = {
                    "review": this.ratingReviewModel,
                    "rating": this.selectOption,
                    "id": this.$route.params.id
                }

                getAPI.post(`/api/create-review-med/`, data, {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
                .then(res => {
                    console.log('create review med ok: ', res);
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

        viewsPlus() {
            let newViews = this.currMedData.views + 1;

            let data = {
                "views": newViews
            }

            getAPI.patch(`/api/med/${this.currMedData.id}/`, data)
            .then(() => {
                console.log("views++");
            })
            .catch(err => {
                console.log("error views++: ", err);
            })
        },

        plusNumPhoneSee() {
            this.currMedData.num_phone_see++;

            getAPI.patch(`/api/med/${this.$route.params.id}/`, {"num_phone_see" : this.currMedData.num_phone_see})
            .then(() => {
                console.log("med num_phone_see++");
            })
            .catch(err => {
                console.log("error num_phone_see++: ", err);
            })

        },

        restartPage() {
            this.$router.go(0)
        },

        createBid(){

            this.phoneLenErr = false;

            

            

            if(this.phoneLenErr == false) {

                if(this.userInfo.name != '') this.name = this.userInfo.name;

                let data = {
                    "name"    : this.name,
                    "phone"   : this.phone,
                    "select"  : this.bid_select_model,
                    "id"      : -1, //this.$route.params.id,
                    "someInfo": this.someInfo,
                    "customerID": this.userID,
                    "in_med_center": true,
                    "medCenter": this.id
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
    },
    mounted() {
        this.fetchCurrMedData();
        this.fetchMedReviewData();
        this.fetchUserInfo();

        for(var i = 0; i < this.bid_select_opt.length; i++){
            this.bid_select_opt_clear[i+1] = (this.bid_select_opt[i].service);
        }

        setTimeout(() => {
            if(this.currMedData.this_is == 4) {
                this.contactTab = false;
                this.doctorsTab = true;
            }
        }, 50);
    },
    computed: {
        b_dataIsLoaded() {
            if(this.dataIsLoaded){
                return true;
            } else {
                return false;
            }
        },

        b_wipe_errors() {
            if(this.authErr || this.reviewErr) {
                return true;
            } else {
                return false;
            }
        },

        compiledHtml: function() {
            return this.currMedData.text;
        }
    },
    watch: {
        b_dataIsLoaded(res){
            if(res){
                this.setMap();
                this.getDocOfThisMed();
                this.viewsPlus();
            }
        },

        b_wipe_errors(res) {
            if(res) {
                setTimeout(() => {
                    this.authErr = false;
                    this.reviewErr = false;
                }, 3000);
            }
        }
    },
    filters: {
        max_digits(amount) {
            const amt = Number(amount)
            return amt && amt.toLocaleString(undefined, {maximumFractionDigits:2}) || '0'
        },

        toTime(value) {
            return String(value).slice(0,5)
        }
    }
}
</script>

<style scoped>
.nav-link {
    color: blue !important;
}

.show__phone {
    cursor: pointer;
    color: orange;
    width: 140px;
}


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
    font-weight: 500;
}

.card {
    border-radius: 15px;
}

.med__rating {
    position: absolute;
    top: 5px;
    right: 15px;
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

@media screen and (max-width: 575px) {
    .col-sm-2 {
        max-width: 100px !important;
    }
}
</style>