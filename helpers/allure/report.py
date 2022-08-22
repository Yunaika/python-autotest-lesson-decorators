import sys
import types
from functools import wraps
from allure_commons.utils import func_parameters
from helpers.utils.utils import humanify
from allure_commons._allure import StepContext


def step(fn):
    @wraps(fn)
    def fn_with_logging(*args, **kwargs):
        is_method = (
                args
                and isinstance(args[0], object)
                and isinstance(getattr(args[0], fn.__name__), types.MethodType)
        )

        args_to_log = args[1:] if is_method else args
        args_and_kwargs_to_log_as_strings = [
            *map(str, args_to_log),
            *[f'{key}={value}' for key, value in kwargs.items()]
        ]
        args_and_kwargs_string = (
            (': ' + ', '.join(map(str, args_and_kwargs_to_log_as_strings)))
            if args_and_kwargs_to_log_as_strings
            else ''
        )

        title = (
            (f'[{args[0].__class__.__name__}] ' if is_method else '')
            + humanify(fn.__name__)
            + args_and_kwargs_string
        )

        fn_params = func_parameters(fn, *args, **kwargs)

        step_obj = StepContext(title, fn_params)
        step_obj.__enter__()

        result = fn(*args, **kwargs)

        step_obj.__exit__(*sys.exc_info())

        return result

    return fn_with_logging
