<!-- src/components/ProfilePage.vue -->
<template>
  <div v-if="user" class="user-profile">
    <h1>{{ user.username }}</h1>

    <!-- Check if email is available before displaying -->
    <p v-if="user.email">Email: {{ user.email }}</p>
    <!-- Check if date of birth is available before displaying -->
    <p v-if="user.date_of_birth">Date of Birth: {{ user.date_of_birth }}</p>
    
    <div class="profile-picture">
      <label>Profile Picture:</label>
      <img :src="user.profile_image" alt="Profile Image" v-if="user.profile_image" />
    </div>
  </div>
  <div v-else>
    <p>Loading user profile...</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: null,
    };
  },
  async mounted() {
    await this.fetchUserProfile();
  },
  methods: {
    async fetchUserProfile() {
      try {
        const response = await fetch('http://localhost:8000/api/get_user_profile/', {
          credentials: 'include', // Include credentials (cookies)
        });

        // Read the response body only once
        const rawResponse = await response.text();
        console.log('Raw response:', rawResponse);

        // Parse the JSON
        const data = JSON.parse(rawResponse);
        console.log('User profile data:', data);
        this.user = data;
      } catch (error) {
        console.error('Error fetching user profile:', error);
      }
    },
  },
};
</script>

<style scoped>
/* Add your component styles here */
.profile-picture {
  margin-top: 10px;
}

</style>

