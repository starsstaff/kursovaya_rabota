from pydantic import BaseModel



class ListingData:


    def __init__(self):
        self.mso = 5918.013

    def get_mso(self):
        return str(self.mso)

listing_data = ListingData()

a = listing_data.get_mso()

print(f'{a}')
