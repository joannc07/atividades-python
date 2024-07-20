def verif_num_primo ():

   num = int(input("Digite um número positivo e inteiro para verificar se é primo ou não: "))


   if num > 1:

       for i in range(2, num):

           if (num % i) == 0:
               print("O número {} não é primo!".format(num))
               break


       else:
           print("O número {} é um número primo!".format(num))



verif_num_primo()