<template>
    <div class="medcard">
        <img :src="card.fields.photo" class="medcard__image">
        <div class="medcard__content">
            <h3>{{card.fields.first_name}} {{ card.fields.last_name }}</h3>
            <hr>
            <p class="m-0 mb-1"> <strong> {{card.fields.position}} </strong> </p>
            <p class="m-0"> Время рабоы: <strong> {{card.fields.time_start | toTime}} - {{card.fields.time_end | toTime}} </strong> </p>
            <p class="m-0">{{card.fields.time_start | toTime}}-{{card.fields.time_end | toTime}}</p>
            <div class="medcard__rating">
                <span>{{card.fields.rating | oneDecimal}} </span>
                <span class="medcard__stars--active">{{card.fields.rating | noDecimal | toStars}}</span>
                <span class="medcard__stars--inactive">{{5 - card.fields.rating | toStars}}</span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "DocCardHorz",
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
  width: 100%;
  background-color: white;
  padding: 5px;
  margin-bottom: 10px;
  font-family: Helvetica;
  box-shadow: 0px 5px 18px 0px rgba(0,0,0,0.2);
  border-radius: 15px;
  transition: top 0.2s ease;
  top: 0;
  position: relative;
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
  width: 188px;
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

</style>