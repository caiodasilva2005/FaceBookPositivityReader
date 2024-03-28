import media_objects as mo
import read_data as rd
import score_calculator as sc

def main():
    page = rd.page_init()
    score = sc.getPagePositivityScore(page)

    print(score)
    
main()
    
    
