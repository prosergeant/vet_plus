<template>
<div class="mt-5">
    <CRow> 
        <CCol md='10' class="mx-auto">
            <CRow>
                <CCol md='4'>
                    <CCard class="p-1">
                        <CRow>
                            <CCol sm='10' class="text-center mx-auto">
                                <img :src="currMedData.photo" style="border-radius: 15px; width: 64px; height: 64px;" class="mb-3 mt-3">
                            </CCol>

                            <CCol sm='12' class="text-center mb-3">
                                <h4>{{currMedData.name}}</h4>
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
                                @click="editTab = false, infoTab = true"> Информация </CButton>
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
                                <CButton class="w-100"
                                        :class="doctorsTab ? 'pressed_tab' : '' "
                                        @click="doctorsTab = true"> Врачи </CButton>
                            </CCol>
                        </CRow>

                        <div v-if="doctorsTab">
                            <div v-for="i in docOfThisService" :key="i.id" class="mt-3">
                                <router-link :to="{name: 'doc', params: {id: i.id}}">
                                    <DocCardHorz :card="i" v-if="windowWidth > 575" />
                                    <DocCard :card="i" v-if="windowWidth < 575" class="mx-auto" />
                                </router-link>
                            </div>
                        </div>
                        
                    </CCard>

                </CCol>
            </CRow>
        </CCol>
    </CRow>
</div>


</template>

<script>
import { getAPI } from '../axios-api'
import DocCardHorz from '../components/DocCardHorzDefault.vue'
import DocCard from '../components/DocCard'

export default {
    name: "Services",
    components: {
        DocCardHorz,
        DocCard
    },
    data() {
        return {
            id: this.$route.params.id,
            windowWidth: window.innerWidth,
            is_auth: this.$store.state.is_auth,

            currMedData: [],
            dataIsLoaded: false,
            docOfThisService: [],

            infoTab: true,
            inputTab: false, 
            endedTab: false, 
            editTab: false,
            contactTab: false,
            serviceTab: false,
            doctorsTab: true, 

            userInfo: [],
            userID: 0,
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

        fetchCurrMedData()
        {
            getAPI.get(`/api/services/${this.id}/`)
            .then(res => {
                this.currMedData = res.data;
                this.dataIsLoaded = true;
            })

        },

        fetchDocOfThisService() {
            getAPI.post(`/api/get-docs-service/`, {'id': this.id}) 
            .then(res => {
                this.docOfThisService = res.data;

                for(var i = 0; i < this.docOfThisService.length; i++) {
                    this.docOfThisService[i].photo = this.$store.state.base_url + this.docOfThisService[i].photo;
                }
            })
            .catch(err => {
                console.log("error while fetch get-docs-service: ", err);
            })
        },

    },
    mounted() {
        this.fetchCurrMedData();
        this.fetchDocOfThisService();
        //this.fetchMedReviewData();
        this.fetchUserInfo();
    },
    computed: {
        b_dataIsLoaded() {
            if(this.dataIsLoaded){
                return true;
            } else {
                return false;
            }
        },
    },
    watch: {
        b_dataIsLoaded(res){
            if(res){
                //this.getDocOfThisMed();
                //this.viewsPlus();
            }
        },
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