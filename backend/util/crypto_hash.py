import hashlib
import json


def crypto_hash(*args):
    """
    Unicode-objects must be encoded before hashing
    -->
    stringify data
    :return: a sha-256 hash of given arguments
    """

    # no matter what the order of input objects is,
    # should encrypt to the same result
    json_args = sorted(map(lambda data: json.dumps(data), args))

    print(f'args: {json_args}')
    joined_data = ''.join(json_args)

    print(f'joined_data: {joined_data}')

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()


def main():
    print(f"crypto_hash(): {crypto_hash(['1'],'df',324,'fewflfd')}")
    print(f"crypto_hash(): {crypto_hash(324,'df', ['1'],'fewflfd')}")


if __name__ == '__main__':
    main()
