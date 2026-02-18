import Image from 'next/image';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

interface NavItem {
  name: string;
  href: string;
  current: boolean;
}

export default function Sidebar() {
  const pathname = usePathname();
  
  const navigation: NavItem[] = [
    { name: 'Dashboard', href: '/dashboard', current: pathname === '/dashboard' },
    { name: 'Tasks', href: '/dashboard/tasks', current: pathname === '/dashboard/tasks' },
    { name: 'Settings', href: '/dashboard/settings', current: pathname === '/dashboard/settings' },
  ];

  return (
    <div className="hidden md:block md:w-64 md:flex-shrink-0">
      <div className="flex flex-col h-0 flex-1 bg-gray-100 border-r border-gray-200">
        <div className="flex-1 flex flex-col pt-5 pb-4 overflow-y-auto">
          <div className="flex items-center flex-shrink-0 px-4">
            <h1 className="text-lg font-bold text-gray-900">TodoApp</h1>
          </div>
          <nav className="mt-5 flex-1 px-2 space-y-1">
            {navigation.map((item) => (
              <Link
                key={item.name}
                href={item.href}
                className={`${
                  item.current
                    ? 'bg-gray-200 text-gray-900'
                    : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
                } group flex items-center px-2 py-2 text-sm font-medium rounded-md`}
              >
                {item.name}
              </Link>
            ))}
          </nav>
        </div>
        <div className="flex-shrink-0 flex border-t border-gray-200 p-4">
          <a href="#" className="flex-shrink-0 w-full group block">
            <div className="flex items-center">
              <div>
                <Image
                    src="/logo.png"
                    alt="Logo"
                    width={32}
                    height={32}
                   className="h-8 w-8"
                />
              </div>
              <div className="ml-3">
                <p className="text-sm font-medium text-gray-700 group-hover:text-gray-900">User Profile</p>
                <p className="text-xs font-medium text-gray-500 group-hover:text-gray-700">View profile</p>
              </div>
            </div>
          </a>
        </div>
      </div>
    </div>
  );
}