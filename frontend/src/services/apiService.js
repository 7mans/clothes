import api from '../plugins/axios';

/**
 * A simple error handler to log errors and re-throw them.
 * @param {Error} error - The error object.
 * @param {string} message - A descriptive message for the error context.
 */
const handleError = (error, message) => {
  console.error(`${message}:`, error);
  // In a real app, you might want to show a notification to the user
  throw error;
};

/**
 * API service for all analysis-related operations.
 */
export const analysisApi = {
  /**
   * Uploads an image for analysis.
   * @param {File} file - The image file to upload.
   * @param {Function} onUploadProgress - A callback function to track upload progress.
   * @returns {Promise<Object>} The analysis result from the backend.
   */
  uploadImage(file, onUploadProgress) {
    const formData = new FormData();
    formData.append('file', file);
    
    return api.post('/api/v1/analysis', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      onUploadProgress
    }).catch(error => handleError(error, 'Image upload failed'));
  },

  /**
   * Fetches the list of all analysis history records.
   * @returns {Promise<Array>} A list of analysis history items.
   */
  getHistory() {
    return api.get('/api/v1/analysis/history')
      .catch(error => handleError(error, 'Failed to fetch history'));
  },

  /**
   * Fetches a single analysis result by its ID.
   * @param {string} id - The unique identifier of the analysis.
   * @returns {Promise<Object>} The detailed analysis data.
   */
  getAnalysis(id) {
    return api.get(`/api/v1/analysis/${id}`)
      .catch(error => handleError(error, `Failed to fetch analysis for ID ${id}`));
  },

  /**
   * Generates outfit recommendations based on analysis data.
   * @param {Object} analysisData - The data from a previous analysis.
   * @returns {Promise<Object>} The generated recommendations.
   */
  generateRecommendations(analysisData) {
    return api.post('/api/v1/analysis/recommendations', {
      analysis_data: analysisData
    }).catch(error => handleError(error, 'Failed to generate recommendations'));
  }
};

export default {
  analysis: analysisApi
};