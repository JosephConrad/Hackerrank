def main():
    string=filter(lambda x: not x.isspace(), raw_input())
    allChars = set(map(chr, range(97, 123)))
    strChars=set()
    for elt in string:
        strChars.add(elt.lower()) 
    print ['not pangram', 'pangram'][strChars==allChars]

main()
