from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    chunk_size = int(chunk_size)
    result = []
    chunk = []

    for i, data in enumerate(list_data):
        chunk.append(data)
        if (i + 1) % chunk_size == 0:
            result.append(chunk)
            chunk = []

    if chunk:
        result.append(chunk)

    return result
