social_media_links = {
    "Facebook" : "https://www.facebook.com/restaurant_placeholder",
    "Instagram": "https://www.instagram.com/restaurant_placeholder",
    }
def add_social_media_to_footer(links):
    footer_content = "Follow us on:\n"
    for platform, link in links.item():
        footer_content += f"{platform}": {link}\n"
        rturn footer_content
    footer = add_social_media_to_footer(social_media_links)
    print(footer)                                 