#data=[{"word":"little","score":1001},{"word":"fish","score":1000},{"word":"veit","score":999},{"word":"late","score":998},{"word":"brazilian","score":997},{"word":"852-3","score":996},{"word":"notorious","score":995},{"word":"young","score":994},{"word":"veil","score":993},{"word":"wet","score":992},{"word":"famous","score":991},{"word":"federal","score":990},{"word":"old","score":989},{"word":"real","score":988},{"word":"schultz","score":987},{"word":"savage","score":986},{"word":"hearted","score":985},{"word":"gallant","score":984},{"word":"wretched","score":983},{"word":"female","score":982},{"word":"lonesome","score":981},{"word":"only","score":980},{"word":"national","score":979},{"word":"maddening","score":978},{"word":"live","score":977},{"word":"alaskan","score":976},{"word":"musical","score":975},{"word":"creatures","score":974},{"word":"observed","score":973},{"word":"unappropriate","score":972},{"word":"artaud","score":971},{"word":"infamous","score":970},{"word":"hog","score":969},{"word":"the","score":968},{"word":"celebrated","score":967},{"word":"semi","score":966},{"word":"original","score":965},{"word":"actual","score":964},{"word":"half","score":963},{"word":"carnivora","score":962},{"word":"taker","score":961},{"word":"unknown","score":960},{"word":"injured","score":959},{"word":"historical","score":958},{"word":"800","score":957},{"word":"extraordinary","score":956},{"word":"romantic","score":955},{"word":"not","score":954},{"word":"feral","score":953},{"word":"chili","score":952},{"word":"criminal","score":951},{"word":"inter","score":950},{"word":"modernized","score":949},{"word":"california","score":948},{"word":"gentle","score":947},{"word":"how","score":946},{"word":"domestic","score":945},{"word":"pre","score":944},{"word":"lupine","score":943},{"word":"faced","score":942},{"word":"jawed","score":941},{"word":"ingenious","score":940},{"word":"implacable","score":939},{"word":"contemporary","score":938},{"word":"bright","score":937},{"word":"justice","score":936},{"word":"viet","score":935},{"word":"frequency","score":934},{"word":"curious","score":933},{"word":"goes","score":932},{"word":"honest","score":931},{"word":"eyed","score":930},{"word":"century","score":929},{"word":"villainous","score":928}]

#print(data[2],['word'])

import json

# JSON data retrieved from the API
data = [{"word":"wild","score":1001},{"word":"dry","score":1000},{"word":"common","score":999}]

# Function to extract and print adjectives
def print_adjectives(json_data):
    print("Adjectives:")
    for item in json_data:
        print(f"- {item['word']} (Score: {item['score']})")

# Pretty-print the JSON data
pretty_data = json.dumps(data, indent=4)
print("Pretty JSON Output:")
print(pretty_data)

# Print adjectives
print("\nTesting Adjectives Output:")
print_adjectives(data)
