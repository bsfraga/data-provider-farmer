from asyncio import as_completed

from helpers.bs4_parser import BeautifulSoupParser
from helpers.four_devs import FourDevs
from models.company import CompanyModel
from models.person import PersonModel
from concurrent.futures import ThreadPoolExecutor, as_completed


if __name__ == '__main__':


    try:
        with ThreadPoolExecutor(max_workers=2) as executor:
            
            futures_company= [executor.submit(FourDevs().generate_company) for i in range(0, 100)]
            futures_persons = [executor.submit(FourDevs().generate_person) for i in range(0, 100)]
            

            companies = []
            persons =  []

            for future in as_completed(futures_company):
                companies.append(future.result())
         
            for future in as_completed(futures_persons):
                persons.append(future.result())
                
        for person in persons:
            if person:
                data = PersonModel(**person[0])
                if data:
                    data.save()
                    print(f'Person {data.nome} saved')

        for company in companies:
            if company:
                data = BeautifulSoupParser.parseHtml(company)
                if isinstance(data, dict) and len(data) > 0:
                    data = CompanyModel(**data)
                    if data:
                        data.save()
                        print(f'Company {data.nome} saved')

    except Exception as e:
        print(e)
