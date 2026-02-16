// Alert component for displaying messages
import { ReactNode } from 'react';

interface AlertProps {
  children: ReactNode;
  type?: 'error' | 'warning' | 'success' | 'info';
  className?: string;
}

const Alert = ({ children, type = 'info', className = '' }: AlertProps) => {
  const baseClasses = 'p-4 rounded-xl';
  
  const typeClasses = {
    error: 'bg-red-50 border border-red-200 text-red-700',
    warning: 'bg-yellow-50 border border-yellow-200 text-yellow-700',
    success: 'bg-green-50 border border-green-200 text-green-700',
    info: 'bg-blue-50 border border-blue-200 text-blue-700',
  };

  const classes = `${baseClasses} ${typeClasses[type]} ${className}`;

  return (
    <div className={classes}>
      <div className="text-sm">{children}</div>
    </div>
  );
};

export default Alert;