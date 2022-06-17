<template>
  <div :fixed="false" v-if="windowWidth > 575" style="   width: 100%;
                                min-height: 230px;
                                background-image: url('/img/footer_def.png');
                                background-repeat: round;
                                border: 0px;">
                                
       


      <p class="logo-text"
        :style="`left: ${logo_pos_x}px; top: 200px;`">ВетПлюс 2021</p>


        <img src="/img/footer_logo.svg" class="footer__logo"/> 

      <CRow >
        <CCol sm='3'>
          <div class="w-100"></div>
        </CCol>
        <CCol sm='5'>
          <p class="footer__btn">Политика конфиденциальности</p>
          <p class="footer__btn">Пользовательское соглашение</p>
          <p class="footer__btn" @click="gotoContacts">Контакты</p>
          
        </CCol>

        <CCol sm='2' class="mt-3">
          <p style="color: #fff; font-size: 17px;" class="m-0">Следите за нами: </p>
          <a href='https://www.instagram.com/vetplus.kz' target="_blank">
            <CIcon name="cib-instagram" />
          </a>

          <a href='https://www.google.kz' target="_blank">
            <CIcon name="cib-facebook" class="ml-2"/>
          </a>
        </CCol>

      </CRow>
      
  </div>
  <div v-else style="   width: 100%;
                        min-height: 260px;
                        background-image: url('/img/footer.png');
                        background-repeat: round;border: 0px;">

      <CRow>
        <CCol sm='12' class="text-center mt-5">
          <p style="color: #fff;">ВетПлюс 2021</p>
        </CCol>
      </CRow>

      <img src="/img/footer_logo.svg" class="footer__logo"/>

      <CRow>
        <CCol sm='12' class="text-center mt-3">
          <p style="color:#fff;">Политика конфиденциальности</p>
        </CCol>
      </CRow>

      <CRow>
        <CCol sm='6' style="width: 100px;" class="mx-auto">
          <a href='https://www.instagram.com/vetplus.kz' target="_blank" class="mr-3">
            <CIcon name="cib-instagram"  />
          </a>

          <a href='https://www.google.kz' target="_blank">
            <CIcon name="cib-facebook" class="ml-2"/>
          </a>
        </CCol>
      </CRow>

  </div>
</template>

<script>
export default {
  name: 'TheFooter',
  data() {
    return {
      windowWidth: window.innerWidth,
      logo_pos_x: 0
    }
  },
  methods: {
    async goTop(){
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    },

    gotoContacts() {
      this.$router.push(`/contacts`)
    }
  },
  mounted() {
    this.logo_pos_x = (this.windowWidth - 260 - 10) / 2;
  }
}
</script>

<style scoped>
a {
  color: #fff;
}

a:hover {
  color: blue;
}

.logo-text {
  font-size: 15px;
  width: 260px;
  color: #fff;
  position: relative;
  text-align: center;
  top: 150px;
}

.footer__btn {
  color: #fff;
  cursor: pointer;
  width: 240px;
  font-size: 17px;
}

.footer__logo {
  position: relative;
  top: 70px;
  left: calc(50% - 40px);
}

@media screen and (max-width: 575px) {
  .footer__logo {
    top: 10px;
  }
}
</style>
