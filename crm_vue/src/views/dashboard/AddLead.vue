<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add lead</h1>
      </div>

      <div class="column is-12">
        <form @submit.prevent="submitForm">
          <div class="field">
            <label for="company">Company</label>
            <div class="control">
              <input
                type="text"
                name="company"
                id="company"
                class="input"
                v-model="company"
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
                v-model="contact_person"
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
                v-model="email"
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
                v-model="phone"
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
                v-model="website"
              />
            </div>
          </div>
          <div class="field">
            <label for="confidence">Confidence</label>
            <div class="control">
              <input
                type="number"
                name="confidence"
                id="confidence"
                class="input"
                v-model="confidence"
              />
            </div>
          </div>
          <div class="field">
            <label for="estimated_value">Confidence</label>
            <div class="control">
              <input
                type="number"
                name="estimated_value"
                id="estimated_value"
                class="input"
                v-model="estimated_value"
              />
            </div>
          </div>
          <div class="field">
            <label for="status">Status</label>
            <div class="control">
              <div class="select">
                <select name="status" id="status" v-model="status">
                  <option value="new">New</option>
                  <option value="contacted">Contacted</option>
                  <option value="inprogress">In progress</option>
                  <option value="lost">Lost</option>
                  <option value="won">Won</option>
                </select>
              </div>
            </div>
          </div>
          <div class="field">
            <label for="priority">Priority</label>
            <div class="control">
              <div class="select">
                <select name="priority" id="priority" v-model="priority">
                  <option value="low">Low</option>
                  <option value="medium">Medium</option>
                  <option value="high">High</option>
                </select>
              </div>
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" :key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success">Submit</button>
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
  name: 'AddLead',
  data() {
    return {
      company: '',
      contact_person: '',
      email: '',
      phone: '',
      website: '',
      confidence: 0,
      estimated_value: 0,
      status: 'new',
      priority: 'medium',
      errors: [],
    }
  },
  methods: {
    async submitForm() {
      this.errors = []

      if (this.company === '') {
        this.errors.push('The company is missing')
      }
      if (this.contact_person === '') {
        this.errors.push('The contact person is missing')
      }
      if (this.email === '') {
        this.errors.push('The email is missing')
      }
      if (this.phone === '') {
        this.errors.push('The phone is missing')
      }

      if (!this.errors.length) {
        this.$store.commit('setIsLoading', true)

        const lead = {
          company: this.company,
          contact_person: this.contact_person,
          email: this.email,
          phone: this.phone,
          website: this.website,
          estimated_value: this.estimated_value,
          confidence: this.confidence,
          status: this.status,
          priority: this.priority,
        }

        await axios
          .post('/api/v1/leads/', lead)
          .then((response) => {
            toast({
              message: 'The lead was added',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right',
            })

            this.$router.push('/dashboard/leads')
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