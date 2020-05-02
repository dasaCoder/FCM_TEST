from profile_scrap import do_scrape
from model import get_suggestions

##############3333
###### scrape user details
scraped_record = do_scrape("https://www.linkedin.com/in/savindi/")

print("****** Information was collected ****************")
print(scraped_record)

print("**************** Suggested areas are: ******************")
suggestions = get_suggestions(scraped_record)[0]

if len(suggestions) > 0:
    print(suggestions[0])