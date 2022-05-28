import sys
print('Bitmap Message, By Prazwal D. Stark prazwaldstark@gmail.com')

bitmap = '''
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................'''
print('Enter the message to display with the bitmap')
message=input('>')
for line in bitmap.splitlines():
    for i,bit in enumerate(line):
        if bit==' ':
            print(' ',end='')
        else:
            print(message[i %len(message)],end='')
    print()