<template>
<div class="mt-5">
    <CRow> 
        <CCol sm='10' class="mx-auto">
            <CCard>
                <div id='map' style="width: 100%; height: 400px;"></div>
            </CCard>
        </CCol>
    </CRow>
</div>
</template>

<script>
import DG from '2gis-maps'
export default {
    name: 'Test',
    data() {
        return {
            windowWidth: window.innerWidth,
            coordX: 0,
            coordY: 0,
            map: null
        }
    },
    methods: {
        onResize() {
            this.windowWidth = window.innerWidth;
        },

        getLocation() {
            this.$getLocation({
                enableHighAccuracy: false, //defaults to false
                timeout: 10000, //defaults to Infinity
                maximumAge: 0 //defaults to 0
                
            })
            .then(coordinates => {
                console.log(coordinates);
                this.coordX = coordinates.lat;
                this.coordY = coordinates.lng;
                this.setMap();
            });
        },

        setMap() {
            setTimeout(() => {
                this.map = new DG.map("map", {
                    center: [this.coordX, this.coordY],
                    zoom: 20,
                    // zoomControl: false,
                    minZoom: 10,
                    fullscreenControl: false,
                    scrollWheelZoom: false
                });

                DG.marker([this.coordX, this.coordY]).addTo(this.map);
            }, 200);
        },
    },
    mounted() {
        this.$nextTick(() => {
            window.addEventListener('resize', this.onResize);
        })

        this.getLocation();
    },

    beforeDestroy() { 
            window.removeEventListener('resize', this.onResize); 
    },
}
</script>

<style scoped>
h3 {
    background-color: red;
}
</style>