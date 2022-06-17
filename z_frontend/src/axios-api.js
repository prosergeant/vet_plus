import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'http://192.168.0.30:8000' // 'http://185.68.21.251',  
})

export { getAPI }