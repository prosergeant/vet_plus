<template>
    <div class="mt-5">

        <CRow :class="windowWidth < 575 ? 'mb-4' : '' ">
            <CCol md='10' class="mx-auto">
                <input type="text" class="search" placeholder="Поиск" v-model="searchtxt" @keyup.enter="startSearch">
                <img class="search__lupa" src="/img/search.png" @click="startSearch" v-if="windowWidth > 575" />
                <div class="dropdown">
                    <div class="default_option" @click="search_dropdown = !search_dropdown"> Выберите категорию </div>  
                    <ul :class="search_dropdown ? 'active' : null ">
                        <li v-for="i in search_option" :key="i.id"> <CInputCheckbox :label="i.name" :checked="i.mod" @click="checkbox(i.id)" /> <hr v-if="i.id==0"> </li>
                    </ul>
                </div>

                <div class="dropdown2">
                    <div class="default_option2" @click="search_dropdown2 = !search_dropdown2"> Район </div>  
                    <ul :class="search_dropdown2 ? 'active' : null ">
                        <li v-for="i in search_district_option" :key="i.id"> 
                            <CInputCheckbox
                            :label="i.name" 
                            :checked="i.mod"
                            @click="checkboxDistrict(i.id)" />
                            <hr v-if="i.id==0">
                        </li>
                    </ul>
                </div>    
                
                <br>
                <CButton class="search__btn mr-2" :class="search_btn_sunday ? 'active' : '' " @click="search_btn_sunday = !search_btn_sunday, f_search_btn_now()"> Работает сейчас </CButton>   
                <CButton class="search__btn" :class="search_btn_now ? 'active' : '' " @click="search_btn_now = !search_btn_now, getLocatiomn()"> Рядом </CButton>
            
                <br>
                <br>
                <p v-if="windowWidth > 575" class="sort__by">Сортировать по: <span :class="sort_by_rating ? 'sort__by__active' : '' "
                                                                @click="f_sort_by_rating() ,sort_by_rating = true, sort_by_new = false, sort_by_alphabet = false">Рейтингу</span> <span :class="sort_by_new ? 'sort__by__active' : '' " @click="f_sort_by_exp(), sort_by_rating = false, sort_by_new = true, sort_by_alphabet = false">Стажу</span> <span :class="sort_by_alphabet ? 'sort__by__active' : '' " @click="f_sort_by_alphabet(), sort_by_rating = false, sort_by_new = false, sort_by_alphabet = true">Алфавиту</span> </p>

                <p v-if="windowWidth < 575 && sort_menu_hide" @click="sort_menu_hide = !sort_menu_hide" class="ml-3"> Сортировать >></p>

                <div v-if="windowWidth < 575 && sort_menu_hide == false">
                    <p class="ml-3">Сортировать по:</p>
                    <p class="ml-3 my-0" 
                    :class="sort_by_rating ? 'sort__by__active' : '' "
                    @click="f_sort_by_rating(),
                    sort_by_rating = true, 
                    sort_by_new = false, 
                    sort_by_alphabet = false" >Рейтингу</p>

                    <p class="ml-3 my-0" 
                    :class="sort_by_new ? 'sort__by__active' : '' " 
                    @click="f_sort_by_exp(), 
                    sort_by_rating = false, 
                    sort_by_new = true, 
                    sort_by_alphabet = false" >Стажу</p>

                    <p class="ml-3 my-0" 
                    :class="sort_by_alphabet ? 'sort__by__active' : '' " 
                    @click="f_sort_by_alphabet(), 
                    sort_by_rating = false, 
                    sort_by_new = false, 
                    sort_by_alphabet = true" >Алфавиту</p>
                </div>
               


            </CCol>
        </CRow>


        <p v-if="docData.length > 0 && MedGuys" style="max-width: 1200px;" class="border-shmorder-140 ml-5">Врачи</p>
        <CRow v-if="docData.length > 0 && MedGuys" style="max-width: 1200px;" class="mx-auto">
            <CCol sm='3' v-for="i in docData" :key="i.pk" class="mb-3">
                <router-link :to="{name: 'doc', params: { id: i.pk }}">
                    <DocCard :card="i" class="mx-auto" />
                </router-link>
            </CCol>
        </CRow>

        <h3 v-if="medData.length > 0 && VetClinics"  style="max-width: 1200px;" class="border-shmorder-140 ml-5">Ветеринарные клиники</h3>
        <CRow v-if="medData.length > 0 && VetClinics" style="max-width: 1200px;" class="mx-auto">
            <div v-for="i in medData" :key="i.pk" class="mb-3" :class="windowWidth < 575 ? 'mx-auto' : '' ">
            <CCol sm='4' v-if="search_district_option[i.fields.district].mod">
                <router-link :to="{name: 'med', params: {id: i.pk}}">
                    <MedCard :card="i" />
                </router-link>
            </CCol>
            </div>
        </CRow>


        <h3 v-if="pharmData.length > 0 && Pharmaces"  style="max-width: 1200px;" class="border-shmorder-140 ml-5 mt-1">Аптеки</h3>
        <CRow v-if="pharmData.length > 0 && Pharmaces"  style="max-width: 1200px;" class="mx-auto">
            <div v-for="i in pharmData" :key="i.pk" :class="windowWidth < 575 ? 'mx-auto' : '' ">
            <CCol sm='4' class="mb-3" v-if="search_district_option[i.fields.district].mod">
                <router-link :to="{name: 'med', params: {id: i.pk}}">
                    <MedCard :card="i" />
                </router-link>
            </CCol>
            </div>
        </CRow>


        <h3 v-if="zooData.length > 0 && Zoos"  style="max-width: 1200px;" class="border-shmorder-140 ml-5 mt-1">Зоомагазины</h3>
        <CRow v-if="zooData.length > 0 && Zoos"  style="max-width: 1200px;" class="mx-auto">
            <div v-for="i in zooData" :key="i.pk" :class="windowWidth < 575 ? 'mx-auto' : '' ">
            <CCol sm='4' class="mb-3" v-if="search_district_option[i.fields.district].mod">
                <router-link :to="{name: 'med', params: {id: i.pk}}">
                    <MedCard :card="i" />
                </router-link>
            </CCol>
            </div>
        </CRow>

        <!--
        <h3 v-if="serviceData.length > 0 && Services"  style="max-width: 1200px;" class="border-shmorder-140 ml-5 mt-1">Услуги</h3>
        <CRow v-if="serviceData.length > 0 && Services"  style="max-width: 1200px;" class="mx-auto">
            <CCol sm='4' v-for="i in serviceData" :key="i.pk" class="mb-3">
                <router-link :to="{name: 'med', params: {id: i.pk}}">
                    <ServiceCard :card="i" />
                </router-link>
            </CCol>
        </CRow>
        -->

        <h3 v-if="kinologData.length > 0 && Kinolog"  style="max-width: 1200px;" class="border-shmorder-140 ml-5 mt-1">Кинологи</h3>
        <CRow v-if="kinologData.length > 0 && Kinolog"  style="max-width: 1200px;" class="mx-auto">
            <div v-for="i in kinologData" :key="i.pk" :class="windowWidth < 575 ? 'mx-auto' : '' ">
            <CCol sm='4' class="mb-3" v-if="search_district_option[i.fields.district].mod">
                <router-link :to="{name: 'med', params: {id: i.pk}}" >
                    <MedCard :card="i" />
                </router-link>
            </CCol>
            </div>
        </CRow>

        <h3 v-if="grumerData.length > 0 && Grumer"  style="max-width: 1200px;" class="border-shmorder-140 ml-5 mt-1">Грумеры</h3>
        <CRow v-if="grumerData.length > 0 && Grumer"  style="max-width: 1200px;" class="mx-auto">
            <div v-for="i in grumerData" :key="i.pk" :class="windowWidth < 575 ? 'mx-auto' : '' ">
            <CCol sm='4' class="mb-3" v-if="search_district_option[i.fields.district].mod">
                <router-link :to="{name: 'med', params: {id: i.pk}}">
                    <MedCard :card="i" />
                </router-link>
            </CCol>
            </div>
        </CRow>


        <h3 v-if="priutData.length > 0 && Priut"  style="max-width: 1200px;" class="border-shmorder-140 ml-5 mt-1">Приюты</h3>
        <CRow v-if="priutData.length > 0 && Priut"  style="max-width: 1200px;" class="mx-auto">
            <div v-for="i in priutData" :key="i.pk" :class="windowWidth < 575 ? 'mx-auto' : '' ">
            <CCol sm='4' class="mb-3" v-if="search_district_option[i.fields.district].mod">
                <router-link :to="{name: 'med', params: {id: i.pk}}">
                    <MedCard :card="i" />
                </router-link>
            </CCol>
            </div>
        </CRow>

    </div>
</template>

<script>
import { getAPI } from '../axios-api'
import MedCard from '../components/MedCardV2'
import DocCard from '../components/DocCardV2'
import ServiceCard from '../components/ServiceCard.vue'
export default {
    name: 'Search',
    components: {
        MedCard,
        DocCard,
        ServiceCard
    },
    data() {
        return {
            windowWidth: window.innerWidth,
            searchtxt: this.$route.query.searchtxt,
            searchResult: [],
            allData: [],
            docData: [],
            medData: [],
            pharmData: [],
            zooData: [],
            serviceData: [],
            kinologData: [],
            grumerData: [],
            priutData: [],

            all: true,
            MedGuys: true,
            VetClinics: true,
            Pharmaces: true,
            Services: true,
            Zoos: true,
            Kinolog: true,
            Grumer: true,
            Priut: true,


            search_dropdown: false,
            search_dropdown2: false,            
            search_option: [  
                {id:0, name:'Все', mod:true},
                {id:1, name:'Медицинские центры', mod:true}, 
                {id:2, name:'Специалисты', mod:true}, 
                {id:3, name:'Зоомагазины', mod:true},
                {id:4, name:'Услуги', mod:true},
                {id:5, name:'Аптеки', mod:true},
                {id:6, name:'Кинологи', mod:true},
                {id:7, name:'Грумеры', mod:true},
                {id:8, name:'Приюты', mod:true} 
            ],

            search_district_option: [  
                {id:0, name:'Все районы', mod: true},
                {id:1, name:'Ауэзовский', mod:true}, 
                {id:2, name:'Медеуский', mod:true}, 
                {id:3, name:'Бостандыкский', mod:true},
                {id:4, name:'Алмалинский', mod:true},
                {id:5, name:'Жетысуский', mod:true},
                {id:6, name:'Турксибский', mod:true},
                {id:7, name:'Алатауский', mod:true},
                {id:8, name:'Наурызбайский', mod:true}
            ],

            search_btn_sunday: false,
            search_btn_now: false,

            sort_by_rating: false,
            sort_by_new: false,
            sort_by_alphabet: false,

            sort_menu_hide: true,
        }
    },
    methods: {
        getLocatiomn() {
            this.$getLocation({
                enableHighAccuracy: false, //defaults to false
                timeout: 10000, //defaults to Infinity
                maximumAge: 0 //defaults to 0
                
            })
            .then(coordinates => {
                console.log(coordinates);
            });
        },

        makeSearch() {

            let data = {
                "search": this.searchtxt
            }

            getAPI.post(`/api/search/`, data) 
            .then(res => {
                let data = JSON.parse(res.data);
                this.searchResult = data;

                console.log("make search ok: ", this.searchResult = data);


                for(var i = 0; i < this.searchResult.length; i++) {
                    if(this.searchResult[i].model == "main.teacher") {
                        this.docData.push(this.searchResult[i]);
                    } else if(this.searchResult[i].model == "main.medicalcenter") {
                        this.allData.push(this.searchResult[i]);
                    }
                }

                for( var i = 0; i < this.allData.length; i++ ) {
                    if( this.allData[i].fields.this_is == 1 ) {
                        this.medData.push(this.allData[i]);
                    }

                    if( this.allData[i].fields.this_is == 2 ) {
                        this.zooData.push(this.allData[i]);
                    }

                    if( this.allData[i].fields.this_is == 3 ) {
                        this.pharmData.push(this.allData[i]);
                    }

                    if( this.allData[i].fields.this_is == 4 ) { 
                        this.kinologData.push(this.allData[i]);
                    }

                    if( this.allData[i].fields.this_is == 5 ) { 
                        this.grumerData.push(this.allData[i]);
                    }

                    if( this.allData[i].fields.this_is == 6 ) { 
                        this.priutData.push(this.allData[i]);
                    }
                }

            })
            .catch(err => {
                console.log("error search: ", err);
            })
        },

        startSearch() {
            this.$router.push({path: 'search', query: {searchtxt: this.searchtxt}})
            this.$router.go(0)
        },

        checkbox(id) {
            if(id == 0) {
                if(this.all == true) {
                    this.all        = false
                    this.VetClinics = false
                    this.MedGuys    = false
                    this.Zoos       = false
                    this.Services   = false
                    this.Pharmaces  = false
                    this.Kinolog    = false
                    this.Grumer     = false
                    this.Priut      = false

                    for(var i = 0; i < this.search_option.length; i++) {
                        this.search_option[i].mod = false
                    }
                } else {
                    this.all        = true
                    this.VetClinics = true
                    this.MedGuys    = true
                    this.Zoos       = true
                    this.Services   = true
                    this.Pharmaces  = true
                    this.Kinolog    = true
                    this.Grumer     = true
                    this.Priut      = true

                    for(var i = 0; i < this.search_option.length; i++) {
                        this.search_option[i].mod = true
                    }
                }
            }
            if(id == 1) this.VetClinics = !this.VetClinics
            if(id == 2) this.MedGuys = !this.MedGuys
            if(id == 3) this.Zoos = !this.Zoos
            if(id == 4) this.Services = !this.Services
            if(id == 5) this.Pharmaces = !this.Pharmaces
            if(id == 6) this.Kinolog = !this.Kinolog
            if(id == 7) this.Grumer = !this.Grumer
            if(id == 8) this.Priut = !this.Priut
        },

        checkboxDistrict(id) {
            console.log("checkboxDistrict id: ", id);

            if(id == 0) {
                if(this.search_district_option[0].mod == true) {
                    for(var i = 0; i < this.search_district_option.length; i++) {
                        this.search_district_option[i].mod = false;
                    }
                } else {
                    for(var i = 0; i < this.search_district_option.length; i++) {
                        this.search_district_option[i].mod = true;
                    }
                }
            } else {
                this.search_district_option[id].mod = !this.search_district_option[id].mod;
            }
        },

        f_sort_by_rating() {
            this.medData.sort(function (a, b) {return a.fields.rating - b.fields.rating}).reverse();
            this.docData.sort(function (a, b) {return a.fields.rating - b.fields.rating}).reverse();
            this.pharmData.sort(function (a, b) {return a.fields.rating - b.fields.rating}).reverse();
            this.zooData.sort(function (a, b) {return a.fields.rating - b.fields.rating}).reverse();
        },

        f_sort_by_exp() {
            this.docData.sort(function (a, b) {return a.fields.exp - b.fields.exp}).reverse();
        },

        f_sort_by_alphabet() {
            this.medData.sort(function (a, b) {
            if (a.fields.name > b.fields.name) {
                return 1;
            }
            if (a.fields.name < b.fields.name) {
                return -1;
            }
            // a должно быть равным b
            return 0;
            });


            this.docData.sort(function (a, b) {
            if (a.fields.first_name > b.fields.first_name) {
                return 1;
            }
            if (a.fields.first_name < b.fields.first_name) {
                return -1;
            }
            // a должно быть равным b
            return 0;
            });


            this.pharmData.sort(function (a, b) {
            if (a.fields.name > b.fields.name) {
                return 1;
            }
            if (a.fields.name < b.fields.name) {
                return -1;
            }
            // a должно быть равным b
            return 0;
            });


            this.zooData.sort(function (a, b) {
            if (a.fields.name > b.fields.name) {
                return 1;
            }
            if (a.fields.name < b.fields.name) {
                return -1;
            }
            // a должно быть равным b
            return 0;
            });
        },

        getIsOpen(med) {
            const time = new Date().getHours();
            const time_end = med.fields.time_end.slice(0,2);
            const time_start = med.fields.time_start.slice(0,2);
            let b_is_open = false;
            if(time < parseInt(time_end) && time >= parseInt(time_start)) b_is_open = true;
            return b_is_open;
        },

        f_search_btn_now() {
            if(this.search_btn_sunday) {
                let temp = []
                for(var i = 0; i < this.medData.length; i++) {
                    if(this.getIsOpen(this.medData[i])) {
                        temp.push(this.medData[i])
                    }
                }
                this.medData = [];
                this.medData = temp;
            } else {
                this.searchResult= []
                this.allData     = []
                this.docData     = []
                this.medData     = []
                this.pharmData   = []
                this.zooData     = []
                this.serviceData = []
                this.kinologData = []
                this.grumerData  = []
                this.priutData   = []
                this.makeSearch();
            }
        }
    },
    mounted() {
        this.makeSearch();
    }
}
</script>

<style scoped>
.search {
    border-top-left-radius: 12px;
    border-bottom-left-radius: 12px;
    width: 690px;
    height: 45px;
    border: 1px solid #00000023;
    box-shadow: 0 8px 8px #00000010;
    margin-top: 10px;
    margin-bottom: 10px;
    padding: 10px;
    outline: none;
    position: relative;
}

.search__btn {
    box-shadow: 0 8px 8px 0 #00000010;
    border-radius: 15px;
    color: #96A7AF;
}

.search__btn.active {
    background-color: #FF8A34;
    color: #fff;
}

.search__btn_2 {
    box-shadow: 0 20px 20px 0 rgba(0,0,0,0.1) !important;
    height: 45px;
    width: 95px;
    position: relative;
    top: -2px;
    background-color: #FF8A34;
    color: white;
}

.search__btn_2:active {
    background-color: #ec721a;
    color: #fff;
}

.search__btn_2:focus, .search__btn_2:active {
    outline: none !important;
    box-shadow: none;
}

.search__lupa {
    position: relative;
    left: 440px;
    height: 44px;
    
}

.search__lupa:hover {
    cursor: pointer;
}

.sort__by {
    position: absolute;
    right: 10px;
    font-weight: 500;
}

.sort__by__active {
    color: orange !important;
}

span:hover {
    cursor: pointer;
}

.dropdown, .dropdown2{
  width: 220px;
  height: 45px;
  border-right: 1px solid #dde2f1;
  color: #9fa3b1;
  position: absolute;
  cursor: pointer;
  top: 10px;
  left: 705px;
  box-shadow: 0 8px 8px 0 #00000010;
}

.dropdown2{
  left: 925px;
}

.dropdown .default_option, .dropdown2 .default_option2{
  text-transform: uppercase;
  padding: 13px 15px;
  font-size: 14px;
}

.dropdown ul, .dropdown2 ul{
  position: absolute;
  top: 70px;
  left: 0px;
  background: #fff;
  width: 220px;
  border-radius: 5px;
  padding: 20px;
  display: none;
  box-shadow: 0px 14px 14px 0px #00000020;
  z-index: 2;
}

.dropdown ul.active, .dropdown2 ul.active{
  display: block;
}

.dropdown ul li, .dropdown2 ul li{
  padding-bottom: 20px;
  list-style-type: none;
}

.dropdown ul li:last-child, .dropdown2 ul li:last-child{
  padding-bottom: 0;
}

.dropdown ul li:hover, .dropdown2 ul li:hover{
  color: #6f768d;
}

.dropdown:before, .dropdown2:before{
  content: "";
  position: absolute;
  top: 18px;
  right: 20px;
  border: 8px solid;
  border-color: #A0B4C3 transparent transparent transparent;
}


@media screen and (max-width: 575px ) {
    .search {
        width: 100%;
        margin-bottom: 130px;
        border-radius: 15px;
    }

    .search__btn_2 {
        width: 100%;
    }

    .dropdown, .dropdown2 {
        left: 0px;
        top: 65px;
        width: 95%;
        margin-left: 0.5rem;
    }

    .dropdown2 {
        top: 130px;
    }

    .dropdown ul, .dropdown2 ul{
        width: 100%;
    }
}

</style>