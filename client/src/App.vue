<template>
  <div class="container">
    <h1>Список людей</h1>

    <input v-model="name" placeholder="Введите имя" />
    <button @click="addPerson">Добавить</button>

    <ul>
      <li v-for="person in people" :key="person.id">{{ person.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      name: '',
      people: [],
    }
  },
  methods: {
    async fetchPeople() {
      const res = await axios.get('/api/people/')
      this.people = res.data
    },
    async addPerson() {
      if (!this.name.trim()) return
      await axios.post('/api/people/', { name: this.name })
      this.name = ''
      await this.fetchPeople()
    },
  },
  mounted() {
    this.fetchPeople()
  },
}
</script>

<style>
.container {
  padding: 2rem;
  font-family: sans-serif;
}
</style>
