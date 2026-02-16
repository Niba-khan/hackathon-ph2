// Label component
import { DetailedHTMLProps, LabelHTMLAttributes } from 'react';

interface LabelProps extends DetailedHTMLProps<LabelHTMLAttributes<HTMLLabelElement>, HTMLLabelElement> {
  required?: boolean;
}

const Label = ({ children, required, className = '', ...props }: LabelProps) => {
  const baseClasses = 'block text-sm font-medium text-gray-700';
  const requiredClass = required ? 'after:content-["_*"] after:ml-0.5 after:text-red-500' : '';
  
  const classes = `${baseClasses} ${requiredClass} ${className}`;

  return (
    <label className={classes} {...props}>
      {children}
    </label>
  );
};

export default Label;