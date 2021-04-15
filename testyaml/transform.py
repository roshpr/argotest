import yaml as pyyaml
import textwrap


def indent(text, amount, ch=' '):
    return textwrap.indent(text, amount * ch)


with open('hello.yaml', 'r') as f:
    data = pyyaml.safe_load(f)
    print(data)
    yaml_data = pyyaml.safe_dump(data)

    print(indent(yaml_data, 5))

# //////////
# foo = {
#     'name': 'foo',
#     'my_list': [{'foo': 'test', 'bar': 'test2', 'bar1': 'test2', 'bar2': 'test2'}, {'foo': 'test3', 'bar': 'test4'}],
#     'hello': 'world'
# }
# print('============================================================')
# yaml.indent(sequence=4, offset=2, mapping=2)
# yaml.dump(foo, sys.stdout)