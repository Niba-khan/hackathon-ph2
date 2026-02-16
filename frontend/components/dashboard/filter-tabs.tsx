import Button from '../ui/button';

interface FilterTabsProps {
  currentFilter: 'all' | 'pending' | 'completed';
  onFilterChange: (filter: 'all' | 'pending' | 'completed') => void;
}

export default function FilterTabs({ currentFilter, onFilterChange }: FilterTabsProps) {
  const filters = [
    { id: 'all', label: 'All Tasks' },
    { id: 'pending', label: 'Pending' },
    { id: 'completed', label: 'Completed' },
  ];

  return (
    <div className="flex rounded-lg bg-gray-100 p-1">
      {filters.map((filter) => (
        <button
          key={filter.id}
          className={`flex-1 rounded-md py-2 px-4 text-sm font-medium ${
            currentFilter === filter.id
              ? 'bg-white text-blue-600 shadow-sm'
              : 'text-gray-600 hover:text-gray-900'
          }`}
          onClick={() => onFilterChange(filter.id as 'all' | 'pending' | 'completed')}
        >
          {filter.label}
        </button>
      ))}
    </div>
  );
}