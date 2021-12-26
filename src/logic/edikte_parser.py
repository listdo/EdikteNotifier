import requests
from bs4 import BeautifulSoup


def get_dataset(URL, debug: bool = False):
    response = requests.get(URL)

    dataset = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find(lambda tag: tag.name == 'table')

        output_rows = []
        for table_row in table.findAll('tr')[1:]:
            columns = table_row.findAll('td')
            output_row = []

            for column in columns[1:-1]:
                for item in column.getText(";").split(";"):
                    output_row.append(item)

            output_rows.append(output_row)

        for row in output_rows:
            datarow = []
            data_part = row[0].split(" ")

            if data_part[0] == 'Versteigerung':
                datarow.append(data_part[0])
                datarow.append((data_part[1]).lstrip("(").rstrip(")"))

                address_part = row[1].split(" ")
                datarow.append(address_part[0])
                datarow.append(address_part[1])

                datarow.append(row[2])

                dataset.append(datarow)

        if debug:
            for row in dataset:
                print(row)

        return dataset
    else:
        print("ERROR: CANNOT ACCESS URL! DIT NOT GET 200 STATUS CODE!")
