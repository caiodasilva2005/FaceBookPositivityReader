import read_data as rd
import ui

def main():

    user = rd.user_init() # initizes data for user Caio DaSilva
    index = int(input("Enter The Page To View: [1: Test Page 2] [2: Test Page] --> "))
   
    ui.init(user.pages[index-1])
    
main()
    
    
