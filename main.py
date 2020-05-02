from profile_scrap import do_scrape
from model import get_suggestions

##############3333
###### scrape user details
scraped_record = do_scrape()

print("****** Information was collected ****************")
print(scraped_record)

print("**************** Suggested areas are: ******************")
print(get_suggestions(scraped_record))