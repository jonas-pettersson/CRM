<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Edit {{ client.name }}</h1>
      </div>

      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label for="name">Name</label>
            <div class="control">
              <input
                type="text"
                name="name"
                id="name"
                class="input"
                v-model="client.name"
              />
            </div>
          </div>
          <div class="field">
            <label for="contact_person">Contact person</label>
            <div class="control">
              <input
                type="text"
                name="contact_person"
                id="contact_person"
                class="input"
                v-model="client.contact_person"
              />
            </div>
          </div>
          <div class="field">
            <label for="email">Email</label>
            <div class="control">
              <input
                type="email"
                name="email"
                id="email"
                class="input"
                v-model="client.email"
              />
            </div>
          </div>
          <div class="field">
            <label for="phone">Phone</label>
            <div class="control">
              <input
                type="text"
                name="phone"
                id="phone"
                class="input"
                v-model="client.phone"
              />
            </div>
          </div>
          <div class="field">
            <label for="website">Website</label>
            <div class="control">
              <input
                type="text"
                name="website"
                id="website"
                class="input"
                v-model="client.website"
              />
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success">Update</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import { toast } from 'bulma-toast'

export default {
  name: 'EditClient',
  data() {
    return {
      client: {},
      errors: [],
    }
  },
  mounted() {
    this.getClient()
  },
  methods: {
    async getClient() {
      this.$store.commit('setIsLoading', true)

      const clientID = this.$route.params.id

      await axios
        .get(`/api/v1/clients/${clientID}/`)
        .then((response) => {
          this.client = response.data
        })
        .catch((error) => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    },

    async submitForm() {
      this.errors = []

      if (this.client.name === '') {
        this.errors.push('The name is missing')
      }
      if (this.client.contact_person === '') {
        this.errors.push('The contact person is missing')
      }
      if (this.client.email === '') {
        this.errors.push('The email is missing')
      }
      if (this.client.phone === '') {
        this.errors.push('The phone is missing')
      }

      if (!this.errors.length) {
        this.$store.commit('setIsLoading', true)

        await axios
          .patch(`/api/v1/clients/${this.client.id}/`, this.client)
          .then((response) => {
            toast({
              message: 'The client was updated',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right',
            })

            this.$router.push(`/dashboard/clients/${this.client.id}`)
          })
          .catch((error) => {
            console.log(error)
          })

        this.$store.commit('setIsLoading', false)
      }
    },
  },
}
</script>