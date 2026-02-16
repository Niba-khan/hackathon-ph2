import { useState } from 'react';
import Button from '../ui/button';
import { Task } from '../../types';

interface TaskCardProps {
  task: Task;
  onToggle: (taskId: string) => Promise<void>;
  onDelete: (taskId: string) => Promise<void>;
}

export default function TaskCard({ task, onToggle, onDelete }: TaskCardProps) {
  const [showConfirmation, setShowConfirmation] = useState(false);

  const handleToggle = async () => {
    try {
      await onToggle(task.id);
    } catch (error) {
      console.error('Failed to toggle task:', error);
    }
  };

  const handleDelete = async () => {
    try {
      await onDelete(task.id);
      setShowConfirmation(false);
    } catch (error) {
      console.error('Failed to delete task:', error);
    }
  };

  return (
    <div className={`bg-white rounded-xl shadow-card p-5 ${task.completed ? 'opacity-70' : ''}`}>
      <div className="flex items-start">
        <input
          type="checkbox"
          checked={task.completed}
          onChange={handleToggle}
          className="mt-1 h-5 w-5 rounded border-gray-300 text-blue-600 focus:ring-blue-500"
        />
        
        <div className="ml-4 flex-1 min-w-0">
          <h3 className={`text-lg font-medium ${task.completed ? 'line-through text-gray-500' : 'text-gray-900'}`}>
            {task.title}
          </h3>
          
          {task.description && (
            <p className={`mt-1 text-sm ${task.completed ? 'line-through text-gray-400' : 'text-gray-600'}`}>
              {task.description}
            </p>
          )}
          
          <div className="mt-3 flex items-center text-xs text-gray-500">
            <span>Created: {new Date(task.createdAt).toLocaleDateString()}</span>
            {task.updatedAt !== task.createdAt && (
              <span className="ml-3">Updated: {new Date(task.updatedAt).toLocaleDateString()}</span>
            )}
          </div>
        </div>
        
        <div className="flex space-x-2">
          {!showConfirmation ? (
            <Button 
              variant="danger" 
              size="sm"
              onClick={() => setShowConfirmation(true)}
            >
              Delete
            </Button>
          ) : (
            <div className="flex space-x-2">
              <Button 
                variant="ghost" 
                size="sm"
                onClick={() => setShowConfirmation(false)}
              >
                Cancel
              </Button>
              <Button 
                variant="danger" 
                size="sm"
                onClick={handleDelete}
              >
                Confirm
              </Button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}