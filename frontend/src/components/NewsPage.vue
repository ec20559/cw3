<!-- src/components/NewsPage.vue -->
<template>
  <div>
    <h1>Welcome to the News Page</h1>
    <div v-if="articles">
      <div v-for="category in articles" :key="category.category">
        <h2>{{ category.category }}</h2>
        <ul>
          <li v-for="article in category.articles" :key="article.id">
            <h3>{{ article.title }}</h3>
            <p>{{ article.contents }}</p>
            <!-- Add other fields as needed -->
          </li>
        </ul>
      </div>
    </div>
    <div v-else>
      <p>Loading news articles...</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      articles: null,
    };
  },
  async mounted() {
    await this.fetchNewsArticles();
  },
  methods: {
    async fetchNewsArticles() {
      try {
        const response = await fetch('http://localhost:8000/api/get_articles/', {
          credentials: 'include', // Include credentials (cookies)
        });

        // Read the response body only once
        const rawResponse = await response.text();
        console.log('Raw response:', rawResponse);

        // Parse the JSON
        const data = JSON.parse(rawResponse);
        console.log('News articles data:', data);
        this.articles = this.groupArticlesByCategory(data);
      } catch (error) {
        console.error('Error fetching news articles:', error);
      }
    },
    groupArticlesByCategory(articles) {
      // Group articles by category
      const groupedArticles = articles.reduce((acc, article) => {
        const category = article.topic;
        if (!acc[category]) {
          acc[category] = { category, articles: [] };
        }
        acc[category].articles.push(article);
        return acc;
      }, {});
      return Object.values(groupedArticles);
    },
  },
};
</script>

<style scoped>
/* Add your component styles here */
</style>
