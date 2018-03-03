<template>
  <div class="hello">
    <h2>Sıcaklık
      <label v-if="si_values.length">max: {{ maxFind(si_values) }}</label>
      <label v-if="si_values.length">min: {{ minFind(si_values) }}</label>
    </h2>
    <line-chart :data="dataset_si"></line-chart>
    <br>
    <h2>Işık
      <label v-if="tsl_values.length">max: {{ maxFind(tsl_values) }}</label>
      <label v-if="tsl_values.length">min: {{ minFind(tsl_values) }}</label>
    </h2>
    <line-chart :data="dataset_tsl"></line-chart>
</div>
</template>

<script>
import { HTTP } from '@/http-common'
import store from '@/store'
import { mapActions } from 'vuex'

export default {
  name: 'Hello',
  data () {
    return {
      msg: 'Welcome to Panda',
      dataset_si: [],
      istatistic: { max_si: 0, min_si: 0, max_tsl: 0, min_tsl: 0 },
      mail_si: [0, 0],
      mail_tsl: [0, 0],
      si_values: [],
      tsl_values: [],
      dataset_tsl: [],
      refreshTime: 5000,
      errors: [],
      data: ''
    }
  },
  computed: {
    currentRefreshTime () {
      return store.state.refreshTime
    },
    currentDataSi () {
      return store.state.data_si
    },
    dataSetSi () {
      return this.dataset_si
    },
    currentDataTsl () {
      return store.state.data_tsl
    },
    dataSetTsl () {
      return this.dataset_tsl
    }
  },
  methods: {
    ...mapActions(['setDataSi', 'pushDataSi', 'setDataTsl', 'pushDataTsl', 'setRefreshTime']),
    maxFind (arr) {
      var max = arr.reduce(function (a, b) {
        return Math.max(a, b)
      })
      return max
    },
    minFind (arr) {
      var min = arr.reduce(function (a, b) {
        return Math.min(a, b)
      })
      return min
    },
    sendMail () {
      HTTP.get(`/send-mail`).then(response => {
        console.log(response.data)
      }).catch(e => {
        this.errors.push(e)
      })
    },
    getSensorSi () {
      var self = this

      setInterval(function () {
        if (self.dataset_si.length > 6) {
          self.dataset_si.unshift()
          self.dataset_si.shift()
        }
        HTTP.get(`/si-sensor`).then(response => {
          var data = response.data
          self.data = data
          data = parseInt(data.split(' ')[0].split(':')[1])
          self.si_values.push(data)
          self.mail_si[0] = data
          self.dataset_si.push([new Date(), data])
          if (Math.abs(self.mail_si[0] - self.mail_si[1]) >= 5) self.sendMail()
          self.mail_si[1] = data
          if (self.istatistic['max_si'] < data) self.istatistic['max_si'] = data
          else self.istatistic['min_si'] = data
        }).catch(e => {
          this.errors.push(e)
        })
      }, this.refreshTime)
    },
    getSensorTsl () {
      var self = this

      setInterval(function () {
        if (self.dataset_tsl.length > 6) {
          self.dataset_tsl.unshift()
          self.dataset_tsl.shift()
        }
        HTTP.get(`/tsl-sensor`).then(response => {
          var data = response.data
          data = parseInt(data.split(' ')[0].split(':')[1])
          self.tsl_values.push(data)
          self.mail_tsl[0] = data
          self.dataset_tsl.push([new Date(), data])
          if (Math.abs(self.mail_tsl[0] - self.mail_tsl[1]) >= 5) self.sendMail()
          self.mail_tsl[1] = data
          if (self.istatistic['max_tsl'] < data) self.istatistic['max_tsl'] = data
          else self.istatistic['min_tsl'] = data
        }).catch(e => {
          this.errors.push(e)
        })
      }, this.refreshTime)
    }
  },
  created () {
    this.getSensorSi()
    this.getSensorTsl()
  }
}
</script>

<style>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #35495E;
}
</style>
