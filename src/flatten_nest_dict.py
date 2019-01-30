# Write a function to flatten a nested dictionary. Namespace the keys with a 
# period.

# For example, given the following dictionary:
# {
#     "key": 3,
#     "foo": {
#         "a": 5,
#         "bar": {
#             "baz": 8
#         }
#     }
# }
# it should become:
# {
#     "key": 3,
#     "foo.a": 5,
#     "foo.bar.baz": 8
# }

# You can assume keys do not contain dots in them, i.e. no clobbering will occur.

def flatten(nested):
    result = {}

    def helper(dic, prefix):
        for key in dic:
            pre = key if not prefix else '{}.{}'.format(prefix, key)
            if isinstance(dic[key], dict):
                helper(dic[key], pre)
            else:
                result[pre] = dic[key]

    helper(nested, '')
    return result


if __name__ == '__main__':
    nested = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }
    print(flatten(nested))