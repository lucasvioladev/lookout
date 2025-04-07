import time

def display_production():
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
        
    prod = r"""
                          :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

db    db d888888b  .d88b.  db       .d8b.       d8888b. d8888b. d88888b .d8888. d88888b d8b   db d888888b .d8888. 
88    88   `88'   .8P  Y8. 88      d8' `8b      88  `8D 88  `8D 88'     88'  YP 88'     888o  88 `~~88~~' 88'  YP 
Y8    8P    88    88    88 88      88ooo88      88oodD' 88oobY' 88ooooo `8bo.   88ooooo 88V8o 88    88    `8bo.   
`8b  d8'    88    88    88 88      88~~~88      88~~~   88`8b   88~~~~~   `Y8b. 88~~~~~ 88 V8o88    88      `Y8b. 
 `8bd8'    .88.   `8b  d8' 88booo. 88   88      88      88 `88. 88.     db   8D 88.     88  V888    88    db   8D 
   YP    Y888888P  `Y88P'  Y88888P YP   YP      88      88   YD Y88888P `8888Y' Y88888P VP   V8P    YP    `8888Y' 
    """
    print(prod)

def display_title():
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    title = r"""
=============================================================================================================
=============================================================================================================

db       .d88b.   .d88b.  db   dD  .d88b.  db    db d888888b      d8b   db d888888b  d888b  db   db d888888b 
88      .8P  Y8. .8P  Y8. 88 ,8P' .8P  Y8. 88    88 `~~88~~'      888o  88   `88'   88' Y8b 88   88 `~~88~~' 
88      88    88 88    88 88,8P   88    88 88    88    88         88V8o 88    88    88      88ooo88    88    
88      88    88 88    88 88`8b   88    88 88    88    88         88 V8o88    88    88  ooo 88~~~88    88    
88booo. `8b  d8' `8b  d8' 88 `88. `8b  d8' 88b  d88    88         88  V888   .88.   88. ~8~ 88   88    88    
Y88888P  `Y88P'   `Y88P'  YP   YD  `Y88P'  ~Y8888P'    YP         VP   V8P Y888888P  Y888P  YP   YP    YP    
=============================================================================================================
=============================================================================================================
  """
    print(title)

def get_input(valid_choices):
    """
    Get and validate user input.
    
    Args:
        valid_choices (list): List of valid input choices
        
    Returns:
        str: The user's validated input
    """
    while True:
        choice = input("\nEnter your choice: ")
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please try again.")