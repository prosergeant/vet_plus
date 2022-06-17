<template>
    <div class="doc-card">
        <img :src="card.photo" alt="Avatar">
        <p class="badge">Стаж {{card.exp}} лет</p>
        <div class="container">
            <br>
            <h4>{{card.first_name}} {{card.last_name}}</h4>
            
            <span class="badge_2"> ★ {{card.rating | oneDecimal}} </span>

            <!--
            <div class="medcard__rating">
                
                <span class="medcard__stars--active">{{card.rating | noDecimal | toStars}}</span>
                <span class="medcard__stars--inactive">{{5 - card.rating | toStars}}</span>
                <span class="ml-2">{{card.rating | oneDecimal}} </span>
            </div>
            -->

            <p>{{card.position}}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DocCard',
    props: {
        card: Array
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
    }
}
</script>

<style scoped>
.doc-card {
    height: 417px;
    width: 260px;
    background-color: white;
    padding: 5px;
    margin-bottom: 10px;
    font-family: Helvetica;
    box-shadow: 0px 1px 2px 0px rgba(0,0,0,0.2);
    border-radius: 15px;
    transition: top 0.2s ease;
    top: 0;
    position: relative;
    z-index: 1;
}

.doc-card:hover {
    /*top: -10px;*/
    text-decoration: none;
}

.doc-card img {
    display: inline-block;
    margin-right: 0px;
    margin-left: -5px;
    /*margin-top: 12px;*/
    margin-top: -5px;
    height: 200px;
    border-top-right-radius: 15px;
    border-top-left-radius: 15px;
    padding: 0;
    width: 260px;
    height: 285px;
    object-fit: cover;
}

.doc-card .badge {
    border: 1px solid orange;
    background-color: orange;
    color: white;
    font-size: 16px;
    font-weight: 100;
    position: absolute;
    right: 0px;
    top: 275px;
    margin-bottom: 0;
}

.doc-card .badge_2 {
    position: absolute;
    top: 10px;
    left: 20px;

    background-color: #FF8A34;
    color: white;
    width: 50px;
    font-size: 18px;
    border-radius: 10px;
    text-align: center;
}


.medcard__stars--active {
  color: orange;
  font-size: 18px;
}
.medcard__stars--inactive {
  color: #CCCCCC;
}

@media screen and (max-width: 575px) {
    .doc-card {
        width: 240px;
        height: 400px;
    }

    .doc-card img {
        width: 240px;
        }
}

</style>

