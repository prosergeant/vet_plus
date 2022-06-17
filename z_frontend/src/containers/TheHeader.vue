<template>
  <div>
    <CHeader v-if="windowWidth > 575" style="position: fixed">

      <CHeaderNav class="mx-auto">
        <CHeaderNavItem class="px-3">
          <router-link to="/" class="no__border">
            <img width="118" height="61" src="/img/logo_1.svg" />
          </router-link>
          <!--<img src="/img/logo_title.svg" width="157" height="21" class="ml-2" />-->
        </CHeaderNavItem>

        <CHeaderNavItem class="mr-4">
          <!--<router-link to='/pharmacy'>-->
          <a @click="gotoPharmacy"> Аптеки </a>
          <!--</router-link>-->
        </CHeaderNavItem>

        <CHeaderNavItem class="mr-4">
          <a @click="gotoAllDocs"> Врачи </a>
        </CHeaderNavItem>

        <CHeaderNavItem class="mr-4">
          <a @click="gotoListOfVets"> Ветеринарные клиники </a>
        </CHeaderNavItem>

        <CHeaderNavItem class="mr-4">
          <a @click="gotoKinolog"> Кинологические центры </a>
        </CHeaderNavItem>

        <CHeaderNavItem class="mr-4">
          <a @click="gotoGrumery"> Груминг </a>
        </CHeaderNavItem>

        <CHeaderNavItem class="mr-4">
          <a @click="gotoServices"> Услуги </a>
        </CHeaderNavItem>

        <CHeaderNavItem class="mr-4">
          <a @click="gotoVetShops"> Зоомагазины </a>
        </CHeaderNavItem>

        <CHeaderNavItem class="mr-4">
          <a @click="gotoContacts"> Контакты </a>
        </CHeaderNavItem>

        <!--
      <CHeaderNavItem class="px-1 ">
        <CHeaderNavLink href='https://www.instagram.com/vetplus.kz' target="_blank">
            <CIcon name="cib-instagram" />
        </CHeaderNavLink>
      </CHeaderNavItem>
      -->

        <CHeaderNavItem class="mr-2">
          <CButton
            style="background-color: #ff8a34; color: #fff; border-radius: 15px"
            @click="gotoVetPartner"
          >
            Стать партнером
          </CButton>
        </CHeaderNavItem>

        <CHeaderNavItem class="pt-3 mr-3" v-if="auth">
          <router-link to="/profile">
            <p>
              {{ userdata.name }}
              <CBadge color="primary" v-if="bidsData.length != 0">{{
                bidsData.length
              }}</CBadge>
            </p>
          </router-link>
        </CHeaderNavItem>
        <CHeaderNavItem class="pt-3" v-if="auth">
          <router-link to="/">
            <p @click="logout">Выйти</p>
          </router-link>
        </CHeaderNavItem>
        <CHeaderNavItem class="" v-else>
          <CButton
            style="background-color: #ff8a34; color: #fff; border-radius: 20px"
            @click="loginModal = true"
          >
            <img src="/img/login_btn.png" />
          </CButton>
        </CHeaderNavItem>

        <!--
      <CHeaderNavItem class="ml-2" v-if="auth == false">
        <CButton style="background-color: #FF8A34; color: #fff;" @click="RegModal = true"> Регистрация</CButton>
      </CHeaderNavItem>
      -->
      </CHeaderNav>
    </CHeader>

    <div
      v-if="windowWidth < 575 && menu == false"
      style="position: fixed; z-index: 10; background: white"
      class="w-100"
    >
      <div style="justify-content: space-between; display: flex;" class="px-3 py-1">
        <router-link to="/" style="border:none;">
          <img src="/img/logo_1.svg" height="54" />
        </router-link>
        <img src="/img/menu_btn.svg" @click="menu = true" />
      </div>
      
    </div>

    <!-- phone menu -->
    <div 
    v-if="windowWidth < 575 && menu" 
    class="pt-3" 
    style="background-color: #fff;" 
    :style="menu ? 'z-index: 20; width: 100%; height: 100vh; position:fixed;' : 'z-index: 0; width: 0; height: 0;' "
    @click="menu = false">
      <p class="border-shmorder-140">Меню</p>
      <br>
      <p class="ml-5" style="font-size: 18px; font-weight: 600;" @click="menu = false, gotoPharmacy()">Аптеки</p>
      <p class="ml-5" style="font-size: 18px; font-weight: 600;" @click="menu = false, gotoAllDocs()">Врачи</p>
      <p class="ml-5" style="font-size: 18px; font-weight: 600;" @click="menu = false, gotoListOfVets()">Ветеринарные клиники</p>
      <p class="ml-5" style="font-size: 18px; font-weight: 600;" @click="menu = false, gotoKinolog()">Кинологические центры</p>
      <p class="ml-5" style="font-size: 18px; font-weight: 600;" @click="menu = false, gotoGrumery()">Груминг</p>
      <p class="ml-5" style="font-size: 18px; font-weight: 600;" @click="menu = false, gotoServices()">Услуги</p>
      <p class="ml-5" style="font-size: 18px; font-weight: 600;" @click="menu = false, gotoVetShops()">Зоомагазины</p>
      <p class="ml-5" style="font-size: 18px; font-weight: 600;" @click="menu = false, gotoContacts()">Контакты</p>

      <img src="/img/partner_phone.svg" class="w-75 mx-auto d-block" @click="menu = false, gotoVetPartner()" />
      <br>
      <img v-if="auth == false" src="/img/login_phone.svg" class="w-75 mx-auto d-block" @click="menu = false, loginModal = true" />
      <router-link v-if="auth" to="/profile">
        <img src="/img/login_phone.svg" class="w-75 mx-auto d-block" />
      </router-link>
      <span v-if="auth" @click="logout" class="mx-auto d-block w-50 mt-4 text-center" style="border-bottom: 1px dashed black;">Выйти из аккаунта</span>
    </div>


    <!-- modal -->

    <CModal
      :rounded="true"
      :login="true"
      title="Вход"
      :show.sync="loginModal"
      size="md"
      :centered="true"
    >
      <CRow>
        <CCol sm="8" class="mx-auto">
          <p v-if="incorrectAuth" style="font-size: 12px" class="m-0">
            Не правильный логин или пароль
          </p>
          <CInput label="Почта" v-model="name" @keyup.enter="login"> </CInput>
          <CInput
            label="Пароль"
            :type="showPass ? 'text' : 'password'"
            v-model="pass"
            @keydown.enter="login"
          >
          </CInput>
          <CInputCheckbox
            :checked="showPass"
            @click="showPass = !showPass"
            label="Показать пароль"
          />
        </CCol>

        <CCol sm="12" class="mt-2">
          <CButton
            class="orange__btn mx-auto d-block w-25"
            style="border-radius: 15px"
            @click="login()"
          >
            Войти
          </CButton>
        </CCol>

        <CCol sm="12" class="mt-2">
          <CButton
            class="blue__btn mx-auto d-block w-50"
            style="border-radius: 15px"
            @click="(loginModal = false), (RegModal = true)"
          >
            Регистрация
          </CButton>
        </CCol>
      </CRow>
    </CModal>

    <!-- ----- -->

    <!-- modal register -->

    <CModal
      title="Регистрация"
      :login="true"
      :reg="true"
      :show.sync="RegModal"
      size="lg"
      :centered="true"
    >
      <CCol sm="8" class="mx-auto">
        <p v-if="passErr" style="font-size: 12px" class="m-0">
          Пароли не совпадают
        </p>
        <p v-if="emailErr" style="font-size: 12px" class="m-0">
          Не правильный формат почты
        </p>
        <p v-if="copyErr" style="font-size: 12px" class="m-0">
          Такой пользователь уже существует
        </p>
        <CInput
          class="m-0"
          v-model="email"
          label="Почта"
          @keyup.enter="register"
        >
        </CInput>
        <CInput
          class="m-0"
          :type="showPass ? 'text' : 'password'"
          v-model="pass"
          label="Пароль"
          @keyup.enter="register"
        >
        </CInput>
        <CInput
          class="m-0"
          :type="showPass ? 'text' : 'password'"
          v-model="pass2"
          label="Повторите пароль"
          @keyup.enter="register"
        >
        </CInput>
        <CInputCheckbox
          :checked="showPass"
          @click="showPass = !showPass"
          label="Показать пароль"
        />
      </CCol>

      <CCol sm="12" class="mt-4">
        <CButton
          class="blue__btn mx-auto d-block w-50"
          style="border-radius: 15px"
          @click="register()"
        >
          Регистрация
        </CButton>
      </CCol>

      <p style="font-size: 10px" class="text-center mt-1">
        Регистрируясь вы соглашаетесь с <br />
        <a style="font-size: 10px" href="/privacy.pdf"
          >политикой конфиденциальности</a
        >
        <br />
        и
        <a style="font-size: 10px" href="agreement.pdf"
          >пользовательским соглашением</a
        >
      </p>
    </CModal>

    <!-- ----- -->
  </div>
</template>



<script>
import { getAPI } from "../axios-api";
import TheHeaderDropdownAccnt from "./TheHeaderDropdownAccnt";
import CModal from "../components/modal/CModalV2.vue";

export default {
  name: "TheHeader",
  components: {
    TheHeaderDropdownAccnt,
    CModal,
  },
  data() {
    return {
      auth: this.$store.state.is_auth || false,
      loginModal: false,
      RegModal: false,
      menu: false,

      userdata: [],
      name: null,
      email: null,
      pass: null,
      pass2: null,

      incorrectAuth: false,
      emailErr: false,
      passErr: false,
      copyErr: false,

      success_register: false,
      windowWidth: window.innerWidth,
      txt: "",

      bidsData: [],
      bidsDataComplete: [],

      showPass: false,
    };
  },
  watch: {
    windowWidth(newWidth, oldWidth) {
      this.txt = `it changed to ${newWidth} from ${oldWidth}`;
    },
  },
  methods: {
    login() {
      //this.loginModal = false;
      this.name = this.name.toLowerCase();

      this.$store
        .dispatch("userLogin", {
          email: this.name,
          password: this.pass,
        })
        .then(() => {
          

          this.$router.push({ path: `/` });
          setTimeout(() => {
            this.$router.go(0);
          }, 100);
        })
        .catch((err) => {
          console.log(err);
          this.incorrectAuth = true;
        });
    },
    login2(email, pass) {
      //this.loginModal = false;
      email = email.toLowerCase();

      this.$store
        .dispatch("userLogin", {
          email: email,
          password: pass,
        })
        .then(() => {
          console.log("vse horosho2");
        })
        .catch((err) => {
          console.log("vse ploho2 :C      : ", err);
        });
    },
    async register() {
      this.emailErr = false;
      this.passErr = false;
      this.copyErr = false;
      //this.success_register = false;

      if (!this.validEmail(this.email)) {
        this.emailErr = true;
      } else if (!this.pass || this.pass != this.pass2) {
        this.passErr = true;
      } else {
        this.email = this.email.toLowerCase();

        let data = {
          password: this.pass,
          email: this.email,
          phone: null,
          cashback: 0,
          money: 0,
          last_login: "0",
          is_superuser: false,
          is_staff: false,
          is_active: true,
          is_doctor: false,
          is_simpleuser: true,
          first_name: "",
          last_name: "",
          text: "",
          exp: 0,
          address: null,
          time_start: null,
          time_end: null,
          price: 0,
          rating: 0.0,
          med: null,
          groups: [],
          user_permissions: [],
        };

        await getAPI
          .post(`/api/create-user/`, data)
          .then((res) => {
            console.log(res);
            console.log("user added");
            this.success_register = true;
          })
          .catch((err) => {
            console.log("error getAPI user add");
            console.log(err);
            this.copyErr = true;
          });

        if (this.success_register == true) {
          this.login2(this.email, this.pass);

          setTimeout(() => {
            this.$router.go(0);
          }, 500);
        }
      }
    },
    validEmail: function (email) {
      var re =
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    },
    logout() {
      setTimeout(() => {
        this.$store.dispatch("userLogout");
        this.$router.go(0);
      }, 100);
    },
    getUserData() {
      getAPI
        .get(`/api/user-info/`, {
          headers: { Authorization: `Bearer ${this.$store.state.accessToken}` },
        })
        .then((res) => {
          this.userdata = res.data;
          if (this.userdata.first_name == "") {
            this.userdata.first_name = "Пользователь";
          }
          if (this.userdata.is_doctor) {
            this.getBids();
          }
          //console.log("userdata: ", this.userdata);
          localStorage.setItem('user_id', this.userdata.id)
        })
        .catch((error) => {
          if (error.response) {
            console.log("error fetch userdata");
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);

            if (
              error.response.data.code == "token_not_valid" &&
              error.response.status == 401
            ) {
              this.logout();
            }
          }
        });
    },
    gotoPharmacy() {
      this.$router.push("/search?searchtxt=Аптека");
      setTimeout(() => {
        this.$router.go(0);
      }, 100);
    },
    gotoAllDocs() {
      this.$router.push("/search?searchtxt=Врач");
      setTimeout(() => {
        this.$router.go(0);
      }, 100);
    },
    gotoListOfVets() {
      this.$router.push("/search?searchtxt=Клиник");
      setTimeout(() => {
        this.$router.go(0);
      }, 100);
    },
    gotoServices() {
      this.$router.push(`/search?searchtxt=Услуг`);
      setTimeout(() => {
        this.$router.go(0);
      }, 100);
    },
    gotoVetShops() {
      this.$router.push(`/search?searchtxt=Магазин`);
      setTimeout(() => {
        this.$router.go(0);
      }, 100);
    },
    gotoKinolog() {
      this.$router.push(`/search?searchtxt=Кинолог`);
      setTimeout(() => {
        this.$router.go(0);
      }, 100);
    },
    gotoGrumery() {
      this.$router.push(`/search?searchtxt=Грум`);
      setTimeout(() => {
        this.$router.go(0);
      }, 100);
    },
    gotoVetPartner() {
      setTimeout(() => {
        this.$router.push(`/partner`);
      }, 100);
      
    },
    gotoContacts() {
      this.$router.push(`/contacts`);
    },

    onResize() {
      this.windowWidth = window.innerWidth;
    },

    getBids() {
      getAPI
        .get(`/api/get-bid-curr-doc/${this.userdata.id}/`)
        .then((res) => {
          let temp = [];

          for (var i = 0; i < res.data.length; i++) {
            if (res.data[i].is_completed == false) {
              temp.push(res.data[i]);
            }
          }

          this.bidsData = temp;
        })
        .catch((err) => {
          console.log("error get bids for curr doc: ", err);
        });
    },

    async openSlide(offset) {
      window.scrollTo({
        top: offset,
        behavior: "smooth",
      });
    },
  },
  mounted() {
    if (this.auth) {
      this.getUserData();
    }

    this.$nextTick(() => {
      window.addEventListener("resize", this.onResize);
    });
  },

  beforeDestroy() {
    window.removeEventListener("resize", this.onResize);
  },

  computed: {
    b_refreshErrors() {
      if (this.incorrectAuth || this.emailErr || this.passErr || this.copyErr) {
        return true;
      } else {
        return false;
      }
    },
  },
  watch: {
    b_refreshErrors(res) {
      if (res) {
        setTimeout(() => {
          this.incorrectAuth = false;
          this.emailErr = false;
          this.passErr = false;
          this.copyErr = false;
        }, 3000);
      }
    },
  },
};
</script>


<style scoped>
a {
  color: black;
  font-size: 16px;
}

p {
  color: #000 ;
}

a:hover {
  color: black;
  border-bottom: 1px solid black;
  cursor: pointer;
}

.no__border,
.no__border:hover {
  border: none;
}
</style>