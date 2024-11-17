# Bookshelf Permissions and Groups Setup

## Custom Permissions
- `can_view`: Allows viewing books.
- `can_create`: Allows creating books.
- `can_edit`: Allows editing books.
- `can_delete`: Allows deleting books.

## User Groups
- **Editors**: Can create and edit books.
- **Viewers**: Can only view books.
- **Admins**: Have all permissions.

## Usage
Use the `@permission_required` decorator to enforce permissions on views.