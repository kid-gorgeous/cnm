from typing import List, TypeVar, Generic

T = TypeVar('T')
def reverse(items: List[T]) -> List[T]:
   return items[::-1]