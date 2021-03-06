import crypt
# CHAPTER 1 p22

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():   
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if ( cryptWord == cryptPass ):
            print("[+] Found Password: {} \n".format(word))
            return
    print("[-] Password not Found. \n")
    return

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print("[*] Cracking password for: {}".format(user))
            testPass(cryptPass)

if __name__ == "__main__":
    main()
