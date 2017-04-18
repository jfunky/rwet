#out must be an already defined list
#incr must be an already defined number variable
def pdfpages(p, start, end, out):
    n = 0
    for page in p.pages:
        if n > start and n < end:
            string = page.extractText()
            line = string.replace(".","\n")
            line2 = string.replace("''"," ")
            if len(line2) > 0:
                out.append(line2)
                for word in line2.split():
                    if len(word) > 0:
                        out.append(word)
        n = n + 1
