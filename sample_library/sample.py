from sample_library.foo_pb2 import Foo

def __write():
    foo = Foo(foo=42, bar=3.14, baz=True)

    with open('foo.pb', 'wb') as f:
        f.write(foo.SerializeToString())

def read():
    __write()

    with open('foo.pb', 'rb') as f:
        foo = Foo().FromString(f.read())
        print(foo)
        return foo
