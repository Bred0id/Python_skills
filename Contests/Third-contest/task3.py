command_registry = {}


def register_command(func):
    command_registry[func.__name__] = func
    return func


def run_command(name, *args, **kwargs):
    if name not in command_registry:
        print(f"Команда '{name}' не найдена.")
        return None
    return command_registry[name](*args, **kwargs)
