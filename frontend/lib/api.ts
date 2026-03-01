// Centralized API client with automatic JWT attachment
import { Task } from '../types/index';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'https://niba-farooq1-todo-app.hf.space';

// Helper to get the JWT token from wherever it's stored
const getToken = (): string | null => {
  // In a real app, you might get this from httpOnly cookie via an API route
  // or from a secure storage mechanism
  return localStorage.getItem('auth_token');
};

// Generic request function that attaches JWT token
const request = async (endpoint: string, options: RequestInit = {}) => {
  const url = `${API_BASE_URL}${endpoint}`;
  
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    ...(options.headers as Record<string, string> | undefined),
  };

  // Add authorization header if token exists
  const token = getToken();
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  const config: RequestInit = {
    headers,
    ...options,
  };

  const response = await fetch(url, config);

  // Handle 401 errors globally
  if (response.status === 401) {
    // Clear the token and redirect to login
    localStorage.removeItem('auth_token');
    window.location.href = '/login';
    throw new Error('Unauthorized: Please log in again');
  }

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.message || `API error: ${response.status}`);
  }

  return response.json();
};

// Specific API functions
export const getTasks = async (): Promise<Task[]> => {
  const response = await request('/api/tasks');
  return response.data;
};

export const createTask = async (taskData: Omit<Task, 'id' | 'userId' | 'createdAt' | 'updatedAt'>): Promise<Task> => {
  return request('/api/tasks', {
    method: 'POST',
    body: JSON.stringify(taskData),
  });
};

export const updateTask = async (taskId: string, taskData: Partial<Task>): Promise<Task> => {
  return request(`/api/tasks/${taskId}`, {
    method: 'PUT',
    body: JSON.stringify(taskData),
  });
};

export const toggleTask = async (taskId: string): Promise<Task> => {
  return request(`/api/tasks/${taskId}/toggle`, {
    method: 'PATCH',
  });
};

export const deleteTask = async (taskId: string): Promise<void> => {
  await request(`/api/tasks/${taskId}`, {
    method: 'DELETE',
  });
};

// Export the base request function for other endpoints
export default request;