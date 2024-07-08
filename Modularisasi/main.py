from gempaterkini.data_extraction import data_extraction
from gempaterkini.data_extraction import show_data
if __name__ == "__main__":
    print("Aplikasi Utama")
    result = data_extraction()
    show_data(result)