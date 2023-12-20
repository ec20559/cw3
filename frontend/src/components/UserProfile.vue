<template>
  <div class="user-profile">
    <h1>{{ userProfile.username }}</h1>
    <p>Email: {{ userProfile.email }}</p>
    <p>Date of Birth: {{ userProfile.date_of_birth }}</p>
    
    <div class="profile-picture">
      <label>Profile Picture:</label>
      <img :src="userProfile.profile_image" alt="Profile Image" v-if="userProfile.profile_image" />
    </div>
  </div>
</template>

<script>
export default {
  props: ['userProfile'], // Make sure you pass 'userProfile' as a prop
};
</script>

<style scoped>
/* Add your component styles here */
.profile-picture {
  margin-top: 10px;
}
</style>
