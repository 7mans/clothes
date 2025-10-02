import axios from 'axios';

// Create an Axios instance
const api = axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL || 'http://localhost:8000',
  timeout: 10000, // 10 seconds timeout
  headers: {
    'Content-Type': 'application/json'
  }
});

// You can add interceptors here if needed (e.g., for token handling)

export default api;