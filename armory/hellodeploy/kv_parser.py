
def parse(kv_text):
    non_empty_lines = filter(lambda x: x.strip() != "", kv_text.split("\n"))
    no_comments = filter(lambda x: not x.startswith("#"), non_empty_lines)
    kv_pairs = map(lambda x: x.partition("=")[::2], no_comments)
    kv_no_spaces = map(lambda x: (x[0].strip(), x[1].strip()), kv_pairs)
    return dict(kv_no_spaces)
