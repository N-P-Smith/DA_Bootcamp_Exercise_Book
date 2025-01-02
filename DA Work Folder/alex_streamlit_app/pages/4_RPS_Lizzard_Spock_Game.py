
import streamlit as st
import random
import time

st.sidebar.markdown(""" 
#
# ----- The Game ----- """)

# 1. get the player's name
player_name = st.text_input('What is your name?', '')
                   
if player_name != '':
    st.header(f'Hello {player_name} !')
    time.sleep(0.6)  
    st.subheader("Let's play a game")
    
    # 2. define rules and values                          
    weapons = ('⛰️ Rock', '🧻 Paper', '✂️ Scissors', '🦎 Lizard', '🖖 Spock') 
  
    rules = {"Scissors cuts Paper" : "tumblr_lht7icY7871qaraif",
         "Paper covers Rock" : "tumblr_lht7jsqpyK1qaraif",
         "Rock crushes Lizard" : "tumblr_lht7l5Jly01qaraif",
         "Lizard poisons Spock" : "tumblr_lht7mmIEv01qaraif",
         "Spock smashes Scissors" : "tumblr_lht7oufT2L1qaraif",
         "Scissors decapitates Lizard" :"tumblr_lht7qekne21qaraif",
         "Lizard eats Paper" : "tumblr_lht7rn4MUa1qaraif",
         "Paper disproves Spock" : "tumblr_lht7suBvjC1qaraif",
         "Spock vaporizes Rock" : "tumblr_lht7usCota1qaraif",
         "Rock crushes Scissors" : "tumblr_lht7wpuIjk1qaraif"}
    
    # 2.1 add rules info expander
    with st.expander("Game Rules"):
        st.write('\n- '+'\n- '.join(map(str, rules.keys() ) ) )
            
    left, right = st.columns([1,1.5])
    
    # 3. request choices
    with left:
        player_choice = st.radio("Select your weapon...", weapons)
        computer_choice = random.choice(weapons)  
        
        # 4. start game
        if st.button('Go'):

            with right:                
                # 5. show selected choices
                st.success(f"{player_name} = {player_choice}")
                time.sleep(.7)
                st.info(f"Computer = {computer_choice}")
                
                # 5.1 fake loading-animation
                with st.empty():
                    for loading in ("","Processing","","Processing",""):
                        st.caption(loading)
                        time.sleep(0.6)
                        
                # 6. draw?
                if player_choice == computer_choice:
                     st.warning("It is a draw! Let's go again!")

                # 7. find the choice-combination, define who is the winner
                else:
                    for result in rules.keys():
                        if player_choice.split()[1] in result.split() and computer_choice.split()[1] in result.split():
                            # st.subheader( result )

                            st.markdown(f"![{result}](https://64.media.tumblr.com/{rules[result]}.gif)")

                            if player_choice.split()[1] in result.split()[0]: 
                                st.success( f"{player_name} wins!" )
                            else:
                                st.info( "I win!" )
                # 8. reset              
                st.button('Restart')