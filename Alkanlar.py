print('Alkanlar programi v1')
cs=int(input('Carbon atomlarinin sayini yazin: '))
hs=2*cs+2
print('\nNetice:\n'+'-'*50)
if cs==1:
    ad=('Metan')
if cs==2:
    ad=('Etan')
if cs==3:
    ad=('Propan')
if cs==4:
    ad=('Butan')
if cs==5:
    ad='Pentan'
if cs==6:
    ad=('Heksan')
if cs==7:
    ad=('Heptan')
if cs==8:
    ad=('Okan')
if cs==9:
    ad=('Nonan')
if cs==10:
    ad=('Dekan')
if cs>10:                   #burda diqqetli ol! Else ancaq 10 olan ife aiddi!
    ad=''
print('Formul:\n')
if cs==1:
    print(""" 
      H
      |        
    H-C-H       
      |
      H""")
else:
    l=cs-2
    print('  H',' H'*(l+1),sep='')
    print('  |',' |'*(l+1),sep='')
    print('H-C','-C'*l,'-C-H',sep='')
    print('  |',' |'*(l+1),sep='')
    print('  H',' H'*(l+1),sep='')
print('\nC{}H{}'.format(cs,hs),ad)
print('\nHibrid rabitelerin sayi: '+str(cs*4))
print('Polyar rabitelerin sayi: '+str(hs))
print('Qeyri polyar rabitelerin sayi: '+str(cs-1))
print('Molekul kutləsi: {}'.format(cs*12+hs*1))

input()
























