# Quickstart Guide: Next.js Frontend for Todo Application

## Getting Started

### Prerequisites
- Node.js 18+ installed
- npm or yarn package manager
- Access to the backend API (FastAPI server)

### Environment Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Navigate to the frontend directory:
   ```bash
   cd apps/frontend
   ```

3. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

4. Create a `.env.local` file in the `apps/frontend` directory with the following content:
   ```
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
   NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:8000
   ```

   Adjust the URLs to match your backend server configuration.

### Running the Application

1. Start the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

2. Open your browser and navigate to `http://localhost:3000`

### Building for Production

1. Create a production build:
   ```bash
   npm run build
   # or
   yarn build
   ```

2. Start the production server:
   ```bash
   npm start
   # or
   yarn start
   ```

## Key Features

### Authentication
- Visit `/login` to log in with existing credentials
- Visit `/signup` to create a new account
- The `/dashboard` route is protected and requires authentication

### Task Management
- On the dashboard, you can create, read, update, and delete tasks
- Tasks are filtered by completion status (All, Pending, Completed)
- Each task can be marked as complete/incomplete or deleted

### Responsive Design
- The UI adapts to different screen sizes (mobile, tablet, desktop)
- On mobile, the add task button becomes sticky at the bottom

## Project Structure

```
apps/
└── frontend/
    ├── app/                 # Next.js App Router pages
    │   ├── layout.tsx       # Root layout
    │   ├── page.tsx         # Landing page
    │   ├── login/page.tsx   # Login page
    │   ├── signup/page.tsx  # Signup page
    │   └── dashboard/page.tsx # Dashboard page
    ├── components/          # Reusable UI components
    │   ├── ui/              # Base UI components
    │   ├── auth/            # Authentication components
    │   ├── dashboard/       # Dashboard components
    │   └── layout/          # Layout components
    ├── lib/                 # Shared utilities
    │   ├── api.ts           # API client
    │   └── auth.ts          # Authentication utilities
    ├── hooks/               # Custom React hooks
    ├── styles/              # Global styles
    │   └── globals.css      # Tailwind and custom styles
    └── public/              # Static assets
```

## API Integration

All API calls go through the centralized client in `lib/api.ts` which:
- Attaches JWT tokens to requests automatically
- Handles 401 errors globally
- Returns parsed JSON responses
- Provides typed responses

## Troubleshooting

### Common Issues

1. **API Connection Errors**: Ensure the backend server is running and the URLs in `.env.local` are correct.

2. **Authentication Issues**: Verify that the Better Auth configuration matches between frontend and backend.

3. **Build Errors**: Clear the cache with `npm run clean` and reinstall dependencies.

### Useful Commands

- `npm run dev` - Start development server
- `npm run build` - Create production build
- `npm run lint` - Run linter
- `npm run type-check` - Run TypeScript type checking