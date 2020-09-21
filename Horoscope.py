again = True  #initialising variable
while again:
    #Printing the zodiac sign name and number
    print("-"*80)
    print("| %-20s%-20s%-20s%-14s|\n| %-20s%-20s%-20s%-14s|\n| %-20s%-20s%-20s%-14s|"%("1. Aries \u2648",
                                                                              "2. Taurus \u2649",
                                                                              "3. Gemini \u264A",
                                                                              "4. Cancer \u264B",
                                                                              "5. Leo \u264C",
                                                                              "6. Virgo \u264D",
                                                                              "7. Libra \u264E",
                                                                              "8. Scorpio \u264F",
                                                                              "9. Sagittarius \u2650",
                                                                              "10. Capricorn \u2651",
                                                                              "11. Aquarius \u2652",
                                                                              "12. Pisces \u2653"))
    print('-'*80)
    #getting user's zodiac sign and printing corresponding horoscope
    horoscope_value = int(input("\nEnter the number corresponding to your zodiac\n"))
    if horoscope_value == 1:
        print("\nAll eyes may be on you today — for your looks, skills, or even your funky bag! Make hay while the sun shines, and charge your batteries with all that attention. You can get some decent work done with that energy, says Ganesha")
    elif horoscope_value == 2:
        print("\nSpontaneity yet sincerity will be the ruling emotions of the day. Keep your eyes and ears open, advises Ganesha, as trouble might be headed your way. Make it a point to read the print well before you sign any legal contract today. Prevention is better than cure, reminds Ganesha.")
    elif horoscope_value == 3:
        print("\nToday, your enthusiasm for sports and outdoor activities is palpable. According to you, variety is the spice of life. You will keep on jumping from one venture to another. You will establish a good rapport with your bosses and colleagues. It's time to taste success in your immediate and interim objectives.")
    elif horoscope_value == 4:
        print("\nIt is likely that you will reach an important milestone in life today. Keep in mind that your success may be a cause of envy for a few people, some of whom may want to harm you. You are left with two choices: either try to help them out of their troubles and miseries, or prepare for a battle.")
    elif horoscope_value == 5:
        print("\nForget the weather. Today, the only thing shining bright are your chances of spending some quality time with your near and dear ones. Going along these lines, Ganesha wonders how long has it been since you last did the same. So, make the most of this lucky day. Chances are that you shall make new friends, who might turn out to be very supportive in the future. Ganesha wishes you the very best on this eventful day.")
    elif horoscope_value == 6:
        print("\nBusiness acumen is natural to you. Your management skills are immaculate. Move with imagination, innovation and motivation to further your enterprise, advises Ganesha. Feel free to express and exercise your sense of judgement, says Ganesha.")
    elif horoscope_value == 7:
        print("\nThe whole point of being a Libran is that you always have the tendency to be two separate things put together on a pair of scales that somehow balance. Ganesha feels that today, you'll bring to the scales the stability of being your own master and servant. It's a fine balance to maintain. But only you are capable of doing that, thanks to your extremely high-power status today.")
    elif horoscope_value == 8:
        print("\nRetail therapy with your loved ones is a perfect recipe to have a good time! You will be more than willing to buy things of their choice. Haggling will be a trait you have closeted today as you go about being lavish in your expenses, says Ganesha.")
    elif horoscope_value == 9:
        print("\nYou may have women swooning over you today; such is your charm and way with them, says Ganesha. But friends are highly valuable to you, and you shall spend much time with them cherishing their company and reliving amazing times spent together.")
    elif horoscope_value == 10:
        print("\nYou love the people around you unconditionally and such emotions will be more visible now than ever. Today, you will want to keep yourself surrounded with your loved ones, make them happy and have a good time, says Ganesha. Your honesty and sincerity will give depth to your existing relationships.")
    elif horoscope_value == 11:
        print("\nGod helps those who help themselves. You have experienced this plenty of times as your efforts have been paid off. While your colleagues at work may pass negative comments at your work, your boss will not have any complains with you. For investments purposes, real estate and construction seem to be a wise option, suggests Ganesha.")
    elif horoscope_value == 12:
        print("\nYou will be able to come up trumps against the competition today. You should be wary of hidden enemies, for they might be involved in slandering you. It is best to reach out to others and make friends before they take it upon themselves to hinder your progress. Apart from this, no other significant event is indicated today, says Ganesha.")
    else:
        print("\nIs that valid zodiac?")

    #Getting whether the user want  to continue or exit
    again = True if input("\nKnow the fortune again? (Y/N)").lower() == 'y' else False
    print() #formatting purpose
