<template>
    <div class="mt-5">
        
        <CRow>
            <CCol sm='11' class="mx-auto">
                <CCard>
                <div id="map" style="width:100%; height:400px"></div>
                </CCard>
            </CCol>
        </CRow>

        <CRow>
            <CCol sm='10' class="mx-auto">
                <CRow>
                    <CCol sm='6'>
                        <CCard class="card__contact">
                            <p style="font-size: 16px; font-weight: 600;">Головной офис </p>
                            <p style="font-size: 16px; font-weight: 600;" class="m-0">Адрес: </p>
                            <p class="m-0 mb-1"> г.Алматы, ул. Шевченко 85, ЖК Молодёжный</p>
                            <p class="m-0" style="font-size: 16px; font-weight: 600;">Телефоны: </p>
                            <p class="m-0">+7(777)448-88-33</p>
                            <p class="m-0">+7(747)373-79-00</p>
                            <p class="m-0" style="font-size: 16px; font-weight: 600;">E-mail: </p>
                            <p>vetpluskz@gmail.com</p>
                        </CCard>
                    </CCol>

                    <CCol sm='6'>
                        <CCard class="card__contact" v-if="done == false">
                            <p>Написать нам:</p>
                            <CInput label="Имя" v-model="name" />
                            <CInput label="E-mail" v-model="email"/>
                            <CInput label="Телефон" v-model="phone"/>
                            <CInput label="Текст сообщения" v-model="message"/>

                            <CButton class="blue__btn" @click="sendMessage" :disabled="btn_disable ? disabled : null "> Отправить </CButton>
                        </CCard>
                        <CCard class="card__contact" v-else>
                            <p class="text-center my-auto">Ваше сообщения отправлено</p>
                        </CCard>
                    </CCol>
                </CRow>
            </CCol>
        </CRow>

    </div>
</template>

<script>
import DG from '2gis-maps'
import { getAPI } from '../axios-api';
export default {
    name: 'Contacts',
    data() {
        return {
            map: null,
            name: '',
            phone: '',
            email: '',
            message: '',

            done: false,
            btn_disable: false
        }
    },

    methods: {
        setMap() {
            setTimeout(() => {
                this.map = new DG.map("map", {
                    center: [43.245896, 76.934775],
                    zoom: 20,
                    // zoomControl: false,
                    minZoom: 10,
                    fullscreenControl: false,
                    scrollWheelZoom: false
                });

                DG.marker([43.246096, 76.935075]).addTo(this.map);
            }, 100);
        },

        sendMessage() {
            this.btn_disable = true
            getAPI.post(`/api/partner-messages/`, {name: this.name, phone: this.phone, email: this.email, message: this.message})
            .then(() => {
                this.done = true;
            })
            .catch(err => {
                console.log("error send message: ", err)
            })
        }
    },
    mounted(){
        this.setMap()
    }
}
</script>

<style scoped>
.card__contact {
    padding: 20px;
    border: none;
    border-radius: 15px;
    box-shadow: 0 22px 22px 0 #00000011;
}
</style>