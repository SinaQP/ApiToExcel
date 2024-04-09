from fetch import Fetch
from toExcel import ToExcel

def main():
    url = input("Enter the url: ")
    token = input('Enter the token ("Optional"): ')
    excel_file_name = input("Enter output excel file name: ") + ".xlsx"
    page = 1
    have_pagination = '{page}' in url

    formatted_url = url.replace('{page}', str(page))
    fetch = Fetch(url=formatted_url)

    if token:
        fetch.set_token(token)
    toExcel = ToExcel(excel_file_name=excel_file_name, data=[])
    while have_pagination:
        response = fetch.get()

        if response.status_code != 200:
            break
        response_body = response.json()
        if not len(response_body):
            break
        toExcel.append_data(response_body)
        page += 1
        formatted_url = url.replace('{page}', str(page))
        fetch.update_url(formatted_url)
        toExcel.convert_data_to_excel()
        print("formatted_url:", formatted_url)
        print("len:", len(toExcel.data))

    toExcel.convert_data_to_excel()


if __name__ == "__main__":
    main()
