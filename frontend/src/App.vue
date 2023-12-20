<template>
  <div>
    <UserProfile v-if="authenticated" :userProfile="userProfile" />
    <div v-else>
      <p>No user logged in</p>
    </div>
  </div>
</template>

<script>
import UserProfile from './components/UserProfile.vue';

export default {
  components: {
    UserProfile,
  },
  data() {
    return {
      authenticated: false,
      userProfile: {},
    };
  },
  mounted() {
    this.fetchUserProfile();
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
        this.userProfile = data;
        this.authenticated = true;
      } catch (error) {
        console.error('Error fetching user profile:', error);
      }
    },
  },
};
</script>

