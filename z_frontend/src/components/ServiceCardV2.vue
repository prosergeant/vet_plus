<template>
    <div class="doc-card">
        <img :src="card.fields.photo" alt="Avatar">
        <div class="container">
            <br>
            <h4 class="text-center">{{card.fields.name}}</h4>
            <h4 v-html="html" class="text"></h4>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DocCard',
    props: {
        card: Array
    },
    computed: {
        html() {
            return this.card.fields.text
        }
    }
}
</script>

<style scoped>
.doc-card {
    height: 200px;
    width: 220px;
    background-color: #00000000;
    padding: 5px;
    margin-bottom: 10px;
    font-family: Helvetica;
    box-shadow: 0px 1px 2px 0px rgba(0,0,0,0.2);
    border-radius: 15px;
    transition: top 0.2s ease;
    top: 0;
    position: relative;
}

.doc-card:hover {
    /*top: -10px;*/
    text-decoration: none;
}

.doc-card img {
    display: inline-block;
    margin-right: 0px;
    margin-left: 60px;
    /*margin-top: 12px;*/
    margin-top: 5px;
    height: 200px;
    border-top-right-radius: 15px;
    border-top-left-radius: 15px;
    padding: 0;
    width: 77px;
    height: 77px;

}

.doc-card .text {
    font-size: 14px;
    text-align: center;
}

</style>

