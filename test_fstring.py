import io
from contextlib import redirect_stdout
import main

buf = io.StringIO()
with redirect_stdout(buf):
    main.main()
out = buf.getvalue().strip()
assert out == 'The sum of 1 and 2 is 3', out
print('f-string output test passed')
