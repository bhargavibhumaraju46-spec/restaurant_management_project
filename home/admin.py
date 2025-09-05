def generate_meta_description(description):
    meta_tag = f'<meta name="description" content="{description}">'
    return meta_tag
description = "welcome to our restaurant!"
meta_description_tag = generate_meta_description(description)
print(meta_description_tag)
print(f"Add this to the <head> section:\n{meta_description_tag}")    