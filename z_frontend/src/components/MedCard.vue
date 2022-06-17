<template>
    <div class="medcard">
        <img :src="card.photo" class="medcard__image">
        <div class="medcard__content">
            <h3>{{card.name}}</h3>
            <hr>
            <img src="/img/card/location.svg" width="16" class="float-left mr-1" />
            <p class="m-0 mb-1">{{card.address}}</p>
            <img src="/img/card/call.svg" width="16" class="float-left mr-1" />
            <p class="m-0 mb-1">+7 {{card.phone}}</p>
            <img src="/img/card/time_circle.svg" width="16" class="float-left mr-1" />
            <p class="m-0">{{card.time_start | toTime}}-{{card.time_end | toTime}}</p>
            <span class="badge"> ★ {{card.rating | oneDecimal}} </span>
            <!--
            <div class="medcard__rating">
                <span>{{card.rating | oneDecimal}} </span>
                <span class="medcard__stars--active">{{card.rating | noDecimal | toStars}}</span>
                <span class="medcard__stars--inactive">{{5 - card.rating | toStars}}</span>
            </div>
            -->
        </div>
    </div>
</template>

<script>
export default {
    name: "MedCard",
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

.medcard {
    height: 160px;
    width: 310px;
    background-color: white;
    padding: 5px;
    margin-bottom: 10px;
    font-family: Helvetica;
    box-shadow: 0px 5px 5px 0px rgba(0,0,0,0.1);
    border-radius: 15px;
    transition: top 0.2s ease;
    top: 0;
    position: relative;
    z-index: 1;
    overflow: hidden;
}

/*
.medcard:hover {
    top: -10px;
}
*/

.medcard__image {
    display: inline-block;
    margin-right: 10px;
    margin-left: -10px;
    /*margin-top: 12px;*/
    margin-top: -5px;
    height: 160px;
    border-bottom-left-radius: 15px;
    border-top-left-radius: 15px;
    width: 40%;
    object-fit: cover;
}

.medcard__content {
    display: inline-block;
    position: relative;
    vertical-align: top;
    width: 180px; /*calc(100% - 120px);*/
    height: 150px;
    padding-top: 10px;
}

.medcard__content h3 {
    font-size: 16px;
    font-weight: 600;
}

.medcard__content hr {
    margin-top: 5px;
}

.medcard__content h3 {
    margin: 0;
}

.medcard__content .badge {
    position: absolute;
    top: 5px;
    left: -120px;

    background-color: #FF8A34;
    color: white;
    font-size: 14px;
    border-radius: 15px;
}

.medcard__rating {
    position: absolute;
    bottom: 0;
}

.medcard__stars--active {
    color: orange;
}
.medcard__stars--inactive {
    color: #CCCCCC;
}

@media screen and (max-width: 575px) {
    .medcard {
        width: 270px;
    }

    .medcard__content {
        width: 140px;
    }

    .medcard__content .badge {
        left: -100px;
    }
}

</style>