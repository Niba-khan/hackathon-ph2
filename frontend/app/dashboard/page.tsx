'use client';

import { useState } from 'react';
import { useTasks, useCreateTask, useToggleTask, useDeleteTask } from '../../hooks/use-tasks';
import TaskForm from '../../components/dashboard/task-form';
import TaskList from '../../components/dashboard/task-list';
import FilterTabs from '../../components/dashboard/filter-tabs';
import { isAuthenticated, redirectToLogin } from '../../lib/auth';

// Verify authentication on the client side
if (typeof window !== 'undefined' && !isAuthenticated()) {
  redirectToLogin();
}

export default function DashboardPage() {
  const [filter, setFilter] = useState<'all' | 'pending' | 'completed'>('all');
  const { tasks, isLoading, isError } = useTasks();
  const { create } = useCreateTask();
  const { toggle } = useToggleTask();
  const { remove } = useDeleteTask();

  if (isError) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold text-red-600">Error loading tasks</h2>
          <p className="text-gray-600">Please try again later</p>
        </div>
      </div>
    );
  }

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading your tasks...</p>
        </div>
      </div>
    );
  }

  // Filter tasks based on the selected filter
  const filteredTasks = tasks?.filter(task => {
    if (filter === 'pending') return !task.completed;
    if (filter === 'completed') return task.completed;
    return true; // 'all'
  }) || [];

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8 flex justify-between items-center">
          <h1 className="text-3xl font-bold text-gray-900">My Tasks</h1>
          <button 
            onClick={() => {
              localStorage.removeItem('auth_token');
              window.location.href = '/login';
            }}
            className="text-sm font-medium text-gray-500 hover:text-gray-700"
          >
            Logout
          </button>
        </div>
      </header>
      
      <main>
        <div className="max-w-3xl mx-auto py-6 sm:px-6 lg:px-8">
          <div className="px-4 py-6 sm:px-0">
            {/* Task Creation Form */}
            <div className="mb-8">
              <TaskForm onCreate={create} />
            </div>
            
            {/* Filter Tabs */}
            <div className="mb-6">
              <FilterTabs currentFilter={filter} onFilterChange={setFilter} />
            </div>
            
            {/* Task List */}
            <div>
              <TaskList 
                tasks={filteredTasks} 
                onToggle={toggle}
                onDelete={remove}
              />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}