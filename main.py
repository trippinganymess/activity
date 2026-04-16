import requests
import json
from console import console

class githubClient:
    BASE_URL = "https://api.github.com/users/"
    def __init__(self, username):
        self.username = username
        
    def getEvents(self):
        return self.BASE_URL+self.username+"/events"
    
    def call(self):
        response = requests.get(self.getEvents(), timeout=10)
        return response
    
    def response_getter(self):
        response = self.call()
        if response.status_code == 200:
            return response   
        elif response.status_code == 503:
            console.print("Api is currently unservicable",style="error")
            return None
        elif response.status_code == 404:
            console.print("Wrong username", style="error")
            return None
        elif response.status_code == 403:
            console.print("can't access this page", style="error")
            return None
        else:
            console.print("Something went wrong!!", style="error")
            return None
        
        
    def sendOutput(self):
        """
        creates the logs based on the activity registered.
        
        param : response
        param : LatestEvents
        """

        Events = self.response_getter()
        if Events is not None:
            LatestEvents = Events.json()
            for event in LatestEvents:
                match event['type']:
                        case "IssueCommentEvent":
                            console.print(f"- made a comment in {event['repo']['name']} at {event['created_at']}", style="enter")
                        case "PushEvent":
                            console.print(f"- pushed into the  {event['repo']['name']} at {event['created_at']}",style="enter" )
                        case "IssuesEvent":
                            console.print(f"- opened an issue in {event['repo']['name']} at {event['created_at']}",style="enter")
                        case "PullRequestEvent":
                            console.print(f"- made a pull request in {event['repo']['name']} at {event['created_at']}",style="pull")
                        case "CreatedEvent":
                            console.print(f"- created {event['repo']['name']} at {event['created_at']}",style="enter")
                        case "WatchEvent":
                            console.print(f"- starred the {event['repo']['name']} at {event['created_at']}",style="enter")
                        case "ForkEvent":
                            console.print(f"- forked the {event['repo']['name']} at {event['created_at']}",style="pull")
                        case "CommitCommentEvent":
                            console.print(f"- made an commit to {event['repo']['name']} at {event['created_at']}",style="enter")
                        case "ReleaseEvent":
                            console.print(f"- publised a release in  {event['repo']['name']} at {event['created_at']}",style="release")
                        case _:
                            console.print(f"unknown activity registered!!{event['type']}",style="error")
        else:
                console.print("Something went wrong :simley:")
            
            
        

def main():
    username = console.input("Enter your github [i]your[/i] [bold red]account[/]? :smiley: ")
    user = githubClient(username)
    user.sendOutput()
main()



        

   



        