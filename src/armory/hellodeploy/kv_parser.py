
def parse(kv_text):
    non_empty_lines = filter(lambda x: x.strip() != "", kv_text.split("\n"))
    kv_pairs = map(lambda x: x.partition("=")[::2], non_empty_lines)
    kv_no_spaces = map(lambda x: (x[0].strip(), x[1].strip()), kv_pairs)
    return dict(kv_no_spaces)
