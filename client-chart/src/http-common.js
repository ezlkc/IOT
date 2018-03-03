import axios from 'axios'
const URL = 'http://localhost:5000'

export const HTTP = axios.create({
  baseURL: URL,
  headers: {
    'Access-Control-Allow-Origin': '*'
  }
})
