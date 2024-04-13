from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar('T')  # Declare a type variable for the entity type

# Classe abstracta genèrica en Python, mirar el model per vore el seu ús
class BaseDAO(Generic[T], ABC):
    @abstractmethod
    def get_all(self) -> List[T]:
        """Get all entities."""
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> T:
        """Get an entity by ID."""
        pass

    @abstractmethod
    def add(self, entity: T) -> None:
        """Add a new entity."""
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        """Update an existing entity."""
        pass

    @abstractmethod
    def delete(self, entity: T) -> None:
        """Delete an entity."""
        pass

    # You can add whatever method you think is worthy