// Custom hook for task-related data fetching
import useSWR from 'swr';
import { getTasks, createTask, updateTask, toggleTask, deleteTask } from '../lib/api';
import { Task } from '../types/index';

// Fetch tasks with SWR
export const useTasks = () => {
  const { data, error, mutate } = useSWR<Task[], Error>('/api/tasks', getTasks);

  return {
    tasks: data,
    isLoading: !error && !data,
    isError: error,
    mutate,
  };
};

// Create a new task
export const useCreateTask = () => {
  const { mutate } = useSWR<Task[], Error>('/api/tasks', getTasks);

  const create = async (taskData: { title: string; description?: string; completed?: boolean }) => {
    try {
      await createTask({ ...taskData, completed: taskData.completed ?? false });
      // Re-fetch the tasks to update the cache
      await mutate();
    } catch (error) {
      console.error('Failed to create task:', error);
      throw error;
    }
  };

  return { create };
};

// Toggle task completion
export const useToggleTask = () => {
  const { mutate } = useSWR<Task[], Error>('/api/tasks', getTasks);

  const toggle = async (taskId: string) => {
    try {
      await toggleTask(taskId);
      // Re-fetch the tasks to update the cache
      await mutate();
    } catch (error) {
      console.error('Failed to toggle task:', error);
      throw error;
    }
  };

  return { toggle };
};

// Delete a task
export const useDeleteTask = () => {
  const { mutate } = useSWR<Task[], Error>('/api/tasks', getTasks);

  const remove = async (taskId: string) => {
    try {
      await deleteTask(taskId);
      // Re-fetch the tasks to update the cache
      await mutate();
    } catch (error) {
      console.error('Failed to delete task:', error);
      throw error;
    }
  };

  return { remove };
};