from fetch import Fetch
from toExcel import ToExcel


def main():
    url = input("Enter the url: ")
    token = input('Enter the token ("Optional"): ')
    excel_file_name = input("Enter output excel file name: ") + ".xlsx"
    fetch = Fetch(url=url)
    if token:
        fetch.set_token(token)

    response = fetch.get()

    if fetch.check_response_status_code(response):
        response_body = response.json()
        toExcel = ToExcel(excel_file_name=excel_file_name, data=response_body)
        toExcel.convert_data_to_excel()


if __name__ == "__main__":
    main()
