import re

nums_regex = re.compile(r"[0-9]+")
def normalize_dst_to_src_column(value):
    result = list(filter(lambda v: v != "", nums_regex.findall(str(value))))
    if len(result) == 0:
        return 0
    result = [int(x) for x in result]
    return sum(result)

def lematize_protocol(protocol):
    if "." in protocol:
        index = protocol.index(".")
        return protocol[:index]
    return protocol

def is_int(val):
    try:
        int(val)
        return True
    except:
        return False


