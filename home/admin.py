class TeamMember:
    def __init__(self, name, role, image_url="placeholder.jpg", description=""):
        self.name = name
        self.role = roleself.image_url = image_url
        seld.description = description 
class OurTeamPage:
    def __init__(self):
        self.team_members.append(member)
    def display_team_members(self):
        print("Our Team:")
        for member in self.team_members:
            print(f"Name: {member.name}")
            print(f"Role: {member.role}")
            print(f"Image: {member.image_url}")
            print(f"Description: {member.description}")
            print("-" *20)
        our_team = OurTeamPage()
        our_team.add_team_member("John Doe", "Head Chef", description="Expert in culinary delights.")
        our_team.add_team_member("Jane smith", description="Friendly and efficient.")
        our_team.display_team_members()    
    
            