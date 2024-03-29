import media_objects as mo
import read_data as rd
import score_calculator as sc
import ui

def main():

    page = rd.page_init()

    '''
    score = sc.getPagePositivityScore(page)

    print(sc.getMostPositiveMedia(sc.__all_comments__))
    print(sc.getMostPositiveMedia(sc.__all_posts__))
    print(sc.__all_reactions__)
    print(score)
    '''
    ui.init(page)
    
main()
    
    
