import Vue from 'vue'
import Router from 'vue-router'

const TheContainer = () => import('@/containers/TheContainer')

const Start = () => import("@/views/Start")
const Doc = () => import("@/views/Doc")
const Med = () => import("@/views/Med")
const Services = () => import("@/views/Services")
const Profile = () => import("@/views/Profile")
const ListOfPharmacy = () => import("@/views/ListOfPharmacy")
const AllDocs = () => import("@/views/ListOfDocs")
const ListOfVets = () => import("@/views/ListOfVets")
const ListOfServices = () => import("@/views/ListOfServices")
const ListOfVetShops = () => import("@/views/ListOfVetShops")
const Search = () => import("@/views/Search")
const Partner = () => import("@/views/Partner")
const Contacts = () => import("@/views/Contacts")

const Test = () => import("@/views/Test")

Vue.use(Router)

export default new Router({
  mode: 'history', // https://router.vuejs.org/api/#mode
  linkActiveClass: 'active',
  scrollBehavior: () => ({ y: 0 }),
  routes: configRoutes()
})

function configRoutes () {
  return [
    {
      path: '/',
      name: 'Home',
      component: TheContainer,
      children: [
        {
          path: '',
          component: Start
        },
        {
          path: 'doc',
          component: { render(c) { return c("router-view") } },
          children: [
            {
              path: ':id',
              name: 'doc',
              component: Doc
            }
          ]
        },
        {
          path: 'med',
          component: { render(c) { return c('router-view') } },
          children: [
            {
              path: ':id',
              name: 'med',
              component: Med
            }
          ]
        },
        {
          path: 'services',
          component: { render(c) { return c('router-view') } },
          children: [
            {
              path: ':id',
              name: 'services',
              component: Services
            }
          ]
        },
        {
          path: 'profile',
          component: Profile
        },
        {
          path: 'pharmacy',
          component: ListOfPharmacy
        },
        {
          path: 'alldocs',
          component: AllDocs
        },
        {
          path: 'listofvets',
          component: ListOfVets
        },
        {
          path: 'listofservices',
          component: ListOfServices
        },
        {
          path: 'listofvetshop',
          component: ListOfVetShops
        },
        {
          path: 'search',
          component: Search
        },
        {
          path: 'partner',
          component: Partner
        },
        {
          path: 'contacts',
          component: Contacts
        },
        {
          path: 'test',
          component: Test
        }
      ]
    },
  ]
}

