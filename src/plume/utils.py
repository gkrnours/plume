from functools import wraps
from io import StringIO
import sys

from flask import request, render_template

def templated(template=None):
    """ Try to render a template for the decorated view
        Template can be computed from the view name

        If the view return something else than None or a dict, it will
        be passed as is to flask
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Run the view
            ctx = f(*args, **kwargs)
            # Create a context if needed
            if ctx is None:
                ctx = {}
            # Or return exotic value. A redirect for example
            elif not isinstance(ctx, dict):
                return ctx
            # Compute the template name if needed
            template_name = template
            if template_name is None:
                template_name = request.endpoint.replace('.', '/') + '.html'
            # Render
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout
