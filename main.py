import media_objects as mo
import read_data as rd

def main():
    page = rd.page_init()
    print(page.posts[1].comments[0].message)

main()
    
    
