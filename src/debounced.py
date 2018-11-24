# Given a function f, and N return a debounced f of N milliseconds.

# That is, as long as the debounced f continues to be invoked, f itself will not 
# be called for N milliseconds.

from threading import Timer
from time import sleep


def debounce(wait):
    def decorator(fn):
        def debounced(*args, **kwargs):
            def call():
                fn(*args, **kwargs)

            try:
                debounced.t.cancel()
            except AttributeError:
                pass

            debounced.t = Timer(wait, call)
            debounced.t.start()

        return debounced
    return decorator


@debounce(1)
def func():
    print('>>>')


if __name__ == '__main__':
    for _ in range(10):
        func()
        sleep(0.2)
