import json
import re

from django.test import TestCase

# Create your tests here.
# str = re.escape('{{book}}')
# print(str)

with open('/bookdrf\\templates\\bookdrt\\test.html') as f:
    d = f.read()
#

# d = re.sub(r"{{\W*book*\W*}}",'java',d)

# books = {'java':'123', 'python':'344'}
books = {'java':23, 'python':30}
books = json.dumps(books)
print(type(books))
# books = set(books)
d = re.sub(r"{{\W*book*\W*}}",books,d)
print(d)
# books = ('java','python')
def safe_substitute(self, mapping=_sentinel_dict, /, **kws):
    if mapping is _sentinel_dict:
        mapping = kws
    elif kws:
        mapping = _ChainMap(kws, mapping)

    # Helper function for .sub()
    def convert(mo):
        named = mo.group('named') or mo.group('braced')
        if named is not None:
            try:
                return str(mapping[named])
            except KeyError:
                return mo.group()
        if mo.group('escaped') is not None:
            return self.delimiter
        if mo.group('invalid') is not None:
            return mo.group()
        raise ValueError('Unrecognized named group in pattern',
                         self.pattern)

    return self.pattern.sub(convert, self.template)