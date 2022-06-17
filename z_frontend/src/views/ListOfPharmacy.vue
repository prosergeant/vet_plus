<template>
<div>
    <CRow>
        <CCol class="m-2" sm='6' v-for="i in allMeds" :key="i.id">
            <router-link :to="{name: 'med', params: {id: i.id}}">
            <CCard class="w-100">
                <CRow>
                    <CCol sm='5'>
                        <img :src="i.photo" class="w-100">
                    </CCol>

                    <CCol sm='7'>
                        <p>{{i.name}}</p>
                        <p>{{i.address}}</p>
                    </CCol>
                </CRow>
            </CCard>
            </router-link>
        </CCol>
    </CRow>
</div>
</template>

<script>
import { getAPI } from '../axios-api'
export default {
    name: 'ListOfVetShops',
    data() {
        return {
            allMeds: []
        }
    },
    methods: {
        fetchMedsData() {
            getAPI.get(`/api/med/`)
            .then(res => {
                for(var i = 0; i < res.data.length; i++) {
                    if(res.data[i].this_is == 3) {              // 1 - med center
                        this.allMeds.push(res.data[i]);         // 2 - zoo shop
                    }                                           // 3 - pharmacy
                }
            })
            .catch(err => {
                console.log("error fetch meds data: ", err);
            })
        }
    },
    mounted() {
        this.fetchMedsData();
    }
}
</script>
