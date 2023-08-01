"""Utility / helper script for breaking PDF files >60MB into smaller files"""


def run_chunker_loop():
    while True:
        u_input_size = int(float(input("What is file size?")))

        div = 1
        max_size = 60
        res_found = False

        while not res_found:
            result = u_input_size / div

            if result <= max_size:
                print(f"Num files: {div}")
                res_found = True

            else:
                div += 1

        page_num_input = int(input("How many pages?"))

        pages_per = page_num_input // div

        file_save_tag = 1
        page_start = 1
        page_end = pages_per

        while page_end <= page_num_input:
            if file_save_tag == div:
                page_end = page_num_input
            print(f"Pages {page_start} - {page_end}")
            print(f"file end tag --> '_{file_save_tag}'")
            print('\n'*4)
            file_save_tag += 1
            page_start = page_end + 1
            page_end += pages_per
            user_continue = input("Enter to continue...")


if __name__ == "__main__":
    run_chunker_loop()