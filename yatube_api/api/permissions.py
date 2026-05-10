from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Только аутентифицированные пользователи могут выполнять любые запросы.
    Изменять/удалять объекты может только их автор.
    """

    def has_permission(self, request, view):
        # Доступ к любому эндпоинту только для аутентифицированных
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Для безопасных методов (GET, HEAD, OPTIONS) – разрешено
        if request.method in permissions.SAFE_METHODS:
            return True
        # Для остальных методов – только автор объекта
        return obj.author == request.user
