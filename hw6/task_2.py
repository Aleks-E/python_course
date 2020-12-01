"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования


def instances_counter(cls):
    '''Some code'''
    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
"""

from typing import TypeVar

modified_class = TypeVar("modified_class", bound="ModifiedClass")


class SomeClass:
    ...


def instances_counter(decorating_class: "SomeClass") -> "modified_class":
    class ModifiedClass(decorating_class):
        def __init__(self, *args: any, **kwargs: any):
            super().__init__(*args, **kwargs)
            self.instance_count_old = None
            self.init_instance_count()

        class InitInstanceCount:
            instance_count = 0
            instance_count_old = None

        @classmethod
        def init_instance_count(cls: "ModifiedClass") -> None:
            cls.InitInstanceCount.instance_count += 1

        @classmethod
        def get_created_instances(cls: "ModifiedClass") -> int:
            return cls.InitInstanceCount.instance_count

        @classmethod
        def reset_instances_counter(cls: "ModifiedClass") -> int:
            cls.InitInstanceCount.instance_count_old = (
                cls.InitInstanceCount.instance_count
            )
            cls.InitInstanceCount.instance_count = 0
            return cls.InitInstanceCount.instance_count_old

    return ModifiedClass
