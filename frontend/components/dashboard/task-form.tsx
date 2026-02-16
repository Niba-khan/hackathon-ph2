'use client';

import { useState } from 'react';
import Button from '../ui/button';
import Input from '../ui/input';

interface TaskFormProps {
  onCreate: (taskData: { title: string; description?: string }) => Promise<void>;
}

export default function TaskForm({ onCreate }: TaskFormProps) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!title.trim()) {
      setError('Title is required');
      return;
    }
    
    try {
      await onCreate({ title: title.trim(), description: description.trim() });
      setTitle('');
      setDescription('');
      setError('');
    } catch (err) {
      setError('Failed to create task. Please try again.');
      console.error(err);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-card p-6">
      <h2 className="text-lg font-medium text-gray-900 mb-4">Add New Task</h2>
      
      {error && (
        <div className="mb-4 p-3 bg-red-50 text-red-700 rounded-lg text-sm">
          {error}
        </div>
      )}
      
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <Input
            label="Task Title *"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="What needs to be done?"
            required
          />
        </div>
        
        <div>
          <Input
            label="Description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Add details..."
          />
        </div>
        
        <div className="pt-2">
          <Button type="submit" variant="primary" fullWidth>
            Add Task
          </Button>
        </div>
      </form>
    </div>
  );
}