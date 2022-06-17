<template>
  <CDropdown
    inNav
    class="c-header-nav-items"
    placement="bottom-end"
    add-menu-classes="pt-0"
  >
    <template #toggler>
      <CHeaderNavLink>
        <div class="c-avatar">
          <img
            src="img/avatars/6.jpg"
            class="c-avatar-img "
          />
        </div>
      </CHeaderNavLink>
    </template>
    <CDropdownHeader tag="div" class="text-center" color="light">
      <strong>{{userEmail}}</strong>
    </CDropdownHeader>
    <p>Уровень: {{userData.lvl}}</p>
    <CProgress :value="userData.exp" :max="(userData.lvl+1)*10" show-percentage animated></CProgress>
    <br>
    <CDropdownHeader
      tag="div"
      class="text-center"
      color="light"
    >
      <strong>Настройки</strong>
    </CDropdownHeader>
    <CDropdownItem>
      <CIcon name="cil-user" /> Профиль
    </CDropdownItem>
    <CDropdownItem>
      <CIcon name="cil-settings" /> Настройки
    </CDropdownItem>
    <CDropdownDivider/>
    <CDropdownItem @click="logout">
      <CIcon name="cil-lock-locked" /> Выход
    </CDropdownItem>
  </CDropdown>
</template>

<script>
import { getAPI } from '../axios-api'

export default {
  name: 'TheHeaderDropdownAccnt',
  created(){
    getAPI.get(`/api/user-info/`, { headers: { Authorization: `Bearer ${this.$store.state.accessToken}` } })
    .then(res =>{
      this.userData = res.data;
      this.userEmail = this.userData.email;
    })
  },
  methods: {
    logout(){
      this.$store.dispatch('userLogout');
      this.$router.go(0);
    }
  },
  data () {
    return { 
      userData: [],
      userEmail: 'anonymous'
    }
  }
}
</script>

<style scoped>
  .c-icon {
    margin-right: 0.3rem;
  }
</style>