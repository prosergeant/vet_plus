<template>
    <div>
        <CCard @click="pn = !pn" :class="pn ? 'active' : '' ">
            <p> Пн </p>
        </CCard>

        <CCard @click="vt = !vt" :class="vt ? 'active' : '' ">
            <p> Вт </p>
        </CCard>

        <CCard @click="sr = !sr" :class="sr ? 'active' : '' ">
            <p> Ср </p>
        </CCard>

        <CCard @click="cht = !cht" :class="cht ? 'active' : '' ">
            <p> Чт </p>
        </CCard>

        <CCard @click="pt = !pt" :class="pt ? 'active' : '' ">
            <p> Пт </p>
        </CCard>

        <CCard @click="sb = !sb" :class="sb ? 'active' : '' ">
            <p> Сб </p>
        </CCard>

        <CCard @click="vs = !vs" :class="vs ? 'active' : '' ">
            <p> Вс </p>
        </CCard>
    </div>
</template>

<script>
import { getAPI } from '../axios-api'
export default {
    name: "WeekWork",
    props: {
        save: Boolean,
        medID: Number
    },
    data() {
        return {
            pn: true,
            vt: true,
            sr: true,
            cht: true,
            pt: true,
            sb: false,
            vs: false,
        }
    },

    methods: {
        getMedData() {
            getAPI.get(`/api/med/${this.medID}/`)
            .then(res => {
                this.pn = res.data.pn;
                this.vt = res.data.vt;
                this.sr = res.data.sr;
                this.cht = res.data.cht;
                this.pt = res.data.pt;
                this.sb = res.data.sb;
                this.vs = res.data.vs;
            })
            .catch(err => {
                console.log("error load med data: ", err);
            })
        }
    },

    mounted() {
        this.getMedData();
    },

    computed: {
        b_save() {
            if(this.save) return true
            else return false
        }
    },
    watch: {
        b_save(res){
            if(res) {
                getAPI.patch(`/api/med/${this.medID}/`, 
                {pn: this.pn, 
                 vt: this.vt,
                 sr: this.sr,
                 cht: this.cht,
                 pt: this.pt,
                 sb: this.sb,
                 vs: this.vs})
                 .then(() => {
                     this.save = false
                 })
                 .catch(err => {
                     console.log("error patch med weekdays: ", err)
                 })
            }
        }
    }
}
</script>

<style scoped>
.card {
    width: 50px !important;
    text-align: center;
    float: left;
    margin-right: 4px;
    cursor: pointer;
}

.card p {
    margin: 5px 5px 5px 5px;
}

.card .active p {
    color: white;
}

.card .active {
    background-color: green;
}
</style>