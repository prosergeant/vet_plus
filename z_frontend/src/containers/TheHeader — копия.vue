<template>
  <CHeader fixed with-subheader class="pr-5">

    <CHeaderNav class="d-md-down-none mr-auto"> <!-- class="d-md-down-none mr-auto" -->
      <CHeaderNavItem class="px-3">
        <router-link to='/'>
        <img width="72" src='/img/logo.png'>
        </router-link>
      </CHeaderNavItem>
    </CHeaderNav>

    <CHeaderNav>
      <CHeaderNavItem class="mx-4">
        <router-link to='/'>
          Стать партнером
        </router-link>
      </CHeaderNavItem>

      <CHeaderNavItem class="mx-4">
        <CButton @click="openSlide(1000000)">
          Контакты
        </CButton>
      </CHeaderNavItem>

      <!--
      <CHeaderNavItem class="pt-3">
        <CHeaderNavLink to='/job'>
            <p class="mob">Вы преподаватель ?</p>
        </CHeaderNavLink>
      </CHeaderNavItem>
      -->

      <CHeaderNavItem class="px-1">
        <CHeaderNavLink href='https://instagram.com' target="_blank">
            <CIcon name="cib-instagram" />
        </CHeaderNavLink>
      </CHeaderNavItem>
      <CHeaderNavItem class="px-1">
        <CHeaderNavLink href='https://wa.me/+77079099454/' target="_blank">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" role="img" class="c-icon c-icon-custom-size" height="16"><path d="M23.328 19.177c-0.401-0.203-2.354-1.156-2.719-1.292-0.365-0.13-0.63-0.198-0.896 0.203-0.26 0.391-1.026 1.286-1.26 1.547s-0.464 0.281-0.859 0.104c-0.401-0.203-1.682-0.62-3.203-1.984-1.188-1.057-1.979-2.359-2.214-2.76-0.234-0.396-0.026-0.62 0.172-0.818 0.182-0.182 0.401-0.458 0.604-0.698 0.193-0.24 0.255-0.401 0.396-0.661 0.13-0.281 0.063-0.5-0.036-0.698s-0.896-2.161-1.229-2.943c-0.318-0.776-0.651-0.677-0.896-0.677-0.229-0.021-0.495-0.021-0.76-0.021s-0.698 0.099-1.063 0.479c-0.365 0.401-1.396 1.359-1.396 3.297 0 1.943 1.427 3.823 1.625 4.104 0.203 0.26 2.807 4.26 6.802 5.979 0.953 0.401 1.693 0.641 2.271 0.839 0.953 0.302 1.823 0.26 2.51 0.161 0.76-0.125 2.354-0.964 2.688-1.901 0.339-0.943 0.339-1.724 0.24-1.901-0.099-0.182-0.359-0.281-0.76-0.458zM16.083 29h-0.021c-2.365 0-4.703-0.641-6.745-1.839l-0.479-0.286-5 1.302 1.344-4.865-0.323-0.5c-1.318-2.099-2.021-4.521-2.021-7.010 0-7.26 5.943-13.182 13.255-13.182 3.542 0 6.865 1.38 9.365 3.88 2.5 2.479 3.88 5.802 3.88 9.323-0.010 7.255-5.948 13.177-13.25 13.177zM27.359 4.599c-3.042-2.938-7.042-4.599-11.297-4.599-8.776 0-15.922 7.115-15.927 15.859 0 2.792 0.729 5.516 2.125 7.927l-2.26 8.214 8.448-2.203c2.328 1.255 4.948 1.927 7.615 1.932h0.005c8.781 0 15.927-7.115 15.932-15.865 0-4.234-1.651-8.219-4.661-11.214z"></path></svg>
        </CHeaderNavLink>
      </CHeaderNavItem>

      <CHeaderNavItem class="pt-3 mr-3" v-if="auth">
        <router-link to='/profile'>
          <p>{{userdata.name}} <CBadge color="primary" v-if="bidsData.length != 0">{{bidsData.length}}</CBadge></p>
        </router-link>
      </CHeaderNavItem>
      <CHeaderNavItem class="pt-3" v-if="auth">
        <router-link to='/'>
          <p @click="logout">Выйти</p>
        </router-link>
      </CHeaderNavItem>
      <CHeaderNavItem class="" v-else>
        <CButton color="success" @click="loginModal = true"> Войти </CButton>
      </CHeaderNavItem>

      <CHeaderNavItem class="ml-2" v-if="auth == false">
        <CButton color="warning" @click="RegModal = true"> Регистрация</CButton>
      </CHeaderNavItem>

    </CHeaderNav>

    <CSubheader v-if="windowWidth > 575" class="px-3">
      <CRow class="w-100">
        <CCol sm='2' class="my-auto">
          <!-- <input type="text" class="form-control" placeholder="Поиск"> -->
          <div class="w-100"></div>
        </CCol>

        <CCol sm='2' class="my-auto">
          <CButton color="primary" class="w-100 h-75" @click="gotoPharmacy"> Аптеки </CButton>
        </CCol>

        <CCol sm='2' class="my-auto">
          <CButton color="primary" class="w-100 h-75" @click="gotoAllDocs"> Врачи </CButton>
        </CCol>
        
        <CCol sm='2' class="my-auto">
          <CButton color="primary" class="w-100 h-75" @click="gotoListOfVets"> Вет клиники </CButton>
        </CCol>

        <CCol sm='2' class="my-auto">
          <CButton color="primary" class="w-100 h-75" @click="gotoServices"> Услуги </CButton>
        </CCol>

        <CCol sm='2' class="my-auto">
          <CButton color="primary" class="w-100 h-75" @click="gotoVetShops"> Зоомагазин </CButton>
        </CCol>
      </CRow>
    </CSubheader>

   

    <!-- modal -->

    <CModal
      title="Вход"
      :show.sync="loginModal"
      size="lg"
      :centered=true
    >
    <CRow>
        <CCol sm='8' class="mx-auto">
          <p v-if="incorrectAuth">Не правильный логин или пароль</p>
          <CInput v-model="name" placeholder="Ваша почта" @keyup.enter="login"> </CInput>
          <CInput v-model="pass" placeholder="Ваш пароль" @keydown.enter="login"> </CInput>
        </CCol>
    </CRow>
    <template #footer>
        <CButton @click="loginModal = false" color="success">Закрыть</CButton>
        <CButton @click="login()" color="success">Войти</CButton>
    </template>
    </CModal>

    <!-- ----- -->


    <!-- modal register -->

    <CModal
      title="Регистрация"
      :show.sync="RegModal"
      size="lg"
      :centered=true
    >

    <CCol sm='8' class="mx-auto">
          <p v-if="passErr">Пароли не совпадают</p>
          <p v-if="emailErr">Не правильный формат почты</p>
          <p v-if="copyErr">Такой пользователь уже существует</p>
          <CInput v-model="email" placeholder="Ваша почта" @keyup.enter="register"> </CInput>
          <CInput v-model="pass" placeholder="Ваш пароль" @keyup.enter="register"> </CInput>
          <CInput v-model="pass2" placeholder="Повторите пароль" @keyup.enter="register"> </CInput>
    </CCol>

    <template #footer>
        <CButton @click="RegModal = false" color="success">Закрыть</CButton>
        <CButton @click="register()" color="success">Регистрация</CButton>
    </template>
    </CModal>

    <!-- ----- -->

  </CHeader>
</template>



<script>
import { getAPI } from '../axios-api'
import TheHeaderDropdownAccnt from './TheHeaderDropdownAccnt'

export default {
  name: 'TheHeader',
  components: {
    TheHeaderDropdownAccnt
  },
  data() {
    return {
      auth: this.$store.state.is_auth || false,
      loginModal: false,
      RegModal: false,
      incorrectAuth: false,
      userdata: [],
      name: null,
      email: null,
      pass: null,
      pass2: null,
      emailErr: false,
      passErr: false,
      copyErr: false,
      success_register: false,
      windowWidth: window.innerWidth,
      txt: '',

      bidsData: [],
      bidsDataComplete: []
    }
  },
  watch: {
    windowWidth(newWidth, oldWidth) {
     this.txt = `it changed to ${newWidth} from ${oldWidth}`;
    }
  },
  methods: {
    login(){
      //this.loginModal = false;
      this.name = this.name.toLowerCase();
      
      this.$store.dispatch('userLogin', {
          email: this.name,
          password: this.pass
        })
        .then(() => {
          this.$router.push({path: `/`})
          setTimeout(() => {
              this.$router.go(0);
          }, 100);
        })
        .catch(err => {
          console.log(err)
          this.incorrectAuth = true
        })
    },
    login2(email, pass){
      //this.loginModal = false;
      email = email.toLowerCase();
      
      this.$store.dispatch('userLogin', {
          email: email,
          password: pass
        })
        .then(() => {
          console.log("vse horosho2");
        })
        .catch(err => {
          console.log("vse ploho2 :C      : ", err);
        })
    },
    async register() {

      this.emailErr = false;
      this.passErr = false;
      this.copyErr = false;
      //this.success_register = false;

      if (!this.validEmail(this.email))
      {
          this.emailErr = true;
      } else if (!this.pass || this.pass != this.pass2) {
          this.passErr = true;
      } else {

        /*
        const today = new Date();
        const day = today.getDate();
        const month = today.getMonth() + 1;
        const year = today.getFullYear();

        let full_date = String(day) + " " + String(month) + " " + String(year);
        console.log("full_date: ", full_date);
        */

       this.email = this.email.toLowerCase();

      let data = {
        "password": this.pass,
        "email": this.email,
        "phone": null,
        "cashback": 0,
        "money": 0,
        "last_login": "0",
        "is_superuser": false,
        "is_staff": false,
        "is_active": true,
        //"date_joined": full_date,
        "is_doctor": false,
        "is_simpleuser": true,
        "first_name": "",
        "last_name": "",
        "text": "",
        "exp": 0,
        "address": null,
        "time_start": null,
        "time_end": null,
        "price": 0,
        "rating": 0.0,
        "med": null,
        "groups": [],
        "user_permissions": []
      }

      await getAPI.post(`/api/create-user/`, data)
      .then(res => {
        console.log(res);
        console.log('user added');
        this.success_register = true;
        //this.$router.push({path: 'login'})
        //this.$router.go('/pages/login/');
      })
      .catch(err => {
        console.log('error getAPI user add');
        console.log(err);
        this.copyErr = true;
      })

      if(this.success_register == true){
        
        this.login2(this.email, this.pass);

        setTimeout(() => {
          this.$router.go(0);
        }, 500);
      }
      }
    },
    validEmail: function (email) {
        var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
    },
    logout() {
      setTimeout(() => {
        this.$store.dispatch('userLogout');
        this.$router.go(0);
      }, 100);
    },
    getUserData(){
      getAPI.get(`/api/user-info/`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
      .then(res => {
        this.userdata = res.data;
        if(this.userdata.first_name == "") 
        {
          this.userdata.first_name = "Пользователь";
        }
        if(this.userdata.is_doctor) {
          this.getBids();
        }
        console.log('userdata: ', this.userdata);
      })
      .catch((error) => {
        if(error.response) {
          console.log('error fetch userdata');
          console.log(error.response.data);
          console.log(error.response.status);
          console.log(error.response.headers);

          if(error.response.data.code == "token_not_valid" && error.response.status == 401) {
            this.logout();
          }
        }
      })
    },
    gotoPharmacy() {
      this.$router.push('/pharmacy');
    },
    gotoAllDocs() {
      this.$router.push('/alldocs');
    },
    gotoListOfVets() {
      this.$router.push('/listofvets');
    },
    gotoServices() {
      this.$router.push(`/listofservices`);
    },
    gotoVetShops() {
      this.$router.push(`/listofvetshop`);
    },

    onResize() {
      this.windowWidth = window.innerWidth;
    },

    getBids() {
      getAPI.get(`/api/get-bid-curr-doc/${this.userdata.id}/`)
      .then(res => {
        let temp = [];

        for(var i = 0; i < res.data.length; i++) {
          if(res.data[i].is_completed == false) {
            temp.push(res.data[i]);
          }
        }

        this.bidsData = temp;
      })
      .catch(err => {
        console.log("error get bids for curr doc: ", err);
      })
    },

    async openSlide(offset){
        window.scrollTo({
            top: offset,
            behavior: 'smooth'
        });
    },
  },
  mounted() {
    if(this.auth){
      this.getUserData();
    }

    this.$nextTick(() => {
      window.addEventListener('resize', this.onResize);
    })
  },

  beforeDestroy() { 
    window.removeEventListener('resize', this.onResize); 
  },
}
</script>

