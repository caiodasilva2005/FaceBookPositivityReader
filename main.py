import read_data as rd
import ui

def main():

    user = rd.user_init()
    ui.init(user.pages[1])
    
main()
    
    
