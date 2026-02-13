class EventDispatcher:
    @staticmethod
    def log(func):
        def wrapper(event_type: str, *args, **kwargs):
            func_name = func.__name__
            
            args_str = ", ".join(map(str, args)) if args else None
            kwargs_list: list[str] = []
            kwargs_list = [f"{key}={value}"for key, value in kwargs.items()]
            kwargs_str =",".join(kwargs_list) if kwargs else None

            print(f"Event type:{event_type}")
            print(f"Function: {func_name}")
            print(f"Arguments: {args_str}")
            print(f"Keyword arguments: {kwargs_str}")
            result = func(event_type, *args, **kwargs)
            return result
        return wrapper

    @staticmethod
    @log
    def dispatch_event(event_type: str, *args, **kwargs):
        return f"Event '{event_type}' has been successfully routed."