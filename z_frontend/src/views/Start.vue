<template>
    <div>

    <CRow> 
        <!-- tablet -->
        <CCol v-if="windowWidth > 576 && windowWidth < 1024" sm='12' style="background-image: url('/img/phone_bg.png'); height: 45rem; background-repeat: round;" >

            <img src="/img/phone_bg_people.svg" style="width: 250px;position:absolute; top: 350px;left:25%;" />
            
            <CRow>
                        <CCol sm='10'>
                            <div>
                                <h4 class="text-center px-2" style="margin-top: 4rem;
                                                        font-size: 32px;
                                                        font-weight: 700;
                                                        color: #fff;"
                                                        >Онлайн-сервис по поиску ветеринарных услуг</h4>
                            </div>
                        </CCol>
                        <CCol sm='2'>
                            <div class="w-100"></div>
                        </CCol>
                        
                        <CCol sm='6' class="mx-auto" style="margin-top: 3rem;">
                            <input 
                                id="search__parent" 
                                type="text" 
                                class="form-control mx-auto" 
                                placeholder="Поиск" 
                                v-model="searchFld" 
                                v-on:keyup.enter="startSearch">

                            <img id="search__child" src="/img/search.png" width="40" height="35" @click="startSearch"/>
                        </CCol>
                    </CRow>
        </CCol>

        <!-- destop -->
        <CCol v-else-if="windowWidth > 575" sm='12' style="background-image: url('/img/bg_v1.png'); height: 35rem; background-repeat: round;">
            
            
            <CRow>
                <CCol sm='6'>
                    <CRow>
                        <CCol sm='11'>
                            <div>
                                <h4 class="" style="margin-top: 12rem;
                                                        font-size: 48px;
                                                        font-weight: 700;
                                                        color: #fff;"
                                                        :style="windowWidth > 575 ? 'position:relative;left: 15%;' : '' "
                                                        ><span style="color: orange;">VetPlus</span> - онлайн-сервис по поиску ветеринарных услуг</h4>
                            </div>
                        </CCol>
                        <CCol sm='2'>
                            <div class="w-100"></div>
                        </CCol>
                        
                        <CCol sm='10' class="mx-auto" style="margin-top: 3rem;">
                            <input 
                                id="search__parent" 
                                type="text" 
                                class="form-control" 
                                placeholder="Поиск" 
                                v-model="searchFld" 
                                v-on:keyup.enter="startSearch">

                            <img id="search__child" src="/img/search.png" width="40" height="35" @click="startSearch"/>
                        </CCol>
                    </CRow>
                </CCol>
            </CRow>

        </CCol> 
        
        <!-- mobile -->
        <CCol v-else-if="windowWidth < 575" sm='12' style="background-image: url('/img/phone_bg.png'); height: 45rem; background-repeat: round;" >

            <img src="/img/phone_bg_people.svg" style="width: 250px;position:absolute; top: 350px;left:25%;" />
            
            <CRow>
                        <CCol sm='10'>
                            <div>
                                <h4 class="text-center px-2" style="margin-top: 4rem;
                                                        font-size: 32px;
                                                        font-weight: 700;
                                                        color: #fff;"
                                                        >Онлайн-сервис по поиску ветеринарных услуг</h4>
                            </div>
                        </CCol>
                        <CCol sm='2'>
                            <div class="w-100"></div>
                        </CCol>
                        
                        <CCol sm='6' class="mx-auto" style="margin-top: 3rem;">
                            <input 
                                id="search__parent" 
                                type="text" 
                                class="form-control mx-auto" 
                                placeholder="Поиск" 
                                v-model="searchFld" 
                                v-on:keyup.enter="startSearch">

                            <img id="search__child" src="/img/search.png" width="40" height="35" @click="startSearch"/>
                        </CCol>
                    </CRow>
        </CCol>

        <!--
        <CCol sm='11'>
            <input type="text" class="form-control" placeholder="Поиск" v-model="searchFld" v-on:keyup.enter="startSearch">
        </CCol>
        <CCol sm='1'>
            <CButton class="success w-100 mx-auto d-block" @click="startSearch"> Поиск</CButton>
        </CCol>
        -->
    </CRow>

        <CRow style="overflow: hidden;">

            <div :style="windowWidth > 575 ?  `background-image: url('/img/lapki_red.png'); 
                                                background-repeat: space;` : ''" 
                  style="width: 100%;"
                class="mt-5">
                <CCol md='10' class="mx-auto" >
                <p class="border-shmorder-140" style="cursor:pointer;" @click="gotoServices">Услуги</p>
                <div class="testimonials5">
                    <div class="scroller5">
                        <div class="item5" v-for="card in serviceData" :key="card.id">
                            <router-link :to="{name: 'services', params: {id: card.id}}">
                                <ServiceCard :card="card" />
                            </router-link>
                        </div>
                    </div>
                    <img src="/img/btn_prev.svg" class="btn prev" @click="scrollToPrevItem(5)" :style="windowWidth < 575 ? `left: calc(((${windowWidth}px - 128px) / 2) - 160px)` : '' " />
                    <img src="/img/btn_next.svg" class="btn next" @click="scrollToNextItem(5)" :style="windowWidth < 575 ? `right: calc(((${windowWidth}px - 128px) / 2) - 120px)` : '' " />
                </div>
            </CCol>
            <img src="/img/for_bg/sled_blue.png" class="sled__blue" :style="windowWidth > 575 ? 'visibility:hidden;' : '' " />
            <img src="/img/for_bg/sled_blue.png" class="sled__blue_service_2" v-if="windowWidth < 575" />
            </div>


            <div style="background-repeat: round;
                        min-height: 650px;
                        width: 100%;"
                :style="windowWidth < 575 ? `background-image: url('/img/wave_bg.png');` : `background-image: url('/img/wave_spec_bg.png');` "
                >
                <CCol md='10' class="mx-auto " style="position:relative; top: 100px;">
                    <p class="border-shmorder-140" style="cursor:pointer;" @click="gotoAllDocs">Специалисты</p>
                    <div class="testimonials2">
                        <div class="scroller2" :style="windowWidth < 575 ? `margin-left: calc((${windowWidth}px - 400px) / 2)` : '' ">
                            <div class="item2" v-for="card in docData" :key="card.id">
                                <router-link :to="{name: 'doc', params: {id: card.id}}">
                                    <DocCard :card="card" />
                                </router-link>
                            </div>
                        </div>                                                                  
                        <img src="/img/btn_prev.png" class="btn prev" @click="scrollToPrevItem(2)" :style="windowWidth < 575 ? `left: calc(((${windowWidth}px - 128px) / 2) - 160px)` : '' " />
                        <img src="/img/btn_next.png" class="btn next" @click="scrollToNextItem(2)" :style="windowWidth < 575 ? `right: calc(((${windowWidth}px - 128px) / 2) - 120px)` : '' " />
                    </div>
                </CCol>
                <img src="/img/for_bg/sled_blue.png" class="sled__blue_spec_1" v-if="windowWidth < 575" />
                <img src="/img/for_bg/sled_blue.png" class="sled__blue_spec_2" v-if="windowWidth < 575" />
                <img src="/img/for_bg/sled_red.png" class="sled__blue_spec_3" v-if="windowWidth < 575" />
                <img src="/img/for_bg/sled_red.png" class="sled__blue_spec_4" v-if="windowWidth < 575" />
            </div>
            
            
            <div style="background-image: url('/img/med_bg.png'); 
                        width: 100%;"
                        class="">
            <CCol md='10' class="mx-auto">
                <p class="border-shmorder-140" style="cursor:pointer;" @click="gotoListOfVets">Ветеринарные клиники</p>
                <div class="testimonials1">
                    <div class="scroller1" :style="windowWidth < 575 ? `margin-left: calc((${windowWidth}px - 415px) / 2)` : '' ">
                        <div class="item1" v-for="card in medData" :key="card.id">
                            <router-link :to="{name: 'med', params: {id: card.id}}">
                                <MedCard :card="card" />
                            </router-link>
                        </div>
                    </div>
                    <img src="/img/btn_prev.svg" class="btn prev" @click="scrollToPrevItem(1)" :style="windowWidth < 575 ? `left: calc(((${windowWidth}px - 128px) / 2) - 160px)` : '' " />
                    <img src="/img/btn_next.svg" class="btn next" @click="scrollToNextItem(1)" :style="windowWidth < 575 ? `right: calc(((${windowWidth}px - 128px) / 2) - 130px)` : '' " />
                </div>
            </CCol>
                <img src="/img/for_bg/sled_blue.png" class="sled__blue_vet" v-if="windowWidth < 575" />
                <img src="/img/for_bg/sled_red.png" class="sled__red_vet" v-if="windowWidth < 575" />
            </div>

            <div style="background-image: url('/img/wave_bg.png');
                        background-repeat: round;
                        max-height: 360px;
                        width: 100%;">
            <CCol md='10' class="mx-auto mt-5">
                <p class="border-shmorder-140" style="cursor:pointer;" @click="gotoVetShops">Зоомагазины</p>
                <div class="testimonials3">
                    <div class="scroller3" :style="windowWidth < 575 ? `margin-left: calc((${windowWidth}px - 415px) / 2)` : '' ">
                        <div class="item3" v-for="card in zooData" :key="card.id">
                            <router-link :to="{name: 'med', params: {id: card.id}}">
                                <MedCard :card="card" />
                            </router-link>
                        </div>
                    </div>
                    <img src="/img/btn_prev.svg" class="btn prev" @click="scrollToPrevItem(3)" :style="windowWidth < 575 ? `left: calc(((${windowWidth}px - 128px) / 2) - 160px)` : '' " />
                    <img src="/img/btn_next.svg" class="btn next" @click="scrollToNextItem(3)" :style="windowWidth < 575 ? `right: calc(((${windowWidth}px - 128px) / 2) - 130px)` : '' " />
                </div>
            </CCol>
                <img src="/img/ball_1.svg" class="ball__zoo"/>
                <img src="/img/for_bg/bone.png" class="bone__zoo" />
            </div>

            <div style="background-image: url('/img/pharm_bg.png'); 
                        width: 100%;
                        "
                        class="mt-5">
        
            <CCol md='10' class="mx-auto">
                <p class="border-shmorder-140" style="cursor:pointer;" @click="gotoPharmacy">Аптеки</p>
                <div class="testimonials4">
                    <div class="scroller4" :style="windowWidth < 575 ? `margin-left: calc((${windowWidth}px - 415px) / 2)` : '' ">
                        <div class="item4" v-for="card in pharmData" :key="card.id">
                            <router-link :to="{name: 'med', params: {id: card.id}}">
                                <MedCard :card="card" />
                            </router-link>
                        </div>
                    </div>
                    <img src="/img/btn_prev.svg" class="btn prev" @click="scrollToPrevItem(4)" :style="windowWidth < 575 ? `left: calc(((${windowWidth}px - 128px) / 2) - 160px)` : '' " />
                    <img src="/img/btn_next.svg" class="btn next" @click="scrollToNextItem(4)" :style="windowWidth < 575 ? `right: calc(((${windowWidth}px - 128px) / 2) - 130px)` : '' "/>
                </div>
            </CCol>
                <img src="/img/for_bg/sled_blue.png" class="sled__blue_pharm" v-if="windowWidth < 575" />
                <img src="/img/for_bg/sled_red.png" class="sled__red_pharm" v-if="windowWidth < 575" />
                <img src="/img/for_bg/sled_red.png" class="sled__red_pharm_2" v-if="windowWidth < 575" />
            </div>


            <div style="background-image: url('/img/wave_bg.png');
                        background-repeat: round;
                        min-height: 400px;
                        width: 100%;">
            <CCol md='10' class="mx-auto mt-5">
                <p class="border-shmorder-140" style="cursor:pointer;" @click="gotoKinolog">Кинологические центры</p>
                <div class="testimonials6">
                    <div class="scroller6" :style="windowWidth < 575 ? `margin-left: calc((${windowWidth}px - 415px) / 2)` : '' ">
                        <div class="item6" v-for="card in kinologData" :key="card.id">
                            <router-link :to="{name: 'med', params: {id: card.id}}">
                                <MedCard :card="card" />
                            </router-link>
                        </div>
                    </div>
                    <img src="/img/btn_prev.svg" class="btn prev" @click="scrollToPrevItem(6)" :style="windowWidth < 575 ? `left: calc(((${windowWidth}px - 128px) / 2) - 160px)` : '' " />
                    <img src="/img/btn_next.svg" class="btn next" @click="scrollToNextItem(6)"  :style="windowWidth < 575 ? `right: calc(((${windowWidth}px - 128px) / 2) - 130px)` : '' "/>
                </div>
            </CCol>
                <img src="/img/for_bg/bone.png"      class="bone__blue" />
                <img :style="windowWidth > 575 ? 'visibility:hidden;' : '' " src="/img/for_bg/sled_red.png"  class="sled__red" />
                <img src="/img/for_bg/sled_blue.png" class="sled__blue" />
                <img src="/img/for_bg/bone_2.png"    class="bone__red" v-if="windowWidth > 575"/>
                <img src="/img/dog.svg"              class="dog" />
                <img src="/img/ball.svg"             class="ball" v-if="windowWidth > 575"/>
            </div>

            <div style="max-height: 360px;
                        width: 100%;"
                        class="">
            <CCol md='10' class="mx-auto">
                <p class="border-shmorder-140" style="cursor:pointer;" @click="gotoGrumery">Грумеры</p>
                <div class="testimonials7">
                    <div class="scroller7" :style="windowWidth < 575 ? `margin-left: calc((${windowWidth}px - 415px) / 2)` : '' ">
                        <div class="item7" v-for="card in grumerData" :key="card.id">
                            <router-link :to="{name: 'med', params: {id: card.id}}">
                                <MedCard :card="card" />
                            </router-link>
                        </div>
                    </div>
                    <img src="/img/btn_prev.svg" class="btn prev" @click="scrollToPrevItem(7)" :style="windowWidth < 575 ? `left: calc(((${windowWidth}px - 128px) / 2) - 160px)` : '' " />
                    <img src="/img/btn_next.svg" class="btn next" @click="scrollToNextItem(7)" :style="windowWidth < 575 ? `right: calc(((${windowWidth}px - 128px) / 2) - 130px)` : '' " />
                </div>
            </CCol>
            <img src="/img/shampoo.svg" class="shampoo" />
            <img src="/img/scissors.svg" class="scissors" v-if="windowWidth > 575"/>
            </div>


            <div style="background-image: url('/img/wave_bg.png');
                        background-repeat: round;
                        min-height: 400px;
                        width: 100%;">
            <CCol md='10' class="mx-auto mt-5">
                <p class="border-shmorder-140" style="cursor:pointer;">Приюты</p>
                <div class="testimonials8">
                    <div class="scroller8" :style="windowWidth < 575 ? `margin-left: calc((${windowWidth}px - 415px) / 2)` : '' ">
                        <div class="item8" v-for="card in priutData" :key="card.id">
                            <router-link :to="{name: 'med', params: {id: card.id}}">
                                <MedCard :card="card" />
                            </router-link>
                        </div>
                    </div>
                    <img src="/img/btn_prev.svg" class="btn prev" @click="scrollToPrevItem(8)" :style="windowWidth < 575 ? `left: calc(((${windowWidth}px - 128px) / 2) - 160px)` : '' " />
                    <img src="/img/btn_next.svg" class="btn next" @click="scrollToNextItem(8)" :style="windowWidth < 575 ? `right: calc(((${windowWidth}px - 128px) / 2) - 130px)` : '' " />
                </div>
            </CCol>
                <img src="/img/for_bg/sled_red.png" class="priut__sled__red" /> 
                <img v-if="windowWidth < 575" src="/img/for_bg/sled_blue.png" class="priut__sled__blue" /> 
                <img v-if="windowWidth > 575" src="/img/for_bg/sled_blue.png" class="priut__sled__blue_2" /> 
                <img v-if="windowWidth > 575" src="/img/for_bg/bone.png" class="priut__bone__blue" />
            </div>

        </CRow>

    </div>
</template>

<script>
import { getAPI } from '../axios-api'
import MedCard from '../components/MedCard'
import DocCard from '../components/DocCard'
import ServiceCard from '../components/ServiceCard.vue'

export default {
    name: "Start",
    components: {
        MedCard,
        DocCard,
        ServiceCard
    },
    data() {
        return {
            typeOptions: ['Врачи', 'Клиники', ],
            typeNames: ['Тип'],
            medData: [],
            docData: [],
            pharmData: [],
            zooData: [],
            serviceData: [],
            kinologData: [],
            grumerData: [],
            priutData: [],

            loading: false,
            searchFld: '',
            windowWidth: window.innerWidth
        }
    },
    methods: {
        fetchMedData() {
            getAPI.get(`/api/med/`)
            .then(res => {
                //this.medData = res.data;

                for( var i = 0; i < res.data.length; i++ ) {
                    if( res.data[i].this_is == 1 ) {
                        this.medData.push(res.data[i]);
                    }

                    if( res.data[i].this_is == 2 ) {
                        this.zooData.push(res.data[i]);
                    }

                    if( res.data[i].this_is == 3 ) {
                        this.pharmData.push(res.data[i]);
                    }

                    if( res.data[i].this_is == 4 ) {
                        this.kinologData.push(res.data[i]);
                    }

                    if( res.data[i].this_is == 5 ) {
                        this.grumerData.push(res.data[i]);
                    }

                    if( res.data[i].this_is == 6 ) {
                        this.priutData.push(res.data[i]);
                    }
                }
            })
            .catch(err => {
                console.log("error fetch med data: ", err);
            })
        },

        async fetchDocData() {
            this.loading = true;
            await getAPI.get(`/api/doc/`)
            .then(res => {
                var temp = [];
                for(var i = 0; i < res.data.length; i++){
                    if(res.data[i].first_name != '' || res.data[i].last_name != '') {
                        if(res.data[i].is_doctor == true)
                            temp.push(res.data[i]);
                    }
                }
                this.docData = temp;
            })
            .catch(err => {
                console.log("error fetch doc data: ", err);
            })
            this.loading = false;
        },

        async fetchServicesData() {
            getAPI.get(`/api/services/`)
            .then(res => {
                this.serviceData = res.data;
            })
            .catch(err => {
                console.log("error fetch service data: ", err);
            });
        },

        startSearch() {
            this.$router.push({path: 'search', query: {searchtxt: this.searchFld}})
        },

        onResize() {
            this.windowWidth = window.innerWidth;
        },

        scrollToNextItem(offset) {
            const testimonials = document.querySelector(`.testimonials${offset}`);
            const scroller = testimonials.querySelector(`.scroller${offset}`);
            let itemWidth = 1000; //testimonials.querySelector(`.item${offset}`).clientWidth;
            if(offset == 5) itemWidth = 300;
            if(this.windowWidth < 575) itemWidth = testimonials.querySelector(`.item${offset}`).clientWidth;

            if(scroller.scrollLeft < (scroller.scrollWidth - itemWidth))
                // The scroll position is not at the beginning of last item
                scroller.scrollBy({left: itemWidth, top: 0, behavior:'smooth'});
            else
                // Last item reached. Go back to first item by setting scroll position to 0
                scroller.scrollTo({left: 0, top: 0, behavior:'smooth'});
        },

        scrollToPrevItem(offset) {
            const testimonials = document.querySelector(`.testimonials${offset}`);
            const scroller = testimonials.querySelector(`.scroller${offset}`);
            let itemWidth = 1000; //testimonials.querySelector(`.item${offset}`).clientWidth;
            if(offset == 5) itemWidth = 300;
            if(this.windowWidth < 575) itemWidth = testimonials.querySelector(`.item${offset}`).clientWidth;

            if(scroller.scrollLeft != 0)
                // The scroll position is not at the beginning of first item
                scroller.scrollBy({left: -itemWidth, top: 0, behavior:'smooth'});
            else
                // This is the first item. Go to last item by setting scroll position to scroller width
                scroller.scrollTo({left: scroller.scrollWidth, top: 0, behavior:'smooth'});
        },


        gotoPharmacy() {
            this.$router.push('/search?searchtxt=Аптека');
            setTimeout(() => {
                this.$router.go(0);
            }, 100);
        },
        gotoAllDocs() {
            this.$router.push('/search?searchtxt=Врач');
            setTimeout(() => {
                this.$router.go(0);
            }, 100);
        },
        gotoListOfVets() {
            this.$router.push('/search?searchtxt=Клиник');
            setTimeout(() => {
                this.$router.go(0);
            }, 100);
        },
        gotoServices() {
            this.$router.push(`/search?searchtxt=Услуг`); 
            setTimeout(() => {
                this.$router.go(0);
            }, 100);
        }, 
        gotoVetShops() {
            this.$router.push(`/search?searchtxt=Магазин`);
            setTimeout(() => {
                this.$router.go(0);
            }, 100);
        },
        gotoKinolog() {
            this.$router.push(`/search?searchtxt=Кинолог`); 
            setTimeout(() => {
                this.$router.go(0);
            }, 100);
        },
        gotoGrumery() {
            this.$router.push(`/search?searchtxt=Грумеры`);
            setTimeout(() => {
                this.$router.go(0);
            }, 100);
        },
        gotoVetPartner() {
            this.$router.push(`/partner`);
        },
    },
    created() {
        this.fetchMedData();
        this.fetchDocData();
        this.fetchServicesData();
    },
    filters: {
        max_digits(amount) {
            const amt = Number(amount)
            return amt && amt.toLocaleString(undefined, {maximumFractionDigits:2}) || '0'
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

        toTime(value) {
            return String(value).slice(0, 5); 
        }
    },
    mounted() {
        this.$nextTick(() => {
            window.addEventListener('resize', this.onResize);
        })
    },
    beforeDestroy() { 
        window.removeEventListener('resize', this.onResize); 
    }
}
</script>

<style scoped>

.success {
    background-color: green;
    color: white;
}

.c-main {
    padding-top: 0 !important;
}

.h3-3 {
    font-size: 200%; /* Размер шрифта */
    border-bottom: 4px solid rgb(252, 41, 41); /* Параметры линии под текстом */
    font-weight: normal; /* Убираем жирное начертание */
    padding-bottom: 5px; /* Расстояние от текста до линии */
    width: 10%;
    margin-right: 7%;
    margin-bottom: 1rem;
   }

h3 {
    font-size: 200%;
    font-weight: normal;
}

.clearfix {
    clear: both;
}


/* ----------------------------------- */
.container-fluid {
    padding: 0 0 !important;
}

.sled__blue_pharm {
    width: 34px;
    position: relative;
    left: 20%;
}

.sled__red_pharm {
    width: 34px;
    position: relative;
    left: 70%;
    top: -300px;
}

.sled__red_pharm_2 {
    width: 34px;
    position: relative;
    left: 50%;
    top: -280px;
}

.sled__blue_vet {
    width: 34px;
    position: relative;
    left: 20%;
}

.sled__red_vet {
    width: 34px;
    position: relative;
    left: 70%;
    top: -280px;
}

.priut__sled__blue {
    position: relative;
    top: -60%;
    left: 0;
}

.priut__sled__red {
    position: relative;
    top: -270px;
    left: 30%;
}

.priut__sled__blue_2 {
    position: relative;
    top: 0%;
    left: 80%;
}

.priut__bone__blue {
    position: relative;
    top: -70%;
    left: 50%;
}

.ball__zoo {
    position: relative;
    top: -70%;
    left: 94%;
}

.bone__zoo {
    width: 44px;
    position: relative;
    top: -40%;
    left: 0%;
}

.scissors {
    position: relative;
    top: -70%;
    left: 86%;
}

.shampoo {
    position: relative;
    top: -30%;
    left: 4%;
}

.dog {
    position: relative;
    left: -11%;
}

.ball {
    position: relative;
    top: -70%;
    left: 75%;
}

.bone__blue {
    z-index: 0;
    position: relative;
    left: 50%;
    top: -70%;
}

.sled__red {
    z-index: 0;
    position: relative;
    left: 10%;
    top: -5%;
}

.sled__blue {
    z-index: 0;
    position: relative;
    left: 50%;
} 

.bone__red {
    z-index: 0;
    position: relative;
    left: 82%;
    top: -35%;
}

.sled__blue_spec_1, .sled__blue_spec_2, .sled__blue_spec_3, .sled__blue_spec_4 {
    width: 34px;
}

.sled__blue_spec_1 {
    position: relative;
    top: 0;
    left: 50px;
}

.sled__blue_spec_2 {
    position: relative;
    top: -40px;
    left: 0px;
}

.sled__blue_spec_3 {
    position: relative;
    left: 65%;
    top: -300px;
}

.sled__blue_spec_4 {
    position: relative;
    left: 60%;
    top: -340px;
}

#search__parent {
    position: relative;
    width: 550px;
    outline: none !important;
    border: none;
    height: 58px;
    border-radius: 15px;
    left: -30px;
}

#search__child {
    position: absolute;
    top: 0px;
    left: 520px;
    height: 58px;
    width: 65px;
    cursor: pointer;
}

#search__parent:focus,#search__parent:active {
   outline: none !important;
   box-shadow: none;
}

.testimonials1, 
.testimonials2, 
.testimonials3, 
.testimonials4, 
.testimonials5,
.testimonials6,
.testimonials7,
.testimonials8 {
    max-width: 1200px;
    margin: auto;
    padding: 15px;
    text-align: left;
    position: relative;
}
.scroller1, 
.scroller2, 
.scroller3, 
.scroller4, 
/*.scroller5,*/
.scroller6,
.scroller7,
.scroller8 {
    overflow-x: auto;
    display: flex;
    scroll-snap-type: x mandatory;
}

.scroller5 {
    overflow-x: scroll;
    display: flex;
}

.scroller1::-webkit-scrollbar, 
.scroller2::-webkit-scrollbar, 
.scroller3::-webkit-scrollbar, 
.scroller4::-webkit-scrollbar,
.scroller5::-webkit-scrollbar,
.scroller6::-webkit-scrollbar,
.scroller7::-webkit-scrollbar,
.scroller8::-webkit-scrollbar {
  display: none;
}

.item1, 
.item2, 
.item3, 
.item4, 
.item5,
.item6,
.item7,
.item8 {
    min-width: 33%;
    scroll-snap-align: center;
    background-color: #00000000;
    margin-bottom: 10px;
    padding: 0 50px;
}
.item2, .item5 {
    min-width: 25%;
}
.item2 {
    padding: 0 20px;
}
/*
.item img {
    margin: 15px auto -60px;
    width: 120px;
    height: 120px;
    border: solid 4px #ffffff;
    border-radius: 60px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    z-index: 2;
}
*/
.card {
    background-color: rgb(237, 242, 247);
    padding: 80px 40px 40px;
    border-radius: 10px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    z-index: 1;
}
.card p {
    font-style: italic;
    line-height: 1.6;
}
.card span {
    display: block;
    margin-top: 20px;
    color: teal;
    font-weight: bold;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}
.testimonials1 .btn, 
.testimonials2 .btn, 
.testimonials3 .btn, 
.testimonials4 .btn, 
.testimonials5 .btn,
.testimonials6 .btn,
.testimonials7 .btn,
.testimonials8 .btn {
    position: absolute;
    top: 50%;
    margin-top: -60px;
    margin-left: -20px;
    /*height: 90px;*/
    width: 90px;
    border-radius: 50%;
    z-index: 1;
    line-height: 30px;
    text-align: center;
    color: white;
    font-weight: bold;
}
.testimonials1 .btn:hover, 
.testimonials2 .btn:hover, 
.testimonials3 .btn:hover, 
.testimonials4 .btn:hover, 
.testimonials5 .btn:hover,
.testimonials6 .btn:hover,
.testimonials7 .btn:hover,
.testimonials8 .btn:hover{
    cursor: pointer;
}

.testimonials1 .btn.next,
.testimonials2 .btn.next, 
.testimonials3 .btn.next, 
.testimonials4 .btn.next, 
.testimonials5 .btn.next,
.testimonials6 .btn.next,
.testimonials7 .btn.next,
.testimonials8 .btn.next {
    right: -70px;
}
.testimonials1 .btn.prev, 
.testimonials2 .btn.prev,
.testimonials3 .btn.prev, 
.testimonials4 .btn.prev, 
.testimonials5 .btn.prev,
.testimonials6 .btn.prev,
.testimonials7 .btn.prev,
.testimonials8 .btn.prev {
    left: -40px;
}
.testimonials2 .btn.prev {
    left: -50px;
}
@media screen and (max-width: 575px) {

    .testimonials1, 
    .testimonials2, 
    .testimonials3, 
    .testimonials4, 
    .testimonials5,
    .testimonials6,
    .testimonials7,
    .testimonials8 {
        margin-left: 3rem;
    }
    .testimonials2 {
        padding: 0;
    }

    .testimonials1 .btn, 
    .testimonials2 .btn, 
    .testimonials3 .btn, 
    .testimonials4 .btn, 
    .testimonials5 .btn,
    .testimonials6 .btn,
    .testimonials7 .btn,
    .testimonials8 .btn {
        height: 64px;
        width: 64px;
    }

    .testimonials1 .btn.next, 
    .testimonials2 .btn.next, 
    .testimonials3 .btn.next, 
    .testimonials4 .btn.next, 
    .testimonials5 .btn.next,
    .testimonials6 .btn.next,
    .testimonials7 .btn.next,
    .testimonials8 .btn.next {
        right: -20px;
    }
    .testimonials5 .btn.next,
    .testimonials2 .btn.next {
        right: 0px;
    }

    .testimonials2 .btn.prev {
        left: -2rem;
    }

    .item1, .item2, .item3, .item4, .item5, .item6, .item7, .item8 {
        min-width: 100%;
        padding: 0 10px;
    }
    .item2, .item5 {
        padding: 0 25px;
    }
    .card {
        padding: 80px 30px 30px;
    }

    #search__parent {
        width: 90%;
        left: 0px;
    }

    #search__child {
        left: calc(100% - 95px);
    }

    .ball__zoo {
        top: -210px;
        left: 84%;
        width: 59px;
    }

    .bone__zoo {
        top: -50px;
        left: -30px;
    }

    .bone__blue {
        width: 44px;
        top: -330px;
        left: 60%;
    }

    .sled__red {
        width: 44px;
        top: -310px;
        left: 0px;
    }

    .dog {
        width: 64px;
        left: -20%;
    }

    .sled__blue_service_2, .sled__blue {
        width: 34px;
    }

    .sled__blue_service_2 {
        position: relative;
        top: -300px;
        left: 30%;
    }

    .priut__sled__blue {
        width: 34px;
    }

    .priut__sled__red {
        width: 34px;
        top: -270px;
        left: 50%;
    }

    .priut__sled__blue_2 {
        top: -20%;
        left: 80%;
    }

}


@media screen 
  and (min-width: 576px) 
  and (max-width: 1024px) {
    .item1, 
    .item2, 
    .item3, 
    .item4, 
    .item5,
    .item6,
    .item7,
    .item8 {
        padding: 0 15px;
        margin-right: 100px;
    }

    .testimonials1 .btn, 
    .testimonials2 .btn, 
    .testimonials3 .btn, 
    .testimonials4 .btn, 
    .testimonials5 .btn,
    .testimonials6 .btn,
    .testimonials7 .btn,
    .testimonials8 .btn {
        visibility: hidden;
    }
}

</style>