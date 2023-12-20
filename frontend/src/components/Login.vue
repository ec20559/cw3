<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="loginUser">
      <label for="username">Username:</label>
      <input type="text" v-model="username" required>
      <label for="password">Password:</label>
      <input type="password" v-model="password" required>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async loginUser() {
      try {
        const response = await fetch("/api/login/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
          }),
        });

        if (response.ok) {
          // Redirect or handle successful login
          console.log("Login successful");
        } else {
          // Handle login error
          console.error("Login failed");
        }
      } catch (error) {
        console.error("Error during login:", error);
      }
    },
  },
};
</script>

<style scoped>
/* Add your styling here */
</style>
