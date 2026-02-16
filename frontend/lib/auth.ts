// Authentication utilities for the frontend

// Check if user is authenticated
export const isAuthenticated = (): boolean => {
  const token = localStorage.getItem('auth_token');
  // In a real app, you might also check if the token is expired
  return !!token;
};

// Get the current user's token
export const getToken = (): string | null => {
  return localStorage.getItem('auth_token');
};

// Store the authentication token
export const setToken = (token: string): void => {
  localStorage.setItem('auth_token', token);
};

// Remove the authentication token (logout)
export const removeToken = (): void => {
  localStorage.removeItem('auth_token');
};

// Get user info from token (decode JWT if needed)
export const getUserInfo = () => {
  const token = getToken();
  if (!token) return null;

  try {
    // Decode JWT token to get user info
    // This is a simplified version - in practice, you'd use a JWT library
    const parts = token.split('.');
    if (parts.length !== 3) return null;

    const payload = parts[1];
    // Add padding if needed
    const decodedPayload = atob(payload.replace(/-/g, '+').replace(/_/g, '/'));
    return JSON.parse(decodedPayload);
  } catch (error) {
    console.error('Error decoding token:', error);
    return null;
  }
};

// Redirect to login page
export const redirectToLogin = (): void => {
  window.location.href = '/login';
};

// Redirect to dashboard
export const redirectToDashboard = (): void => {
  window.location.href = '/dashboard';
};