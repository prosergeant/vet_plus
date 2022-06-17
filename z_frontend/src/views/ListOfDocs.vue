<template>
    <div>
        <CRow>
            <CCol class="m-2" sm='3' v-for="i in allDocs" :key="i.id">
                <router-link :to="{name: 'doc', params: {id: i.id}}">
                <CCard class="w-100 h-100">
                    <CRow>
                        <CCol sm='5'>
                            <img :src="i.photo" class="w-100">
                        </CCol>

                        <CCol sm='7'>
                            <p>{{i.first_name}} {{i.last_name}}</p>
                            <p>{{i.position}}</p>
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
    name: 'ListOfDocs',
    data() {
        return {
            allDocs: []
        }
    },
    methods: {
        getAllDocsData() {
            getAPI.get(`/api/doc/`)
            .then(res => {
                var temp = [];
                console.log("res data: ", res.data);
                for(var i = 0; i < res.data.length; i++){
                    if(res.data[i].first_name != '' || res.data[i].last_name != '') {
                        if(res.data[i].is_doctor == true)
                            temp.push(res.data[i]);
                    }
                }
                this.allDocs = temp; //res.data;

            })
            .catch(err => {
                console.log("error while fetch alldocsdata: ", err);
            })
        }
    },
    mounted(){
        this.getAllDocsData();
    }
}
</script>