# Components Specification: Next.js Frontend for Todo Application

## Overview
This document specifies the reusable components for the Next.js frontend of the Todo application. All components must follow the UI design principles defined in the main specification.

## Component Specifications

### 1. Navbar
**Purpose**: Provide consistent navigation across all pages.

**Props**:
- `isLoggedIn` (boolean): Determines whether to show auth vs public navigation
- `onLogout` (function): Callback for logout functionality when logged in

**Functionality**:
- Display logo/application name
- Show appropriate navigation links based on authentication status
- Include logout button when user is authenticated
- Responsive design that collapses on mobile

**Styling**:
- Fixed position at top of screen
- Background with subtle shadow
- Consistent spacing and padding
- Follow color palette (neutral background with primary accent for active items)

### 2. Sidebar (Desktop View)
**Purpose**: Provide secondary navigation and quick actions on desktop views.

**Props**:
- `user` (object): User information to display in sidebar

**Functionality**:
- Display user profile information
- Provide quick links to dashboard sections
- Collapsible on smaller screens

**Styling**:
- Fixed position on left side
- Width appropriate for desktop (not mobile)
- Follow color palette (neutral background)
- Subtle border separating from main content

### 3. TaskCard
**Purpose**: Display individual task information with interactive elements.

**Props**:
- `task` (object): Task object with id, title, description, completed status
- `onToggle` (function): Callback for toggling task completion
- `onDelete` (function): Callback for deleting task
- `onEdit` (function): Callback for editing task

**Functionality**:
- Display task title and description
- Show completion status with visual indicator
- Provide toggle button to mark task as complete/incomplete
- Provide edit button to modify task
- Provide delete button with confirmation

**Styling**:
- Rounded-xl card with subtle shadow
- Consistent padding and spacing
- Visual indication of completion status (line-through, faded appearance)
- Hover effects for interactive elements
- Follow color palette (neutral background with primary accent for interactive elements)

### 4. TaskList
**Purpose**: Display a collection of TaskCards with filtering capabilities.

**Props**:
- `tasks` (array): Array of task objects
- `onToggle` (function): Callback for toggling task completion
- `onDelete` (function): Callback for deleting task
- `onEdit` (function): Callback for editing task
- `filter` (string): Current filter (all, pending, completed)

**Functionality**:
- Render multiple TaskCards
- Apply current filter to displayed tasks
- Handle empty state when no tasks match filter
- Manage loading states during data fetching

**Styling**:
- Consistent spacing between cards
- Follow color palette
- Loading spinner during data fetch
- Empty state display when appropriate

### 5. TaskForm
**Purpose**: Provide interface for creating and editing tasks.

**Props**:
- `initialData` (object): Initial task data for editing (optional)
- `onSubmit` (function): Callback for form submission
- `onCancel` (function): Callback for canceling form (optional)

**Functionality**:
- Input field for task title
- Textarea for task description
- Submit button to create/update task
- Cancel button to discard changes (when editing)
- Form validation for required fields
- Disable submit button during submission

**Styling**:
- Rounded-xl card with subtle shadow
- Consistent spacing and padding
- Follow color palette
- Disabled state styling for submit button
- Error message display for validation

### 6. FilterTabs
**Purpose**: Allow users to filter tasks by completion status.

**Props**:
- `currentFilter` (string): Current active filter ('all', 'pending', 'completed')
- `onFilterChange` (function): Callback for filter selection

**Functionality**:
- Display three tabs for filtering options
- Highlight currently active filter
- Trigger filter change when tab is clicked

**Styling**:
- Horizontal tab layout
- Active tab with primary accent color
- Subtle border separating tabs
- Follow color palette
- Hover effects for interactive elements

### 7. EmptyState
**Purpose**: Display friendly message when no tasks are available.

**Props**:
- `message` (string): Message to display
- `icon` (string): Icon to display (optional)

**Functionality**:
- Show message indicating no items
- Optionally display relevant icon
- Potentially include call-to-action button

**Styling**:
- Centered content
- Muted text color
- Follow color palette
- Appropriate spacing and padding

### 8. LoadingSpinner
**Purpose**: Indicate loading state during data fetching operations.

**Props**: None

**Functionality**:
- Display animated spinner
- Indicate that content is loading

**Styling**:
- Circular spinner animation
- Primary accent color
- Appropriately sized
- Centered when used alone

### 9. ErrorAlert
**Purpose**: Display error messages to users in a consistent way.

**Props**:
- `message` (string): Error message to display
- `onDismiss` (function): Callback for dismissing the alert (optional)

**Functionality**:
- Display error message prominently
- Optionally provide dismiss button
- Follow accessibility standards for alerts

**Styling**:
- Warning/error color scheme
- Rounded-xl with border
- Clear visual distinction from other content
- Follow color palette (danger/red for errors)

### 10. ConfirmationModal
**Purpose**: Request user confirmation before performing destructive actions.

**Props**:
- `isOpen` (boolean): Whether modal is visible
- `title` (string): Modal title
- `message` (string): Confirmation message
- `onConfirm` (function): Callback for confirmation
- `onCancel` (function): Callback for cancellation

**Functionality**:
- Display modal overlay when open
- Show confirmation message and action buttons
- Handle confirmation and cancellation
- Close when backdrop is clicked (optional)

**Styling**:
- Overlay background
- Centered modal content
- Rounded-xl card with shadow
- Follow color palette
- Clear distinction between confirm and cancel buttons